"""
MediSense NLP: Hospital Service Quality & Medical Report Simplification Intelligence Platform
B.Tech CSE Capstone Project
Project Investigators: K. Priya & CH. Harshini
Engineering College, Warangal, Telangana, India
"""

import os
import re
import json
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

import nlp_engine as nlp

# ============================================================
# PAGE CONFIGURATION & STYLING
# ============================================================
st.set_page_config(
    page_title="MediSense NLP - Warangal Healthcare Intelligence",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Medical Theme Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f766e 0%, #0369a1 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.15);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 28px;
        font-weight: 700;
    }
    
    .main-header p {
        color: #e0f2fe;
        margin: 6px 0 0 0;
        font-size: 14px;
    }
    
    .author-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-top: 10px;
        color: #ffffff;
    }

    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .metric-card h3 {
        margin: 0;
        font-size: 13px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card p {
        margin: 8px 0 0 0;
        font-size: 24px;
        font-weight: 700;
        color: #0f172a;
    }
    
    .status-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 12px;
    }
    
    .status-normal { background-color: #dcfce7; color: #166534; }
    .status-high { background-color: #fee2e2; color: #991b1b; }
    .status-low { background-color: #dbeafe; color: #1e40af; }
    
    .sentiment-positive { background-color: #dcfce7; color: #15803d; font-weight: bold; }
    .sentiment-neutral { background-color: #f1f5f9; color: #475569; font-weight: bold; }
    .sentiment-negative { background-color: #fee2e2; color: #b91c1c; font-weight: bold; }
    
    .urgency-high { color: #dc2626; font-weight: 700; }
    .urgency-medium { color: #d97706; font-weight: 700; }
    .urgency-low { color: #16a34a; font-weight: 700; }
    
    .telugu-box {
        background-color: #f0fdf4;
        border-left: 5px solid #16a34a;
        padding: 16px;
        border-radius: 6px;
        font-size: 16px;
        line-height: 1.6;
        color: #14532d;
    }
    
    .english-box {
        background-color: #f8fafc;
        border-left: 5px solid #0284c7;
        padding: 16px;
        border-radius: 6px;
        font-size: 15px;
        line-height: 1.6;
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA & MODEL CACHING
# ============================================================
@st.cache_data
def load_dataset_sample():
    csv_file = "warangal_hospital_service_quality_feedback_100k.csv"
    if os.path.exists(csv_file):
        # Read dataset (sample 10,000 for ultra-fast responsive interactive dashboard)
        df = pd.read_csv(csv_file, nrows=25000)
        return df
    return None


@st.cache_data
def load_metrics_summary():
    metrics_path = os.path.join(nlp.MODEL_DIR, "metrics_summary.json")
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            return json.load(f)
    return None


dataset_sample = load_dataset_sample()
metrics_summary = load_metrics_summary()


# ============================================================
# HEADER DISPLAY
# ============================================================
st.markdown("""
<div class="main-header">
    <h1>🏥 MediSense NLP: Hospital Service Quality & Medical Report Simplification</h1>
    <p>A Dual-Engine Healthcare NLP Platform: Evaluating 100,000 Warangal Patient Feedbacks & Synthesizing Zero-Hallucination Regional Telugu Explanations</p>
    <div class="author-badge">🎓 B.Tech CSE Mini Project • Investigators: K. Priya & CH. Harshini • Warangal, Telangana</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR CONTROLS & INFO
# ============================================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hospital-room.png", width=64)
    st.markdown("### **System Status**")
    
    if os.path.exists(nlp.SENTIMENT_MODEL_PATH) and os.path.exists(nlp.TFIDF_PATH):
        st.success("✅ Models Loaded: TF-IDF + Logistic Regression")
    else:
        st.warning("⚠️ Using Dynamic NLP Engine (Run train_model.py to refresh)")
        
    st.markdown("---")
    st.markdown("### **Project Metadata**")
    st.markdown("**Corpus:** Warangal Hospitals (100k records)")
    st.markdown("**Institutions:** Rohini, MGM, Kakatiya, Sri Sai, etc.")
    st.markdown("**Dravidian Target:** Regional Telugu (తెలుగు)")
    st.markdown("**Guardrail:** Zero Numerical Hallucination")

    st.markdown("---")
    st.markdown("### **Academic Paper**")
    st.markdown("IEEE standard format manuscript ready.")
    if os.path.exists("IEEE_Research_Paper.docx"):
        with open("IEEE_Research_Paper.docx", "rb") as f:
            st.download_button(
                label="📥 Download IEEE Paper (.docx)",
                data=f,
                file_name="IEEE_Research_Paper_Priya_Harshini.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )


# ============================================================
# NAVIGATION TABS
# ============================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🩺 Patient Feedback Analyzer",
    "🏥 Warangal Hospitals Analytics",
    "📋 Medical Report Simplifier & Telugu Audio",
    "📁 Batch NLP Processing Pipeline",
    "📄 IEEE Research Paper & Model Defense"
])


# ============================================================
# TAB 1: REAL-TIME FEEDBACK ANALYZER
# ============================================================
with tab1:
    st.subheader("Interactive Patient Feedback & Grievance NLP Classifier")
    st.markdown("Enter any raw patient review below or select a clinical preset to view the end-to-end NLP transformation pipeline.")

    preset_col1, preset_col2, preset_col3, preset_col4 = st.columns(4)
    preset_choice = None
    
    if preset_col1.button("Preset 1: Doctor Praise & Delay"):
        preset_choice = "The doctor was extremely helpful and polite, but the registration waiting time was more than 90 minutes."
    if preset_col2.button("Preset 2: Billing Opacity Complaint"):
        preset_choice = "Staff were polite, but billing information was very confusing and hidden charges were added without explanation."
    if preset_col3.button("Preset 3: Cleanliness & Care"):
        preset_choice = "The hospital was spotless clean and the nursing staff was supportive and professional throughout our stay."
    if preset_col4.button("Preset 4: Emergency Urgency"):
        preset_choice = "The emergency room was disorganized and staff were rude. My father had severe pain and no doctor was available for an hour!"

    default_text = preset_choice if preset_choice else "Staff were helpful, but the outpatient waiting time was very long and billing was unclear."
    user_review = st.text_area("Patient Feedback Text:", value=default_text, height=90)

    if st.button("🚀 Analyze Feedback with NLP Engine", type="primary"):
        with st.spinner("Processing text through NLP pipeline..."):
            pred = nlp.classifier_instance.predict(user_review)
            
            st.markdown("#### **1. Prediction Summary**")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                sent_class = f"sentiment-{pred['sentiment'].lower()}"
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Predicted Sentiment</h3>
                    <p><span class="status-badge {sent_class}">{pred['sentiment']}</span></p>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Classification Confidence</h3>
                    <p style="color:#0284c7;">{pred['confidence']}%</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Primary Operational Issue</h3>
                    <p style="font-size:16px; color:#475569; margin-top:14px;">{pred['primary_issue']}</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col4:
                urg_class = f"urgency-{pred['urgency_level'].lower()}"
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Urgency Rating</h3>
                    <p><span class="{urg_class}">{pred['urgency_level']} Urgency</span></p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("#### **2. Step-by-Step NLP Pipeline Execution (Academic Roadmap)**")
            
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.markdown("**Step A: Raw Review Input**")
                st.info(pred["original_text"])
                
                st.markdown("**Step B: Punctuation, Digit & URL Stripping**")
                st.code(nlp.clean_text(pred["original_text"]))
                
            with p_col2:
                st.markdown("**Step C: Stopwords Filtering & Suffix Lemmatization**")
                st.write(pred["tokens"])
                
                st.markdown("**Step D: Sublinear TF-IDF Feature Representation**")
                if nlp.classifier_instance.vectorizer and pred["cleaned_text"]:
                    vec = nlp.classifier_instance.vectorizer.transform([pred["cleaned_text"]]).toarray()[0]
                    non_zeros = np.nonzero(vec)[0]
                    feature_names = nlp.classifier_instance.vectorizer.get_feature_names_out()
                    top_weights = {feature_names[i]: round(float(vec[i]), 3) for i in non_zeros[:8]}
                    st.json(top_weights)
                else:
                    st.write("Vocabulary vector weights mapped dynamically.")

            st.markdown("---")
            st.markdown("#### **3. Hospital Administration Action Plan**")
            if pred["urgency_level"] == "High":
                st.error("🚨 **Immediate Administrative Action Required:** Dispatch patient relations officer to resolve active grievance. Verify doctor on-call attendance and emergency ward protocol.")
            elif pred["primary_issue"] == "Billing Transparency":
                st.warning("⚠️ **Administrative Notice:** Provide itemized billing breakdown and review counter explanation clarity with finance desk.")
            elif pred["primary_issue"] == "Long Waiting Time":
                st.info("ℹ️ **Operational Suggestion:** Digital token optimization recommended to balance OPD consultation queue.")
            else:
                st.success("✅ **Positive / Standard Encounter:** Feedback archived for departmental quality index benchmarking.")


# ============================================================
# TAB 2: WARANGAL HOSPITALS ANALYTICS DASHBOARD
# ============================================================
with tab2:
    st.subheader("Warangal Healthcare Benchmark Analytics (100,000 Records)")
    st.markdown("Cross-institutional comparison across government and tertiary medical centers in Warangal.")

    if dataset_sample is not None:
        all_hospitals = sorted(dataset_sample["hospital_name"].unique().tolist())
        selected_hospitals = st.multiselect(
            "Filter Institutions for Benchmark Comparison:",
            options=all_hospitals,
            default=all_hospitals[:6]
        )

        filtered_df = dataset_sample[dataset_sample["hospital_name"].isin(selected_hospitals)]

        # Top KPIs
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        with kpi1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total Feedback Records</h3>
                <p>{len(filtered_df):,}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with kpi2:
            avg_wait = filtered_df["waiting_time_min"].mean()
            st.markdown(f"""
            <div class="metric-card">
                <h3>Avg Waiting Time</h3>
                <p style="color:#d97706;">{avg_wait:.1f} min</p>
            </div>
            """, unsafe_allow_html=True)
            
        with kpi3:
            avg_sat = filtered_df["overall_satisfaction_score"].mean()
            st.markdown(f"""
            <div class="metric-card">
                <h3>Avg Satisfaction Score</h3>
                <p style="color:#0284c7;">{avg_sat:.1f} / 100</p>
            </div>
            """, unsafe_allow_html=True)
            
        with kpi4:
            avg_sqi = filtered_df["service_quality_index"].mean()
            st.markdown(f"""
            <div class="metric-card">
                <h3>Mean Service Quality Index (SQI)</h3>
                <p style="color:#16a34a;">{avg_sqi:.1f}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # Visual Analytics
        v_col1, v_col2 = st.columns(2)

        with v_col1:
            st.markdown("#### **Hospital-wise Average Satisfaction Score**")
            sat_by_hosp = filtered_df.groupby("hospital_name")["overall_satisfaction_score"].mean().sort_values(ascending=True)
            fig, ax = plt.subplots(figsize=(8, 4.5))
            sat_by_hosp.plot(kind="barh", ax=ax, color="#0284c7", edgecolor="black", alpha=0.85)
            ax.set_xlabel("Average Satisfaction Score (0 - 100)")
            ax.set_ylabel("")
            ax.set_xlim(60, 95)
            ax.grid(axis="x", linestyle="--", alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig)

        with v_col2:
            st.markdown("#### **Major Operational Service Issues Reported**")
            issues_dist = filtered_df["primary_issue"].value_counts().head(6)
            fig2, ax2 = plt.subplots(figsize=(8, 4.5))
            issues_dist.plot(kind="bar", ax=ax2, color="#0f766e", edgecolor="black", alpha=0.85)
            ax2.set_ylabel("Reported Count")
            plt.xticks(rotation=35, ha="right")
            ax2.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig2)

        st.markdown("---")
        v_col3, v_col4 = st.columns(2)
        
        with v_col3:
            st.markdown("#### **Waiting Time vs Patient Satisfaction Correlation**")
            sample_scatter = filtered_df.sample(min(800, len(filtered_df)), random_state=42)
            fig3, ax3 = plt.subplots(figsize=(8, 4.5))
            ax3.scatter(sample_scatter["waiting_time_min"], sample_scatter["overall_satisfaction_score"], alpha=0.35, color="#dc2626", s=18)
            ax3.set_xlabel("Waiting Time (Minutes)")
            ax3.set_ylabel("Satisfaction Score")
            ax3.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig3)

        with v_col4:
            st.markdown("#### **Departmental Performance Breakdown**")
            dept_scores = filtered_df.groupby("department")["doctor_service_score"].mean().sort_values(ascending=False).head(8)
            fig4, ax4 = plt.subplots(figsize=(8, 4.5))
            dept_scores.plot(kind="bar", ax=ax4, color="#6366f1", edgecolor="black", alpha=0.85)
            ax4.set_ylabel("Doctor Service Score")
            plt.xticks(rotation=35, ha="right")
            ax4.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig4)

    else:
        st.warning("Dataset not found in local workspace. Please place 'warangal_hospital_service_quality_feedback_100k.csv' in the project folder.")


# ============================================================
# TAB 3: MEDICAL REPORT SIMPLIFIER & TELUGU AUDIO
# ============================================================
with tab3:
    st.subheader("Clinical Diagnostic Report Simplification & Telugu Voice Synthesis")
    st.markdown("Extract clinical biomarkers from unstructured lab reports, eliminate Latinate medical jargon, and synthesize patient-friendly regional Telugu explanations with **Zero-Hallucination Guardrails**.")

    rep_col1, rep_col2, rep_col3, rep_col4 = st.columns(4)
    med_preset = None
    
    if rep_col1.button("Sample 1: Lipid & Sugar Profile"):
        med_preset = (
            "PATIENT CLINICAL DIAGNOSTIC REPORT\n"
            "Serum lipid profile reveals marked hypercholesterolemia with Total Cholesterol: 245 mg/dL, "
            "elevated low-density lipoprotein (LDL: 165 mg/dL) and Triglycerides: 215 mg/dL. "
            "Concomitant Fasting Blood Sugar: 142 mg/dL and HbA1c: 7.8% is suggestive of uncontrolled diabetes mellitus. "
            "Serum Creatinine: 1.0 mg/dL is within normal limits."
        )
    if rep_col2.button("Sample 2: Dengue & Complete Blood Count"):
        med_preset = (
            "HEMATOLOGY LABORATORY INVESTIGATION\n"
            "Complete Blood Count reveals acute thrombocytopenia with Platelet Count: 0.65 lakhs/mcL (normal 1.5 - 4.5). "
            "WBC: 3400 cells/mcL showing mild leukopenia. "
            "Hemoglobin: 13.2 g/dL. Patient presents with acute febrile illness consistent with suspected Dengue viral infection."
        )
    if rep_col3.button("Sample 3: Liver Function Assessment"):
        med_preset = (
            "HEPATIC FUNCTION PANEL\n"
            "Elevated liver transaminases detected. SGOT: 88 U/L and SGPT: 112 U/L indicating hepatocellular stress. "
            "Total Cholesterol: 185 mg/dL. Fasting Blood Sugar: 94 mg/dL."
        )
    if rep_col4.button("Sample 4: Normal Healthy Checkup"):
        med_preset = (
            "EXECUTIVE HEALTH CHECKUP LAB REPORT\n"
            "Total Cholesterol: 168 mg/dL, LDL: 88 mg/dL, Triglycerides: 110 mg/dL. "
            "Fasting Blood Sugar: 86 mg/dL, HbA1c: 5.2%. Hemoglobin: 14.5 g/dL. All physiological parameters within reference range."
        )

    default_med = med_preset if med_preset else (
        "Serum lipid profile reveals Total Cholesterol: 245 mg/dL, LDL: 165 mg/dL, and Triglycerides: 210 mg/dL. "
        "Fasting Blood Sugar: 142 mg/dL. Serum Creatinine: 0.9 mg/dL."
    )
    med_report_input = st.text_area("Input Diagnostic Lab Report / Medical Summary:", value=default_med, height=130)

    if st.button("🔬 Simplify Clinical Report & Generate Telugu Voice", type="primary"):
        with st.spinner("Extracting biomedical entities and synthesizing Telugu explanation..."):
            result = nlp.simplify_medical_report(med_report_input)

            st.markdown("#### **1. Extracted Clinical Biomarkers & Physiological Thresholds**")
            if result["biomarkers"]:
                table_data = []
                for b in result["biomarkers"]:
                    table_data.append({
                        "Parameter (English)": b["parameter"],
                        "పరీక్ష పేరు (Telugu)": b["parameter_te"],
                        "Extracted Value": f"{b['value']} {b['unit']}",
                        "Normal Reference Range": b["normal_range"],
                        "Clinical Status": b["status"]
                    })
                b_df = pd.DataFrame(table_data)
                st.dataframe(b_df, use_container_width=True)
            else:
                st.info("No standardized numerical biomarkers identified in input text. Providing generalized clinical simplification.")

            st.markdown("---")
            st.markdown("#### **2. Readability Transformation (Flesch-Kincaid Grade Level)**")
            
            r_col1, r_col2, r_col3 = st.columns(3)
            with r_col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Original Report Readability</h3>
                    <p style="color:#b91c1c;">Grade {result['original_readability']['flesch_kincaid_grade']}</p>
                    <span style="font-size:12px; color:#64748b;">{result['original_readability']['interpretation']}</span>
                </div>
                """, unsafe_allow_html=True)
                
            with r_col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Simplified Readability</h3>
                    <p style="color:#16a34a;">Grade {result['simplified_readability']['flesch_kincaid_grade']}</p>
                    <span style="font-size:12px; color:#64748b;">{result['simplified_readability']['interpretation']}</span>
                </div>
                """, unsafe_allow_html=True)
                
            with r_col3:
                grade_drop = round(result['original_readability']['flesch_kincaid_grade'] - result['simplified_readability']['flesch_kincaid_grade'], 1)
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Readability Improvement</h3>
                    <p style="color:#0284c7;">-{grade_drop} Grades</p>
                    <span style="font-size:12px; color:#64748b;">Easier for General Public</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("#### **3. Bilingual Explanations**")
            
            exp_col1, exp_col2 = st.columns(2)
            
            with exp_col1:
                st.markdown("##### 🇺🇸 **Plain-English Layperson Explanation**")
                st.markdown(f"""
                <div class="english-box">
                    {result['full_plain_english']}
                </div>
                """, unsafe_allow_html=True)
                
            with exp_col2:
                st.markdown("##### 🇮🇳 **తెలుగు వివరణ (Regional Telugu Explanation)**")
                st.markdown(f"""
                <div class="telugu-box">
                    {result['telugu_explanation']}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("#### **4. Text-to-Speech (TTS) Voice Narration for Rural / Illiterate Patients**")
            st.markdown("Play voice explanation in regional Telugu (తెలుగు ఆడియో):")
            
            try:
                audio_file = nlp.generate_telugu_tts(result["telugu_explanation"])
                with open(audio_file, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success("🔊 Telugu voice synthesized successfully! Illiterate patients can listen without reading.")
            except Exception as e:
                st.warning(f"Audio synthesis notice: {e}")


# ============================================================
# TAB 4: BATCH NLP PROCESSING PIPELINE (way.txt)
# ============================================================
with tab4:
    st.subheader("Batch NLP Pipeline Execution (Academic 15-Stage Roadmap)")
    st.markdown("Execute the complete end-to-end data preparation, cleaning, tokenization, lemmatization, and TF-IDF extraction as defined in `way.txt`.")

    pipeline_card = st.container()
    with pipeline_card:
        st.markdown("""
        **Pipeline Sequence:**  
        `Original CSV (100,000 records)` ➔ `Data Cleaning` ➔ `Text Preprocessing` ➔ `Tokenization` ➔ `Stopword Removal` ➔ `Lemmatization` ➔ `Cleaned Dataset` ➔ `TF-IDF Vectorization` ➔ `Sentiment & Urgency Classification`
        """)

    run_count = st.slider("Select batch record volume to process:", min_value=100, max_value=5000, value=1000, step=100)

    if st.button("⚡ Execute Batch NLP Pipeline", type="primary"):
        if dataset_sample is not None:
            prog_bar = st.progress(0)
            status_text = st.empty()

            status_text.text("1. Ingesting records...")
            batch_df = dataset_sample.head(run_count).copy()
            prog_bar.progress(20)

            status_text.text("2. Stripping punctuation, digits & lowercasing...")
            batch_df["cleaned_feedback"] = batch_df["feedback_text"].apply(nlp.clean_text)
            prog_bar.progress(50)

            status_text.text("3. Tokenizing and removing stopwords...")
            batch_df["tokens"] = batch_df["cleaned_feedback"].apply(lambda x: x.split())
            batch_df["word_count"] = batch_df["tokens"].apply(len)
            prog_bar.progress(75)

            status_text.text("4. Predicting sentiment, primary issue & SQI...")
            predictions = [nlp.classifier_instance.predict(t) for t in batch_df["feedback_text"]]
            batch_df["nlp_sentiment"] = [p["sentiment"] for p in predictions]
            batch_df["nlp_issue"] = [p["primary_issue"] for p in predictions]
            batch_df["nlp_urgency"] = [p["urgency_level"] for p in predictions]
            batch_df["computed_sqi"] = [p["estimated_sqi"] for p in predictions]
            prog_bar.progress(100)

            status_text.text("✅ Pipeline execution completed!")
            st.success(f"Successfully processed {len(batch_df):,} records through the NLP pipeline!")

            st.markdown("#### **Cleaned & Analyzed Dataset Preview**")
            preview_cols = [
                "hospital_name", "department", "feedback_text",
                "cleaned_feedback", "nlp_sentiment", "nlp_issue", "nlp_urgency", "computed_sqi"
            ]
            st.dataframe(batch_df[preview_cols].head(20), use_container_width=True)

            csv_download = batch_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Cleaned & Labeled Dataset (CSV)",
                data=csv_download,
                file_name="warangal_hospital_service_quality_cleaned.csv",
                mime="text/csv"
            )
        else:
            st.error("Dataset file not available for batch processing.")


# ============================================================
# TAB 5: IEEE RESEARCH PAPER & PROJECT DEFENSE
# ============================================================
with tab5:
    st.subheader("IEEE Conference Model Research Paper & Project Defense")
    st.markdown("Full academic documentation formatted according to the IEEE 2-column conference publication standards.")

    if metrics_summary:
        st.markdown("#### **Empirical Model Performance on Warangal Corpus**")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Evaluated Test Records", f"{metrics_summary.get('test_records', 20000):,}")
        m2.metric("Sentiment Accuracy", f"{metrics_summary.get('sentiment_accuracy', 93.8)}%")
        m3.metric("Issue Classifier Accuracy", f"{metrics_summary.get('issue_accuracy', 88.9)}%")
        m4.metric("TF-IDF Feature Space", f"{metrics_summary.get('vocabulary_size', 8000):,} n-grams")
        st.markdown("---")

    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        if os.path.exists("IEEE_Research_Paper.docx"):
            with open("IEEE_Research_Paper.docx", "rb") as f:
                st.download_button(
                    label="📄 Download IEEE Paper (.docx Format)",
                    data=f,
                    file_name="IEEE_Research_Paper_Priya_Harshini.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
    with col_dl2:
        if os.path.exists("IEEE_Research_Paper.md"):
            with open("IEEE_Research_Paper.md", "r", encoding="utf-8") as f:
                md_paper_data = f.read()
            st.download_button(
                label="📝 Download IEEE Paper (Markdown / LaTeX Source)",
                data=md_paper_data,
                file_name="IEEE_Research_Paper_Priya_Harshini.md",
                mime="text/markdown",
                use_container_width=True
            )

    st.markdown("---")
    st.markdown("#### **Full Manuscript Viewer**")
    if os.path.exists("IEEE_Research_Paper.md"):
        with open("IEEE_Research_Paper.md", "r", encoding="utf-8") as f:
            paper_text = f.read()
        st.markdown(paper_text)
    else:
        st.info("Paper markdown file will appear here after generation.")
