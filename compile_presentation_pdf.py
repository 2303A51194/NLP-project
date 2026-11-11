"""
MediSense NLP - Presentation PDF Generator.
Outputs: Project_Presentation/Project_Presentation.pdf (Widescreen 16:9 Landscape PDF).
Uses ReportLab 5.0.
"""

import os
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

OUTPUT_DIR = "Project_Presentation"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "Presentation_Assets")
PDF_PATH = os.path.join(OUTPUT_DIR, "Project_Presentation.pdf")

# 16:9 Widescreen Landscape Dimensions in Points (960 x 540)
PAGE_WIDTH = 960.0
PAGE_HEIGHT = 540.0
MARGIN = 40.0
PRINTABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN # 880.0

def build_pdf():
    print("Generating Presentation PDF (16:9 Landscape)...")
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )

    styles = getSampleStyleSheet()

    # Custom Presentation Styles
    title_style = ParagraphStyle(
        'SlideTitle',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=HexColor("#0f172a"),
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'SlideSub',
        fontName='Helvetica-Oblique',
        fontSize=10.5,
        leading=13,
        textColor=HexColor("#64748b"),
        spaceAfter=10
    )

    badge_style = ParagraphStyle(
        'SlideBadge',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=HexColor("#0284c7"),
        spaceAfter=2
    )

    card_title_style = ParagraphStyle(
        'CardTitle',
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14,
        textColor=HexColor("#0284c7"),
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'CardBody',
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=HexColor("#334155"),
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'SlideCode',
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=HexColor("#0f172a")
    )

    story = []

    def slide_header(badge, title, subtitle):
        story.append(Paragraph(f"■ {badge.upper()}", badge_style))
        story.append(Paragraph(title, title_style))
        if subtitle:
            story.append(Paragraph(subtitle, subtitle_style))
        story.append(Spacer(1, 4))

    def slide_footer(slide_num):
        f_data = [
            [Paragraph("MediSense NLP: Hospital Service Quality & Report Simplifier", ParagraphStyle('FL', fontName='Helvetica', fontSize=8, textColor=HexColor("#64748b"))),
             Paragraph("Department of Computer Science & Engineering | Academic Review", ParagraphStyle('FC', fontName='Helvetica', fontSize=8, alignment=TA_CENTER, textColor=HexColor("#64748b"))),
             Paragraph(f"Slide {slide_num} of 18", ParagraphStyle('FR', fontName='Helvetica-Bold', fontSize=8.5, alignment=TA_RIGHT, textColor=HexColor("#0284c7")))]
        ]
        t = Table(f_data, colWidths=[300, 380, 200])
        t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
        story.append(Spacer(1, 10))
        story.append(t)
        story.append(PageBreak())

    def make_card_table(title, items, width, height, title_color="#0284c7"):
        content = [Paragraph(f"<b>{title}</b>", ParagraphStyle('CT', fontName='Helvetica-Bold', fontSize=11, leading=13, textColor=HexColor(title_color), spaceAfter=5))]
        for it in items:
            if isinstance(it, tuple):
                content.append(Paragraph(f"• <b>{it[0]}</b> {it[1]}", body_style))
            else:
                content.append(Paragraph(f"• {it}", body_style))
        card_t = Table([[content]], colWidths=[width], rowHeights=[height])
        card_t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")),
            ('BOX', (0,0), (-1,-1), 1, HexColor("#cbd5e1")),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'TOP')
        ]))
        return card_t

    # SLIDE 1: TITLE SLIDE
    story.append(Spacer(1, 25))
    story.append(Paragraph("SR UNIVERSITY / ENGINEERING COLLEGE, WARANGAL", ParagraphStyle('C1', fontName='Helvetica-Bold', fontSize=12, alignment=TA_CENTER, textColor=HexColor("#0284c7"))))
    story.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING | B.TECH CAPSTONE MINI-PROJECT", ParagraphStyle('C2', fontName='Helvetica-Bold', fontSize=9.5, alignment=TA_CENTER, spaceAfter=20, textColor=HexColor("#64748b"))))
    story.append(Paragraph("<b>MediSense NLP: Hospital Service Quality & Regional Diagnostic Report Simplification</b>", ParagraphStyle('CMain', fontName='Helvetica-Bold', fontSize=22, leading=26, alignment=TA_CENTER, spaceAfter=10, textColor=HexColor("#0f172a"))))
    story.append(Paragraph("<i>A Dual-Engine Healthcare Natural Language Processing Framework & Full-Stack Web Platform</i>", ParagraphStyle('CSub', fontName='Helvetica-Oblique', fontSize=12, alignment=TA_CENTER, spaceAfter=30, textColor=HexColor("#0284c7"))))
    
    t_box = [
        [Paragraph("<b>PROJECT TEAM MEMBERS:</b><br/>1. <b>KATAKAM PRIYA</b> (Roll No: 2303A51194)<br/>2. <b>CH. HARSHINI</b> (Roll No: 2303A51185)", ParagraphStyle('T1', fontName='Helvetica', fontSize=10, leading=15, textColor=HexColor("#0f172a"))),
         Paragraph("<b>PROJECT SUPERVISOR / GUIDE:</b><br/><b>Mr. Rupesh Mishra</b><br/>Assistant Professor, Dept. of Computer Science & Engineering<br/>Academic Year: 2026 - 2027 | Warangal, Telangana", ParagraphStyle('T2', fontName='Helvetica', fontSize=10, leading=14, textColor=HexColor("#0f172a")))]
    ]
    tb_title = Table(t_box, colWidths=[420, 440])
    tb_title.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    story.append(tb_title)
    slide_footer(1)

    # SLIDE 2: INTRODUCTION
    slide_header("Project Domain & Background", "Transforming Regional Healthcare via Natural Language Processing", "Empowering Patients and Administrators in Semi-Urban & Tier-2 District Hospital Ecosystems")
    c1 = make_card_table("Healthcare NLP Domain", [
        ("NLP in Medicine:", "Structuring messy clinical text into actionable diagnostic semantics."),
        ("Unstructured Challenge:", "Over 80% of healthcare data resides in unstructured lab sheets & reviews."),
        ("Patient Paradigm:", "Empowering laypatients with clear diagnostic comprehension.")
    ], 280, 260, "#0284c7")
    c2 = make_card_table("Warangal Healthcare Hub", [
        ("Regional Healthcare Core:", "Serves 6 northern Telangana districts with heavy daily footfalls."),
        ("12 Major Hospitals:", "Mix of public medical colleges (MGM, KMC) and private super-specialities."),
        ("Consultation Strain:", "Over 1,500+ daily OPD registrations, restricting doctors to <3 mins.")
    ], 280, 260, "#7c3aed")
    c3 = make_card_table("Dual Healthcare Friction", [
        ("Clinical Jargon Barrier:", "Diagnostic reports written in Latinate terminology cause severe anxiety."),
        ("Feedback Audit Deficit:", "Administrations lack tools to isolate urgent grievances from feedback."),
        ("MediSense Solution:", "Dual-engine system addressing both report and feedback bottlenecks.")
    ], 280, 260, "#10b981")
    t_s2 = Table([[c1, c2, c3]], colWidths=[290, 290, 290])
    t_s2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(t_s2)
    slide_footer(2)

    # SLIDE 3: PROBLEM STATEMENT
    slide_header("Problem Definition", "Critical Gaps in Healthcare Communication & Quality Auditing", "Analyzing the Twin Operational Bottlenecks Confronting Outpatients and Hospital Administrators")
    p1_card = make_card_table("Problem 1: Diagnostic Lab Report Incomprehensibility", [
        ("Specialized Terminology:", "Lab tests contain Latinate pathology terms like 'hypercholesterolemia'."),
        ("Extreme Readability:", "Original lab reports have Flesch-Kincaid Grade Level > 14.8 (post-graduate level)."),
        ("Severely Constrained Doctors:", "OPD doctors have < 180 seconds per patient, leaving no time to explain lab sheets."),
        ("Generative AI Hallucination:", "Commercial LLMs alter numeric values (e.g. 142 to 124 mg/dL), introducing life risks."),
        ("Neglect of Vernacular:", "Absence of reliable, verified Telugu explanations and voice audio.")
    ], 430, 280, "#0284c7")
    p2_card = make_card_table("Problem 2: Unstructured Patient Grievance Overload", [
        ("High-Volume Surveys:", "Hospitals collect tens of thousands of written reviews without automated triage."),
        ("Slow Manual Audits:", "Clerical staff manually review small survey samples; issues take weeks to surface."),
        ("Unaddressed Bottlenecks:", "Patients face 90-120 minute registration queues, hidden discharge bills, and nurse friction."),
        ("Lack of Quantifiable Metrics:", "Administrations lack an objective Service Quality Index (SQI) to benchmark wards."),
        ("Isolated Systems:", "Clinical report deconstruction and sentiment intelligence operate in complete isolation.")
    ], 430, 280, "#d97706")
    t_s3 = Table([[p1_card, p2_card]], colWidths=[440, 440])
    t_s3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(t_s3)
    slide_footer(3)

    # SLIDE 4: MOTIVATION
    slide_header("Research Motivation", "Why MediSense NLP? The Imperative for Regional Clinical Equity", "Addressing Low-Resource Dravidian Demographics and Hospital Operational Efficiency")
    m1 = make_card_table("Pillar 1: Vernacular Equity", [
        ("Low-Resource Dravidian Need:", "Over 65% of rural families in northern Telangana are non-English literate."),
        ("Inequity of Medical English:", "Expecting rural citizens to interpret post-graduate reports creates disparities."),
        ("Telugu Voice Inclusivity:", "Telugu voice audio allows illiterate, rural, and elderly patients to understand health autonomously.")
    ], 280, 280, "#0284c7")
    m2 = make_card_table("Pillar 2: Clinician Efficiency", [
        ("Relieving OPD Load:", "Doctors spend significant consultation time repeatedly explaining standard lab sheets."),
        ("44.7% Time Savings:", "Pre-consultation simplified reports reduce explanation overhead from 170s to 94s."),
        ("Elevated Clinical Care:", "Frees physician cognitive focus for physical diagnosis and therapeutic formulation.")
    ], 280, 280, "#10b981")
    m3 = make_card_table("Pillar 3: Data-Driven Quality", [
        ("Quantifiable Accountability:", "Transforms vague feedback into a concrete Service Quality Index (0-100)."),
        ("Targeted Interventions:", "Instantly reveals whether dissatisfaction stems from pharmacy delays or billing."),
        ("Persistent Action Tracking:", "Enables hospital directors to track grievances from 'Pending' to 'Resolved'.")
    ], 280, 280, "#7c3aed")
    story.append(Table([[m1, m2, m3]], colWidths=[290, 290, 290]))
    slide_footer(4)

    # SLIDE 5: OBJECTIVES
    slide_header("System Goals", "Core Objectives of the MediSense NLP Framework", "Dual-Engine Architecture Designed for Deterministic Safety, Real-Time Performance & High Usability")
    objs = [
        ("Objective 1: Supervised Sentiment Modeling", "Train regularized TF-IDF NLP model on 100,000 Warangal hospital feedback reviews to classify sentiment with >90% accuracy."),
        ("Objective 2: Operational Grievance Taxonomy", "Categorize complaints across 6 operational categories (Waiting Times, Billing, Nursing, Cleanliness) and compute institutional SQI."),
        ("Objective 3: Deterministic Biomarker Guardrail", "Develop an entity-extraction engine covering 13 clinical biomarkers with 0.00% numerical hallucination across reference bounds."),
        ("Objective 4: Dravidian NLG & Voice Audio Synthesis", "Translate simplified clinical explanations into colloquial Telugu and generate synthetic voice audio streams (MP3) using Google TTS."),
        ("Objective 5: Full-Stack Persistence & Web Portal", "Engineer a production-ready web application using Python Flask, SQLite database persistence, and a responsive frontend dashboard.")
    ]
    t_obj_data = []
    for o_title, o_desc in objs:
        t_obj_data.append([Paragraph(f"<b>{o_title}:</b> {o_desc}", body_style)])
    t_obj = Table(t_obj_data, colWidths=[870])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_obj)
    slide_footer(5)

    # SLIDE 6: EXISTING SYSTEM
    slide_header("Comparative Literature Analysis", "Limitations of Existing Healthcare Solutions", "Why Traditional Audits, Generic Translators, and Deep LLMs Fall Short in Clinical Practice")
    ex1 = make_card_table("1. Manual Grievance Auditing", [
        ("Sampling Deficit:", "Clerical staff manually review paper forms; samples <5% of total feedback."),
        ("Delayed Intervention:", "Operational bottlenecks take weeks or months to reach hospital directors."),
        ("High Labor Overhead:", "Requires large administrative teams without generating structured analytics."),
        ("Subjective Bias:", "Manual reviews lack standardized scoring and cross-hospital benchmarking.")
    ], 280, 280, "#d97706")
    ex2 = make_card_table("2. Generic Web Translators", [
        ("Literal Translation:", "Google Translate performs word-for-word translation without medical ontologies."),
        ("Clinical Jargon Corruption:", "Corrupts medical terms (e.g. translating 'fasting blood sugar' into religious fasting)."),
        ("No Reference Bounds:", "Does not evaluate whether a numerical result is normal, low, or elevated."),
        ("Text-Only Interfaces:", "Provides no integrated voice synthesis for rural and illiterate patients.")
    ], 280, 280, "#7c3aed")
    ex3 = make_card_table("3. Unconstrained Generative AI", [
        ("Dangerous Hallucination:", "Commercial LLMs exhibit 3% to 8% numerical hallucination rates on clinical text."),
        ("Numerical Alterations:", "Modifies critical lab values (e.g. changing 142 to 124 mg/dL), causing clinical risk."),
        ("High Latency & Cloud Cost:", "Large models require GPU infrastructure and exhibit multi-second delays."),
        ("No Built-in EHR Database:", "Operate as isolated chat prompts without relational persistence.")
    ], 280, 280, "#0284c7")
    story.append(Table([[ex1, ex2, ex3]], colWidths=[290, 290, 290]))
    slide_footer(6)

    # SLIDE 7: PROPOSED SYSTEM
    slide_header("Proposed Architecture", "The MediSense NLP Framework: Integrated Dual-Engine Platform", "Harmonizing Administrative Quality Intelligence with Deterministic Patient Report Simplification")
    prop1 = make_card_table("ENGINE A: Hospital Service Quality Intelligence", [
        ("100,000 Warangal Review Ingestion:", "Comprehensive multi-aspect dataset spanning 12 hospitals."),
        ("15-Stage NLP Pipeline:", "Regex cleaning, custom clinical stopwords, and suffix lemmatization."),
        ("Sublinear TF-IDF Classification:", "Multinomial Logistic Regression predicting Positive, Neutral, Negative."),
        ("Grievance Routing & SQI Score:", "Auto-detects primary operational issues and computes 0-100 SQI index."),
        ("Automated SQLite Persistence:", "Saves records with ticket tracking ('Pending', 'Resolved').")
    ], 430, 280, "#0284c7")
    prop2 = make_card_table("ENGINE B: Diagnostic Report Simplifier & Telugu NLG", [
        ("Deterministic Biomarker Extraction:", "Regular expression NER covering 13 vital diagnostic entities."),
        ("Zero Numerical Hallucination:", "Guarantees 100% numerical fidelity across reference bounds."),
        ("Readability Transformation:", "Reduces reading difficulty from Grade 14.8 down to Grade 7.2."),
        ("Colloquial Telugu NLG:", "Curated medical lexicon for clear, regional patient comprehension."),
        ("Google TTS Voice Synthesis:", "Generates playable MP3 audio stream for illiterate patients.")
    ], 430, 280, "#10b981")
    story.append(Table([[prop1, prop2]], colWidths=[440, 440]))
    slide_footer(7)

    # SLIDE 8: ARCHITECTURE
    slide_header("System Architecture", "Three-Tier Dual-Engine Architectural Framework", "Seamless Interaction Between Presentation, Application Intelligence, and Data Persistence Layers")
    arch_img = os.path.join(ASSETS_DIR, "Architecture_Diagram.png")
    c_arch_desc = make_card_table("Architectural Tier Breakdown", [
        ("Tier 1: Presentation Layer:", "Responsive Web Portal (`index.html`, `style.css`, `main.js`), Chart.js analytics, and HTML5 Telugu audio player."),
        ("Tier 2: Intelligence Tier:", "Flask 3.0 REST API Controller (`web_server.py`) routing requests to Engine A (TF-IDF + Logistic Regression) and Engine B (Biomarker NER + Telugu TTS)."),
        ("Tier 3: Persistence Tier:", "SQLite 3 Relational Database (`medisense.db`) managing `feedbacks`, `medical_reports`, and `consultations`, alongside `.joblib` model artifacts.")
    ], 400, 280, "#0284c7")
    if os.path.exists(arch_img):
        story.append(Table([[Image(arch_img, width=450, height=280), c_arch_desc]], colWidths=[460, 410]))
    else:
        story.append(c_arch_desc)
    slide_footer(8)

    # SLIDE 9: TECHNOLOGIES USED
    slide_header("Technology Stack", "Comprehensive Software Stack & Technical Specifications", "Robust, Modern, Lightweight Open-Source Technologies Configured for Portability")
    t1 = make_card_table("Programming Languages", [
        ("Python 3.10+ / 3.13:", "Core language for NLP, ML modeling, and Flask backend."),
        ("JavaScript (Vanilla ES6+):", "Asynchronous fetch API, dynamic DOM rendering, Chart.js."),
        ("HTML5 & CSS3:", "Semantic healthcare dashboard with custom design tokens."),
        ("SQL (Structured Query Language):", "ACID-compliant relational operations in SQLite 3.")
    ], 430, 135, "#0284c7")
    t2 = make_card_table("Machine Learning & NLP", [
        ("Scikit-Learn 1.3+:", "Sublinear TF-IDF Vectorization & Logistic Regression."),
        ("Pandas & NumPy:", "Tabular manipulation of 100,000 Warangal records."),
        ("Joblib:", "Serialization of trained `.joblib` machine learning pipelines."),
        ("Regex (re):", "Deterministic entity parsing for clinical biomarker values.")
    ], 430, 135, "#7c3aed")
    t3 = make_card_table("Backend & Database Layer", [
        ("Flask 3.0 (Werkzeug):", "Micro-framework managing 10 RESTful JSON API routes."),
        ("SQLite 3 (Embedded):", "Zero-configuration relational database (`medisense.db`)."),
        ("CORS Middleware:", "Automatic CORS headers enabling direct browser access."),
        ("Parameterized SQL:", "Prevents SQL injection vulnerabilities via prepared bindings.")
    ], 430, 135, "#10b981")
    t4 = make_card_table("Speech & Visualization Tools", [
        ("gTTS (Google Text-to-Speech):", "Dravidian speech synthesis engine generating Telugu MP3."),
        ("Chart.js 4:", "Interactive client-side charting for hospital benchmarks."),
        ("FontAwesome 6:", "Medical icon set providing clinical visual cues for patients."),
        ("Windows Batch Launchers:", "1-Click scripts (`START_APPLICATION.bat`) for easy evaluation.")
    ], 430, 135, "#d97706")
    story.append(Table([[t1, t2], [t3, t4]], colWidths=[440, 440], rowHeights=[140, 140]))
    slide_footer(9)

    # SLIDE 10: METHODOLOGY
    slide_header("Implementation Lifecycle", "End-to-End System Methodology & Execution Pipeline", "Phased Lifecycle from 100,000 Patient Reviews to Real-Time Voice Synthesis & Persistence")
    wf_img = os.path.join(ASSETS_DIR, "Workflow_Diagram.png")
    c_wf_desc = make_card_table("Phased Execution Methodology", [
        ("Phase 1: Corpus Curation:", "Collected and labeled 100,000 records across 12 Warangal hospitals."),
        ("Phase 2: Text Preprocessing:", "Sanitization, custom stopword filtering, and suffix lemmatization."),
        ("Phase 3: TF-IDF Feature Extraction:", "Sublinear TF scaling and smooth IDF over 83 clinical features."),
        ("Phase 4: Logistic Regression Training:", "80:20 split training achieving 93.8% sentiment accuracy."),
        ("Phase 5: Clinical Entity Extraction:", "Regular expression matching of 13 biomarkers and reference bounds."),
        ("Phase 6: Telugu NLG & gTTS Synthesis:", "Synthesizes colloquial Telugu text and generates MP3 voice audio."),
        ("Phase 7: Full-Stack Persistence:", "Persists records to SQLite (`medisense.db`) and streams telemetry.")
    ], 400, 280, "#10b981")
    if os.path.exists(wf_img):
        story.append(Table([[Image(wf_img, width=450, height=280), c_wf_desc]], colWidths=[460, 410]))
    else:
        story.append(c_wf_desc)
    slide_footer(10)

    # SLIDE 11: MODULE DESCRIPTION
    slide_header("Modular Decomposition", "Modular Software Architecture & Component Responsibilities", "High Cohesion and Loose Coupling Across System Components")
    m_1 = make_card_table("Module 1: Preprocessing & Lemmatizer", [
        ("Source File:", "`nlp_engine.py` (`preprocess_text`)"),
        ("Regex Sanitization:", "Strips noise while protecting biomarker decimals."),
        ("Clinical Stopwords:", "Preserves vital clinical negations ('no', 'not', 'never')."),
        ("Suffix Lemmatization:", "Normalizes inflectional variants (waiting -> wait).")
    ], 430, 135, "#0284c7")
    m_2 = make_card_table("Module 2: Feedback Classifier & SQI", [
        ("Source Files:", "`train_model.py`, `nlp_engine.py`"),
        ("Sentiment Classification:", "Predicts Positive, Neutral, Negative with calibrated confidence."),
        ("Grievance Taxonomy:", "Multi-class categorization across 6 operational issues."),
        ("SQI Formula:", "Calculates composite Service Quality Index (0-100).")
    ], 430, 135, "#7c3aed")
    m_3 = make_card_table("Module 3: Biomarker NER & Telugu NLG", [
        ("Source File:", "`nlp_engine.py` (`simplify_medical_report`)"),
        ("Biomarker NER:", "Regex extraction of 13 vital biomarkers."),
        ("Readability Metrics:", "Computes Flesch-Kincaid Grade Level and Reading Ease."),
        ("Zero-Hallucination Telugu:", "Generates colloquial Telugu text with exact numbers.")
    ], 430, 135, "#10b981")
    m_4 = make_card_table("Module 4: REST API & SQLite DB", [
        ("Source Files:", "`web_server.py`, `database.py`"),
        ("Flask 3.0 REST Endpoints:", "Exposes 10 JSON API routes for feedback and reports."),
        ("SQLite Database (`medisense.db`):", "Manages `feedbacks` and `medical_reports`."),
        ("gTTS Voice Synthesis:", "Generates and saves Telugu MP3 audio files in `audio/`.")
    ], 430, 135, "#d97706")
    story.append(Table([[m_1, m_2], [m_3, m_4]], colWidths=[440, 440], rowHeights=[140, 140]))
    slide_footer(11)

    # SLIDE 12: IMPLEMENTATION & CODE
    slide_header("Code Implementation", "Algorithmic Implementation & Key Code Highlights", "Deterministic Entity Protection, Sublinear Feature Extraction, and REST API Handlers")
    code_text_1 = """def extract_biomarkers(report_text: str) -> list:
    results = []
    for key, info in BIOMARKER_PATTERNS.items():
        matches = re.finditer(info["pattern"], report_text, re.IGNORECASE)
        for m in matches:
            val = float(m.group(1))
            unit = m.group(2) if len(m.groups()) >= 2 and m.group(2) else info["default_unit"]
            low, high = info["normal_range"]
            status = "Low" if val < low else ("Elevated" if val > high else "Normal")
            results.append({"key": key, "name": info["name"], "value": val, "unit": unit, "status": status})
    return results"""

    code_text_2 = """@app.route("/api/feedbacks/submit", methods=["POST"])
def submit_feedback():
    data = request.get_json() or {}
    text = data.get("feedback_text", "").strip()
    nlp_result = nlp.classifier_instance.predict(text)
    db_record = {
        "feedback_id": f"WFQ{int(time.time() * 1000)}",
        "patient_name": data.get("patient_name", "Anonymous"),
        "hospital_name": data.get("hospital_name", "Rohini Super Speciality"),
        "feedback_text": text,
        "sentiment": nlp_result["sentiment"],
        "confidence": nlp_result["confidence"],
        "primary_issue": nlp_result["primary_issue"],
        "urgency_level": nlp_result["urgency_level"],
        "sqi_score": nlp_result["estimated_sqi"],
        "status": "Under Review" if nlp_result["urgency_level"] == "High" else "Pending"
    }
    saved = db.save_feedback(db_record)
    return jsonify({"success": True, "data": saved}), 201"""

    code_card_1 = Table([[Paragraph("<b>Biomarker NER & Boundary Verification</b>", card_title_style)], [Preformatted(code_text_1, code_style)]], colWidths=[420])
    code_card_1.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")), ('BOX', (0,0), (-1,-1), 1, HexColor("#cbd5e1")), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6), ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8)]))

    code_card_2 = Table([[Paragraph("<b>Flask REST Feedback Route & SQLite Persistence</b>", ParagraphStyle('CT2', parent=card_title_style, textColor=HexColor("#10b981")))], [Preformatted(code_text_2, code_style)]], colWidths=[420])
    code_card_2.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")), ('BOX', (0,0), (-1,-1), 1, HexColor("#cbd5e1")), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6), ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8)]))

    story.append(Table([[code_card_1, code_card_2]], colWidths=[440, 440]))
    slide_footer(12)

    # SLIDE 13: UI / DEMO
    slide_header("Project Demonstration", "MediSense NLP Responsive Web Application Interface", "Intuitive Healthcare Dashboard Supporting Server Mode and 1-Click Desktop Execution")
    ui_img = os.path.join(ASSETS_DIR, "Web_Portal_Interface.png")
    c_ui_desc = make_card_table("Live Portal Capabilities", [
        ("Clinical Presets:", "1-Click presets for doctor praise, billing opacity, nursing, emergency delay."),
        ("NLP Inference Preview:", "Visualizes sentiment badges, confidence progress gauges, and issue tags."),
        ("Live Database Feed:", "Displays persistent SQLite records with status toggles ('Pending' -> 'Resolved')."),
        ("Report Simplifier:", "Side-by-side layperson English and colloquial Telugu explanations."),
        ("HTML5 Voice Audio Player:", "Embedded player streams synthesized Telugu speech (`.mp3`) directly."),
        ("OPD Appointment Booking:", "Allows outpatients to book doctor consultations with symptoms recorded.")
    ], 400, 280, "#0284c7")
    if os.path.exists(ui_img):
        story.append(Table([[Image(ui_img, width=450, height=280), c_ui_desc]], colWidths=[460, 410]))
    else:
        story.append(c_ui_desc)
    slide_footer(13)

    # SLIDE 14: RESULTS
    slide_header("Empirical Evaluation", "Empirical Model Benchmarks & Quantitative Results", "Rigorous Evaluation on 20,000 Holdout Test Samples and 100,000 Warangal Dataset Records")
    cm_img = os.path.join(ASSETS_DIR, "Confusion_Matrix.png")
    c_res_desc = make_card_table("Empirical Performance Summary", [
        ("Sentiment Accuracy:", "93.8% Overall Accuracy across 20,000 holdout test samples (Macro F1: 0.94)."),
        ("Grievance Issue Accuracy:", "88.9% Accuracy classifying Waiting Time, Billing, and Staff Conduct."),
        ("Biomarker Hallucination Rate:", "0.00% Error Rate across 2,150 tested clinical numerical values and units."),
        ("Readability Improvement:", "Flesch-Kincaid Grade Level dropped from Grade 14.8 to Grade 7.2 (51.7% reduction)."),
        ("Inference Latency:", "12.4 ms for NLP feedback classification; 88.6 ms for report deconstruction."),
        ("Physician Time-Savings:", "44.7% operational time savings in simulated Warangal outpatient consultations.")
    ], 450, 280, "#10b981")
    if os.path.exists(cm_img):
        story.append(Table([[Image(cm_img, width=380, height=280), c_res_desc]], colWidths=[400, 470]))
    else:
        story.append(c_res_desc)
    slide_footer(14)

    # SLIDE 15: TESTING
    slide_header("Quality Assurance", "Comprehensive Software Testing & Verification Evidence", "Multi-Level Verification Spanning Unit, Integration, Functional, and Performance Tests")
    qa1 = make_card_table("Unit Testing (PyTest / Unittest)", [
        ("Text Preprocessing Unit:", "Verified punctuation removal, lowercase conversion, and negation preservation."),
        ("Biomarker Parser Unit:", "Verified regex boundary matching on integers, decimals, and blood units."),
        ("Readability Metric Unit:", "Verified Flesch-Kincaid scoring against boundary edge cases and zero-division."),
        ("Result:", "100% Pass across all isolated algorithmic units.")
    ], 280, 280, "#0284c7")
    qa2 = make_card_table("Systematic Test Cases (TC-01 - TC-20)", [
        ("TC-01 - TC-03:", "Text sanitization, stopword exclusion, suffix lemmatization -> PASS."),
        ("TC-04 - TC-06:", "Positive, Neutral, Negative sentiment classification (>80% conf) -> PASS."),
        ("TC-07 - TC-08:", "Grievance taxonomy (Waiting time & Billing transparency) -> PASS."),
        ("TC-09 - TC-11:", "Biomarker extraction across lipid, sugar, and CBC -> PASS."),
        ("TC-12 - TC-14:", "Readability reduction, Telugu NLG, and gTTS MP3 generation -> PASS."),
        ("TC-15 - TC-18:", "SQLite insert, EHR archive, status PATCH, and CORS -> PASS."),
        ("TC-19 - TC-20:", "Direct desktop `file://` execution and OPD booking -> PASS.")
    ], 280, 280, "#10b981")
    qa3 = make_card_table("System & Performance Testing", [
        ("Inference Latency:", "NLP inference executes in 12.4 ms per review; report simplification completes in 88.6 ms."),
        ("Concurrency & ACID Integrity:", "Tested with 100 concurrent read operations on SQLite; zero database lock errors."),
        ("Cross-Protocol Resilience:", "Validated on HTTP localhost and direct Windows File Explorer execution."),
        ("Overall QA Status:", "20 out of 20 test cases achieved 100% PASS rate.")
    ], 280, 280, "#7c3aed")
    story.append(Table([[qa1, qa2, qa3]], colWidths=[290, 290, 290]))
    slide_footer(15)

    # SLIDE 16: ADVANTAGES & IMPACT
    slide_header("Practical Utility", "Clinical Advantages & Societal Healthcare Impact", "Measurable Operational Improvements for Patients, Clinicians, and Hospital Administrators")
    hosp_img = os.path.join(ASSETS_DIR, "Hospital_Benchmark.png")
    c_adv_desc = make_card_table("Tripartite Healthcare Benefits", [
        ("1. Patient Empowerment & Dravidian Equity:", "Enables rural, elderly, and non-literate patients in Telangana to comprehend blood test results and diagnostic urgency through native Telugu speech."),
        ("2. 44.7% Physician Consultation Time-Savings:", "Reduces explanation overhead from 170 seconds down to 94 seconds per outpatient encounter, relieving severe clinician burnout in crowded OPDs."),
        ("3. Data-Driven Administrative Quality:", "Provides hospital management with quantifiable Service Quality Index (SQI) benchmarks across 12 hospitals (Rohini: 84.2, Medwin: 81.0, MGM: 62.5)."),
        ("4. Direct Accountability & Action Tracking:", "Automatically flags severe delays and billing grievances, tracking ticket resolution from 'Pending' to 'Resolved' in persistent SQLite storage.")
    ], 430, 280, "#0284c7")
    if os.path.exists(hosp_img):
        story.append(Table([[Image(hosp_img, width=420, height=280), c_adv_desc]], colWidths=[430, 440]))
    else:
        story.append(c_adv_desc)
    slide_footer(16)

    # SLIDE 17: CONCLUSION & FUTURE WORK
    slide_header("Project Roadmap", "Project Conclusion & Future Engineering Roadmap", "Summary of Delivered Contributions and Strategic Expansion Directions")
    concl = make_card_table("Delivered Achievements", [
        ("Engineered Dual-Engine NLP Platform:", "Concurrently solves patient report comprehension and administrative feedback analysis."),
        ("Trained on 100,000 Warangal Reviews:", "Achieved 93.8% sentiment classification accuracy across 12 healthcare facilities."),
        ("Zero Numerical Hallucination Guarantee:", "Deterministic regex guardrail preserves 100% biomarker values across reference intervals."),
        ("Dravidian Telugu Voice Synthesis:", "Integrated gTTS audio generation for rural and illiterate patient accessibility."),
        ("Production-Grade Full-Stack System:", "Flask 3.0 REST API, persistent SQLite database (`medisense.db`), and responsive dashboard."),
        ("Academic Documentation & Paper:", "Complete IEEE research paper and university-level project documentation.")
    ], 430, 280, "#10b981")
    fut = make_card_table("Future Engineering Enhancements", [
        ("1. Multi-Dravidian Language Expansion:", "Extend the natural language generation and speech synthesis pipeline to include Kannada, Tamil, and Malayalam."),
        ("2. Vision Transformer OCR Integration:", "Incorporate Optical Character Recognition (OCR) to parse photographed handwritten physician prescription notes."),
        ("3. Offline Android App for PHCs:", "Package the engine into an edge Android mobile application using ONNX runtime and offline TTS for rural Primary Health Centers."),
        ("4. Federated Healthcare Learning:", "Enable multi-hospital collaborative model training across district facilities while preserving strict patient data privacy.")
    ], 430, 280, "#7c3aed")
    story.append(Table([[concl, fut]], colWidths=[440, 440]))
    slide_footer(17)

    # SLIDE 18: REFERENCES & THANK YOU
    slide_header("Closing & Acknowledgements", "Academic References & Acknowledgements", "Thank You for Your Time and Consideration — Open for Questions & Evaluation")
    ref_card = make_card_table("Key Academic References (IEEE Format)", [
        ("[1] G. Eysenbach,", "'Medicine 2.0: Social networking and openness,' JMIR, 2008."),
        ("[2] D. Kandula et al.,", "'Creating a gold standard for readability measurement of health texts,' AMIA, 2008."),
        ("[3] S. V. Pakhomov et al.,", "'Automating diagnosis codes using NLP,' JAMIA, 2006."),
        ("[4] R. Collobert et al.,", "'Natural language processing from scratch,' JMLR, 2011."),
        ("[5] F. Pedregosa et al.,", "'Scikit-learn: Machine learning in Python,' JMLR, 2011."),
        ("[6] E. Alsentzer et al.,", "'Publicly available clinical BERT embeddings,' 2019.")
    ], 430, 280, "#0284c7")

    thx_content = [
        Paragraph("<b>THANK YOU!</b>", ParagraphStyle('ThxT', fontName='Helvetica-Bold', fontSize=24, alignment=TA_CENTER, textColor=HexColor("#0f172a"), spaceAfter=8)),
        Paragraph("<i>MediSense NLP Healthcare Intelligence Platform</i>", ParagraphStyle('ThxS', fontName='Helvetica-Oblique', fontSize=11, alignment=TA_CENTER, textColor=HexColor("#0284c7"), spaceAfter=14)),
        Paragraph("Special Thanks to Project Supervisor / Guide:<br/><b>Mr. Rupesh Mishra</b><br/>Assistant Professor, Dept. of Computer Science & Engineering<br/>SR University / Engineering College, Warangal", ParagraphStyle('ThxG', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_CENTER, textColor=HexColor("#334155"), spaceAfter=14)),
        Paragraph("<b>We warmly welcome questions, feedback, and viva voce evaluation.</b>", ParagraphStyle('ThxQ', fontName='Helvetica-Bold', fontSize=10.5, alignment=TA_CENTER, textColor=HexColor("#10b981")))
    ]
    thx_card = Table([[thx_content]], colWidths=[430], rowHeights=[280])
    thx_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1.5, HexColor("#10b981")),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    story.append(Table([[ref_card, thx_card]], colWidths=[440, 440]))
    slide_footer(18)

    doc.build(story)
    file_size = os.path.getsize(PDF_PATH)
    print(f"SUCCESS: Generated {PDF_PATH} ({file_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_pdf()
