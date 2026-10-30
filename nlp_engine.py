"""
NLP Engine for Hospital Service Quality Intelligence & Medical Report Simplification
Project by: K. Priya & CH. Harshini (B.Tech CSE, Warangal)
"""

import os
import re
import string
import joblib
import numpy as np
import pandas as pd
from collections import Counter
from gtts import gTTS

# ============================================================
# 1. NLP STOPWORDS & CONFIGURATION
# ============================================================
STOP_WORDS = set("""
a an the and or but if then than so because as of at by for from in into on onto
to with about after before during through over under again further once here there
all any both each few more most other some such no nor not only own same too very
can will just should now is am are was were be been being have has had do does did
this that these those it its he him his she her hers they them their theirs we us
our ours you your yours i me my mine
""".split())

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
TFIDF_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.joblib")
SENTIMENT_MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.joblib")
ISSUE_MODEL_PATH = os.path.join(MODEL_DIR, "issue_model.joblib")


# ============================================================
# 2. TEXT PREPROCESSING (PIPELINE STEPS 1 - 5)
# ============================================================
def clean_text(text: str) -> str:
    """
    Standardized NLP text cleaning pipeline matching academic methodology:
    1. Case normalization (Lowercasing)
    2. URL, email, and digit removal
    3. Punctuation stripping
    4. Stopword filtering
    5. Rule-based morphological suffix reduction (Lemmatization/Stemming)
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()

    tokens = text.split()
    tokens = [w for w in tokens if w not in STOP_WORDS and len(w) > 2]

    cleaned_words = []
    for word in tokens:
        if word.endswith("ies") and len(word) > 4:
            word = word[:-3] + "y"
        elif word.endswith("ing") and len(word) > 5:
            word = word[:-3]
        elif word.endswith("ed") and len(word) > 4:
            word = word[:-2]
        elif word.endswith("es") and len(word) > 4:
            word = word[:-2]
        elif word.endswith("s") and len(word) > 3:
            word = word[:-1]
        cleaned_words.append(word)

    return " ".join(cleaned_words)


def tokenize(text: str) -> list:
    """Split text into individual word tokens."""
    cleaned = clean_text(text)
    return cleaned.split() if cleaned else []


# ============================================================
# 3. READABILITY METRICS (FLESCH-KINCAID)
# ============================================================
def count_syllables(word: str) -> int:
    word = word.lower()
    count = len(re.findall(r'[aeiouy]+', word))
    if word.endswith('e') and not word.endswith('le') and len(word) > 2:
        count = max(1, count - 1)
    return max(1, count)


def calculate_readability(text: str) -> dict:
    """
    Computes Flesch Reading Ease and Flesch-Kincaid Grade Level.
    Higher reading ease = easier to read (e.g. 70-80 = 7th grade).
    """
    sentences = max(1, len(re.split(r'[.!?]+', text.strip())))
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    total_words = max(1, len(words))
    total_syllables = sum(count_syllables(w) for w in words)

    # Standard Flesch Reading Formulas
    fk_grade = 0.39 * (total_words / sentences) + 11.8 * (total_syllables / total_words) - 15.59
    reading_ease = 206.835 - 1.015 * (total_words / sentences) - 84.6 * (total_syllables / total_words)

    fk_grade = max(1.0, min(18.0, round(fk_grade, 1)))
    reading_ease = max(0.0, min(100.0, round(reading_ease, 1)))

    if fk_grade <= 6:
        interpretation = "Very Easy (Middle School Level)"
    elif fk_grade <= 9:
        interpretation = "Plain Language (General Public)"
    elif fk_grade <= 12:
        interpretation = "High School Level"
    else:
        interpretation = "Dense Clinical Jargon (Post-Graduate)"

    return {
        "words": total_words,
        "sentences": sentences,
        "flesch_reading_ease": reading_ease,
        "flesch_kincaid_grade": fk_grade,
        "interpretation": interpretation
    }


# ============================================================
# 4. ASPECT, ISSUE & URGENCY DETECTION
# ============================================================
ISSUE_KEYWORDS = {
    "Long Waiting Time": [
        "wait", "waiting", "delay", "hours", "late", "queue", "slow", "line",
        "standing", "took long", "schedule", "time"
    ],
    "Billing Transparency": [
        "bill", "billing", "cost", "charge", "expensive", "fee", "money",
        "receipt", "overcharge", "hidden", "price", "insurance", "cash"
    ],
    "Staff Behavior & Nursing": [
        "rude", "staff", "nurse", "behavior", "attitude", "reception", "harsh",
        "arrogant", "unhelpful", "impatient", "disrespect", "careless"
    ],
    "Doctor Availability & Care": [
        "doctor", "consultation", "physician", "hurried", "unavailable",
        "unattentive", "diagnosis", "expert", "specialist"
    ],
    "Cleanliness & Hygiene": [
        "dirty", "washroom", "clean", "hygiene", "bathroom", "smell", "unclean",
        "bedsheet", "mosquito", "sanitation", "floor", "dust"
    ],
    "Digital Service & Records": [
        "app", "online", "portal", "digital", "system", "report download",
        "server", "booking", "sms", "token"
    ]
}

POSITIVE_LEXICON = {
    "excellent", "good", "great", "helpful", "polite", "professional",
    "clean", "supportive", "prompt", "satisfactory", "caring", "best",
    "smooth", "kind", "friendly", "fast", "hygienic", "well", "appreciate",
    "recommend", "compassionate", "effective", "neat", "organized"
}

NEGATIVE_LEXICON = {
    "rude", "worst", "terrible", "bad", "slow", "delayed", "horrible",
    "pathetic", "poor", "painful", "dirty", "unhelpful", "angry",
    "confusing", "disappointed", "irresponsible", "negligent", "arrogant",
    "expensive", "waste", "suffered", "careless", "unclean"
}


def analyze_feedback_aspects(text: str) -> dict:
    """Identifies primary service issue, detected issues, and sentiment signals."""
    lower_text = text.lower()
    detected_issues = []

    for issue, keywords in ISSUE_KEYWORDS.items():
        if any(re.search(r"\b" + re.escape(kw) + r"\b", lower_text) for kw in keywords):
            detected_issues.append(issue)

    if not detected_issues:
        primary_issue = "No Major Issue"
    else:
        primary_issue = detected_issues[0]

    # Calculate rule-based lexicon scores
    tokens = set(clean_text(text).split())
    pos_count = len(tokens.intersection(POSITIVE_LEXICON))
    neg_count = len(tokens.intersection(NEGATIVE_LEXICON))

    # Urgency analysis
    high_urgency_triggers = ["emergency", "critical", "severe", "life", "urgent", "negligence", "died", "blood", "complain", "terrible", "unbearable"]
    med_urgency_triggers = ["delay", "waiting", "rude", "billing", "problem", "disappointed", "mistake"]

    if any(w in lower_text for w in high_urgency_triggers) or neg_count >= 2:
        urgency = "High"
    elif any(w in lower_text for w in med_urgency_triggers) or neg_count >= 1 or detected_issues:
        urgency = "Medium"
    else:
        urgency = "Low"

    return {
        "primary_issue": primary_issue,
        "all_detected_issues": detected_issues,
        "urgency_level": urgency,
        "positive_hits": pos_count,
        "negative_hits": neg_count
    }


# ============================================================
# 5. INFERENCE CLASSIFIER WRAPPER
# ============================================================
class FeedbackClassifier:
    """Wrapper that manages TF-IDF Vectorizer and ML Classifier with graceful fallback."""

    def __init__(self):
        self.vectorizer = None
        self.model = None
        self.issue_model = None
        self.load_models()

    def load_models(self):
        try:
            if os.path.exists(TFIDF_PATH) and os.path.exists(SENTIMENT_MODEL_PATH):
                self.vectorizer = joblib.load(TFIDF_PATH)
                self.model = joblib.load(SENTIMENT_MODEL_PATH)
                if os.path.exists(ISSUE_MODEL_PATH):
                    self.issue_model = joblib.load(ISSUE_MODEL_PATH)
                return True
        except Exception as e:
            print(f"Notice: Loading saved model encountered: {e}. Falling back to dynamic pipeline.")
        return False

    def predict(self, text: str) -> dict:
        cleaned = clean_text(text)
        aspects = analyze_feedback_aspects(text)

        # 1. Check strong negative keywords
        if aspects["negative_hits"] > aspects["positive_hits"] and aspects["negative_hits"] >= 1:
            sentiment = "Negative"
            conf = 0.88 + min(aspects["negative_hits"] * 0.04, 0.10)
        elif self.model and self.vectorizer and cleaned:
            # Model prediction
            X_vec = self.vectorizer.transform([cleaned])
            pred = self.model.predict(X_vec)[0]
            probs = self.model.predict_proba(X_vec)[0]
            conf = float(np.max(probs))

            # Guard against false neutral on clear polarity
            if aspects["positive_hits"] >= 2 and aspects["negative_hits"] == 0:
                sentiment = "Positive"
                conf = max(conf, 0.92)
            elif aspects["negative_hits"] >= 1 and aspects["positive_hits"] == 0:
                sentiment = "Negative"
                conf = max(conf, 0.90)
            else:
                sentiment = pred
        else:
            # Heuristic fallback if models not yet generated
            if aspects["positive_hits"] > aspects["negative_hits"]:
                sentiment = "Positive"
                conf = 0.85
            elif aspects["negative_hits"] > 0:
                sentiment = "Negative"
                conf = 0.85
            else:
                sentiment = "Neutral"
                conf = 0.75

        # Service Quality Index (SQI) estimate (0-100)
        base_sqi = 75.0
        if sentiment == "Positive":
            base_sqi += 15.0 + min(aspects["positive_hits"] * 2.0, 8.0)
        elif sentiment == "Negative":
            base_sqi -= 25.0 + min(aspects["negative_hits"] * 4.0, 15.0)
        
        if aspects["primary_issue"] != "No Major Issue":
            base_sqi -= 6.0
        sqi = max(10.0, min(99.0, round(base_sqi, 1)))

        return {
            "original_text": text,
            "cleaned_text": cleaned,
            "tokens": cleaned.split(),
            "sentiment": sentiment,
            "confidence": round(conf * 100, 1),
            "primary_issue": aspects["primary_issue"],
            "detected_issues": aspects["all_detected_issues"],
            "urgency_level": aspects["urgency_level"],
            "estimated_sqi": sqi
        }


# ============================================================
# 6. CLINICAL BIOMARKER ONTOLOGY & REFERENCE RANGES
# ============================================================
CLINICAL_REFERENCE_DATABASE = {
    # Lipid Profile
    "total_cholesterol": {
        "names": ["total cholesterol", "cholesterol, total", "serum cholesterol"],
        "unit": "mg/dL",
        "normal_min": 125,
        "normal_max": 200,
        "display": "Total Cholesterol",
        "te_name": "మొత్తం కొలెస్ట్రాల్ (Total Cholesterol)",
        "desc": "Fat level in the bloodstream."
    },
    "ldl": {
        "names": ["ldl", "ldl cholesterol", "low density lipoprotein", "ldl-c"],
        "unit": "mg/dL",
        "normal_min": 0,
        "normal_max": 100,
        "display": "LDL Cholesterol ('Bad' Cholesterol)",
        "te_name": "చెడు కొలెస్ట్రాల్ (LDL)",
        "desc": "Builds up arterial plaque, increasing cardiac risks."
    },
    "hdl": {
        "names": ["hdl", "hdl cholesterol", "high density lipoprotein", "hdl-c"],
        "unit": "mg/dL",
        "normal_min": 40,
        "normal_max": 60,
        "display": "HDL Cholesterol ('Good' Cholesterol)",
        "te_name": "మంచి కొలెస్ట్రాల్ (HDL)",
        "desc": "Protective cholesterol clearing blood vessels."
    },
    "triglycerides": {
        "names": ["triglycerides", "serum triglycerides", "tg"],
        "unit": "mg/dL",
        "normal_min": 0,
        "normal_max": 150,
        "display": "Triglycerides",
        "te_name": "ట్రైగ్లిజరైడ్స్ (రక్తంలో కొవ్వు నిల్వలు)",
        "desc": "Fat storage in blood from caloric excess."
    },
    # Diabetes / Glucose
    "fasting_blood_sugar": {
        "names": ["fasting blood sugar", "fasting glucose", "fbs", "glucose, fasting"],
        "unit": "mg/dL",
        "normal_min": 70,
        "normal_max": 99,
        "display": "Fasting Blood Sugar (FBS)",
        "te_name": "పరగడుపున చక్కెర స్థాయి (Fasting Blood Sugar)",
        "desc": "Blood glucose after overnight fasting."
    },
    "post_prandial_sugar": {
        "names": ["post prandial", "ppbs", "post-prandial blood sugar", "glucose pp"],
        "unit": "mg/dL",
        "normal_min": 70,
        "normal_max": 140,
        "display": "Post-Prandial Glucose (PPBS)",
        "te_name": "భోజనం తర్వాత చక్కెర స్థాయి (PPBS)",
        "desc": "Blood sugar 2 hours after meal."
    },
    "hba1c": {
        "names": ["hba1c", "glycated hemoglobin", "glycosylated hemoglobin", "a1c"],
        "unit": "%",
        "normal_min": 4.0,
        "normal_max": 5.6,
        "display": "HbA1c (3-Month Sugar Average)",
        "te_name": "3 నెలల చక్కెర సగటు (HbA1c)",
        "desc": "Gold-standard 90-day average blood glucose."
    },
    # CBC / Hematology
    "hemoglobin": {
        "names": ["hemoglobin", "hb", "haemoglobin"],
        "unit": "g/dL",
        "normal_min": 12.0,
        "normal_max": 16.5,
        "display": "Hemoglobin",
        "te_name": "రక్తంలో హిమోగ్లోబిన్ (Hemoglobin)",
        "desc": "Oxygen-carrying protein in red blood cells."
    },
    "wbc_count": {
        "names": ["wbc", "total wbc count", "leukocyte count", "white blood cells"],
        "unit": "cells/mcL",
        "normal_min": 4000,
        "normal_max": 11000,
        "display": "White Blood Cells (WBC)",
        "te_name": "తెల్ల రక్తకణాలు (WBC - రోగనిరోధక కణాలు)",
        "desc": "Immune system infection defense cells."
    },
    "platelets": {
        "names": ["platelet count", "platelets"],
        "unit": "lakhs/mcL",
        "normal_min": 1.5,
        "normal_max": 4.5,
        "display": "Platelet Count",
        "te_name": "ప్లేట్‌లెట్స్ (రక్తం గడ్డకట్టే కణాలు)",
        "desc": "Cells responsible for blood clotting."
    },
    # Liver Function
    "sgot_ast": {
        "names": ["sgot", "ast", "aspartate aminotransferase"],
        "unit": "U/L",
        "normal_min": 10,
        "normal_max": 40,
        "display": "SGOT / AST (Liver Enzyme)",
        "te_name": "కాలేయ ఎంజైమ్ (SGOT)",
        "desc": "Enzyme released during liver or muscle cell stress."
    },
    "sgpt_alt": {
        "names": ["sgpt", "alt", "alanine aminotransferase"],
        "unit": "U/L",
        "normal_min": 7,
        "normal_max": 56,
        "display": "SGPT / ALT (Liver Enzyme)",
        "te_name": "కాలేయ ఎంజైమ్ (SGPT)",
        "desc": "Key marker of liver cellular integrity."
    },
    # Kidney Function
    "serum_creatinine": {
        "names": ["serum creatinine", "creatinine"],
        "unit": "mg/dL",
        "normal_min": 0.6,
        "normal_max": 1.2,
        "display": "Serum Creatinine",
        "te_name": "సీరమ్ క్రియాటినిన్ (కిడ్నీ పనితీరు)",
        "desc": "Primary biomarker for kidney filtration health."
    }
}


# ============================================================
# 7. CLINICAL REPORT SIMPLIFIER & TELUGU GENERATOR
# ============================================================
def extract_biomarkers(report_text: str) -> list:
    """
    Extracts clinical biomarkers, values, and units from unstructured lab report text
    and compares with normal reference intervals with zero numerical distortion.
    """
    extracted = []
    text_lower = report_text.lower()

    for key, info in CLINICAL_REFERENCE_DATABASE.items():
        for name in info["names"]:
            # Pattern matching: parameter name followed by optional colon/dash and numeric value
            pattern = re.compile(
                r"\b" + re.escape(name) + r"\b[\s:=-]+([0-9]+(?:\.[0-9]+)?)",
                re.IGNORECASE
            )
            match = pattern.search(text_lower)
            if match:
                val = float(match.group(1))
                min_n = info["normal_min"]
                max_n = info["normal_max"]

                if val < min_n:
                    status = "Low"
                    status_te = "తక్కువగా ఉంది (Low)"
                    status_color = "#2563eb"  # blue
                elif val > max_n:
                    status = "Elevated"
                    status_te = "సాధారణం కంటే ఎక్కువగా ఉంది (High)"
                    status_color = "#dc2626"  # red
                else:
                    status = "Normal"
                    status_te = "సాధారణ స్థాయిలో ఉంది (Normal)"
                    status_color = "#16a34a"  # green

                extracted.append({
                    "key": key,
                    "parameter": info["display"],
                    "parameter_te": info["te_name"],
                    "value": val,
                    "unit": info["unit"],
                    "normal_range": f"{min_n} - {max_n} {info['unit']}",
                    "status": status,
                    "status_te": status_te,
                    "status_color": status_color,
                    "description": info["desc"]
                })
                break  # avoid duplicate alias matches for same marker

    return extracted


def simplify_medical_report(report_text: str) -> dict:
    """
    Transforms dense medical diagnostic reports into:
    1. Plain-English patient summary with Flesch-Kincaid grade level reduction.
    2. Zero-hallucination, culturally accessible regional Telugu explanation.
    3. Actionable lifestyle advice and doctor visit notes.
    """
    biomarkers = extract_biomarkers(report_text)
    readability_original = calculate_readability(report_text)

    plain_english_points = []
    telugu_sentences = []
    urgent_flags = []

    if biomarkers:
        for b in biomarkers:
            val_str = f"{b['value']} {b['unit']}"
            if b['status'] == "Elevated":
                plain_english_points.append(
                    f"**{b['parameter']}** is higher than normal ({val_str}, standard healthy range is {b['normal_range']}). {b['description']}"
                )
                telugu_sentences.append(
                    f"మీ రక్త పరీక్షలో **{b['parameter_te']}** స్థాయి **{val_str}** గా నమోదైంది. ఇది సాధారణ స్థాయి ({b['normal_range']}) కంటే **ఎక్కువగా ఉంది**. కాబట్టి జాగ్రత్త వహించాలి."
                )
                urgent_flags.append(b['parameter'])
            elif b['status'] == "Low":
                plain_english_points.append(
                    f"**{b['parameter']}** is lower than normal ({val_str}, standard healthy range is {b['normal_range']})."
                )
                telugu_sentences.append(
                    f"మీ రక్త పరీక్షలో **{b['parameter_te']}** స్థాయి **{val_str}** గా నమోదైంది, ఇది సాధారణ స్థాయి ({b['normal_range']}) కంటే **తక్కువగా ఉంది**."
                )
                urgent_flags.append(b['parameter'])
            else:
                plain_english_points.append(
                    f"**{b['parameter']}** is normal ({val_str})."
                )
                telugu_sentences.append(
                    f"మీ రక్త పరీక్షలో **{b['parameter_te']}** స్థాయి **{val_str}** తో **సాధారణ ఆరోగ్యకరమైన పరిధిలో ఉంది**."
                )
    else:
        # General text fallback if no standard lab parameters matched
        plain_english_points.append("The medical report describes clinical observations regarding your current consultation.")
        telugu_sentences.append("ఈ మెడికల్ రిపోర్ట్ మీ వైద్య పరీక్షల వివరాలను తెలియజేస్తోంది. వైద్యుల సలహా ప్రకారం తగిన సూచనలు పాటించండి.")

    # Doctor consultation guidance
    if urgent_flags:
        plain_english_summary = (
            f"Overall Diagnostic Summary: Several lab values require attention ({', '.join(urgent_flags)}). "
            "Please schedule a consultation with your treating physician for medical advice and prescriptions. "
            "Maintain proper hydration, a balanced diet, and avoid self-medication."
        )
        telugu_guidance = (
            "ముఖ్య గమనిక: మీ నివేదికలోని కొన్ని అంశాలు ({flags}) వైద్యుల పర్యవేక్షణ అవసరమని సూచిస్తున్నాయి. "
            "దయచేసి వరంగల్‌లోని మీ సమీప ఆసుపత్రి వైద్యులను సంప్రదించి సరైన మందులు మరియు ఆహార నియమాలను పాటించండి."
        ).format(flags=", ".join([b['parameter_te'] for b in biomarkers if b['status'] != 'Normal']))
    else:
        plain_english_summary = (
            "Overall Diagnostic Summary: All extracted parameters are within healthy reference limits. "
            "Continue regular physical activity, balanced nutrition, and scheduled routine health check-ups."
        )
        telugu_guidance = (
            "ముఖ్య గమనిక: మీ రక్త పరీక్షల ఫలితాలు ఆరోగ్యకరమైన పరిధిలోనే ఉన్నాయి. "
            "మంచి ఆహారపు అలవాట్లు, రోజువారీ వ్యాయామం కొనసాగించండి."
        )

    full_plain_english = "\n\n".join([plain_english_summary] + [f"- {p}" for p in plain_english_points])
    full_telugu = " ".join(telugu_sentences) + "\n\n" + telugu_guidance

    readability_simplified = calculate_readability(full_plain_english)

    return {
        "biomarkers": biomarkers,
        "original_readability": readability_original,
        "simplified_readability": readability_simplified,
        "plain_english_summary": plain_english_summary,
        "plain_english_points": plain_english_points,
        "full_plain_english": full_plain_english,
        "telugu_explanation": full_telugu,
        "has_abnormal": len(urgent_flags) > 0,
        "abnormal_count": len(urgent_flags)
    }


def generate_telugu_tts(telugu_text: str, output_path: str = "telugu_audio.mp3") -> str:
    """Synthesizes speech audio for regional Telugu explanation using gTTS."""
    clean_speech_text = re.sub(r'[*#_`]', '', telugu_text)
    clean_speech_text = clean_speech_text.replace('\n', ' ')
    tts = gTTS(text=clean_speech_text, lang='te', slow=False)
    tts.save(output_path)
    return output_path


# Initialize singleton classifier
classifier_instance = FeedbackClassifier()
