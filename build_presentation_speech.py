"""
NLP-Based Hospital Service Quality Analysis in Warangal
Slide-by-Slide Student Presentation Speaking Script.
Outputs: Project_Presentation/Presentation_Speech.docx
Department of Computer Science & Engineering.
Authors: KATAKAM PRIYA (2303A51194) & CH. HARSHINI (2303A51185)
Guide: Mr. Rupesh Mishra, Assistant Professor, Dept. of CSE
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_DIR = "Project_Presentation"
SPEECH_DOCX_PATH = os.path.join(OUTPUT_DIR, "Presentation_Speech.docx")

def build_speech_doc():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)
        s.page_width = Inches(8.27); s.page_height = Inches(11.69)
        
        hp = s.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("NLP-Based Hospital Service Quality Analysis in Warangal — Presentation Speaking Script")
        hrun.font.name = "Times New Roman"; hrun.font.size = Pt(8.5); hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(100, 116, 139)

        fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Department of Computer Science & Engineering | Presentation Speaking Script")
        frun.font.name = "Times New Roman"; frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)

    p_t = doc.add_paragraph(); p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_t.add_run("NLP-Based Hospital Service Quality Analysis in Warangal\n")
    r_t.font.name = "Times New Roman"; r_t.font.size = Pt(16); r_t.font.bold = True; r_t.font.color.rgb = RGBColor(2, 132, 199)
    r_st = p_t.add_run("Slide-by-Slide Student Presentation Speaking Script (30 - 60 Seconds per Slide)\n")
    r_st.font.name = "Times New Roman"; r_st.font.size = Pt(11.5); r_st.font.italic = True; r_st.font.color.rgb = RGBColor(71, 85, 105)
    r_auth = p_t.add_run("Presenters: KATAKAM PRIYA (2303A51194) & CH. HARSHINI (2303A51185)\nProject Supervisor: Mr. Rupesh Mishra, Assistant Professor, Dept. of CSE\nAcademic Year: 2026 - 2027 | Warangal, Telangana\n")
    r_auth.font.name = "Times New Roman"; r_auth.font.size = Pt(10.5); r_auth.font.color.rgb = RGBColor(30, 41, 59)

    p_rule = doc.add_paragraph(); p_rule.paragraph_format.space_after = Pt(14)
    r_line = p_rule.add_run("—" * 60); r_line.font.color.rgb = RGBColor(203, 213, 225)

    slides_speech = [
        ("SLIDE 1: TITLE SLIDE (Cover & Team Introduction)",
         "Estimated Speaking Time: 35 seconds",
         "Respected evaluators, faculty members, and project guide Mr. Rupesh Mishra sir, a very warm good morning. "
         "I am Katakam Priya, and along with my project partner Ch. Harshini, we are proud to present our final-year capstone project entitled: "
         "'NLP-Based Hospital Service Quality Analysis in Warangal'. "
         "This is an end-to-end healthcare Natural Language Processing framework and full-stack web application developed to analyze patient reviews, "
         "classify sentiments, extract critical operational issues, and objectively benchmark hospital service standards across Warangal. "
         "Today, we will walk you through our problem statement, methodology, architecture, live software demonstration, and our empirical findings."),

        ("SLIDE 2: PROJECT ABSTRACT & OVERVIEW",
         "Estimated Speaking Time: 50 seconds",
         "Moving to Slide 2, let us read our core project abstract: "
         "'NLP-Based Hospital Service Quality Analysis in Warangal is a Natural Language Processing-based project that analyzes patient reviews and feedback "
         "to evaluate the quality of hospital services. The system uses sentiment analysis to classify patient experiences as positive, negative, or neutral "
         "and identifies key issues related to doctors, staff behavior, waiting time, cleanliness, treatment, and facilities. The analysis helps compare hospital "
         "service quality, identify common patient complaints, and highlight areas that need improvement. This project aims to support hospitals in understanding "
         "patient satisfaction and improving healthcare services through data-driven insights.' "
         "Our framework evaluates 100,000 patient feedback reviews across 12 prominent Warangal hospitals, achieving 93.8% sentiment classification accuracy."),

        ("SLIDE 3: PROBLEM STATEMENT",
         "Estimated Speaking Time: 45 seconds",
         "On Slide 3, we define the critical problems we address. In healthcare, feedback is overwhelmingly collected through unstructured comments, "
         "paper suggestion boxes, or generic web star ratings. Physical suggestion boxes suffer from an extremely low response rate of under 3%, "
         "and manual clerical collation takes weeks or months—meaning urgent grievances like poor sanitation or critical emergency delays go completely unnoticed. "
         "Furthermore, a generic 2-star rating on Google Maps doesn't tell a hospital superintendent whether the failure occurred due to doctor consultation, "
         "rude nursing conduct, or billing confusion. There is an urgent need for an automated NLP pipeline that performs granular aspect extraction."),

        ("SLIDE 4: RESEARCH MOTIVATION",
         "Estimated Speaking Time: 45 seconds",
         "Slide 4 highlights why this project is so essential. Warangal is the second-largest medical hub in Telangana, serving over 6 northern districts "
         "with massive daily outpatient traffic exceeding 10,000 visits across government hospitals like MGM and private tertiary centers like Rohini and MaxCare. "
         "Patient satisfaction is directly tied to therapeutic compliance, recovery rates, and institutional trust. "
         "By converting thousands of unstructured text reviews into an objective, data-driven Service Quality Index (SQI), we give medical directors "
         "the exact evidence they need to eliminate operational bottlenecks and allocate healthcare resources effectively."),

        ("SLIDE 5: SYSTEM OBJECTIVES",
         "Estimated Speaking Time: 40 seconds",
         "Slide 5 outlines our five primary technical objectives: "
         "1. Ingest and preprocess a large-scale corpus of 100,000 patient feedback records across 12 Warangal healthcare facilities. "
         "2. Train a supervised 3-class NLP sentiment classifier to categorize patient experiences into Positive, Neutral, or Negative with over 90% accuracy. "
         "3. Implement multi-aspect grievance extraction covering six core dimensions: Doctors, Staff Behavior, Waiting Time, Cleanliness, Treatment, and Facilities. "
         "4. Formulate a normalized Service Quality Index (SQI 0-100) to benchmark hospitals and profile common complaints. "
         "And 5. Deploy an interactive, responsive web dashboard with persistent SQLite storage for real-time review triage and ticket tracking."),

        ("SLIDE 6: EXISTING SYSTEM & LIMITATIONS",
         "Estimated Speaking Time: 45 seconds",
         "Slide 6 reviews existing approaches and why they fall short. "
         "Traditional suggestion boxes suffer from low volume and delayed manual analysis. "
         "Generic online review platforms like Google Maps or JustDial provide superficial star ratings that lack aspect-level issue categorization "
         "and skew heavily towards extreme anger. "
         "And manual clerical audits are prohibitively expensive, sample under 5% of patient footfalls, and suffer from subjective human bias. "
         "Our proposed NLP system provides continuous, automated, unbiased, and instantaneous feedback analysis."),

        ("SLIDE 7: PROPOSED SYSTEM & KEY INNOVATIONS",
         "Estimated Speaking Time: 50 seconds",
         "Slide 7 presents our proposed architecture. Our solution operates as an automated end-to-end intelligence platform. "
         "Our NLP Engine takes raw patient reviews, executes a 15-stage preprocessing pipeline that preserves crucial medical negations, "
         "extracts sublinear TF-IDF features, and predicts 3-class sentiment with 93.8% accuracy. "
         "Simultaneously, our grievance classifier pins issues to doctors, staff behavior, waiting time, cleanliness, treatment, or facilities. "
         "The system computes an institutional SQI score, compares hospital standards, and logs every ticket into an embedded SQLite database "
         "with live status controls ('Pending' -> 'Under Review' -> 'Resolved')."),

        ("SLIDE 8: SYSTEM ARCHITECTURE",
         "Estimated Speaking Time: 50 seconds",
         "Slide 8 illustrates our Three-Tier Architecture. "
         "Tier 1 is the Presentation Layer: a modern, responsive web dashboard built with HTML5, CSS3, and JavaScript, featuring real-time Chart.js visualizations. "
         "Tier 2 is the Application and NLP Intelligence Layer: a Python Flask 3.0 REST controller managing endpoints that route review text "
         "to our trained Scikit-Learn TF-IDF vectorizer and Logistic Regression models. "
         "Tier 3 is the Data Persistence Layer: an ACID-compliant SQLite 3 database (`medisense.db`) managing relational tables alongside serialized `.joblib` model artifacts. "
         "The application works seamlessly over HTTP and via direct desktop file execution with full CORS support."),

        ("SLIDE 9: TECHNOLOGIES USED",
         "Estimated Speaking Time: 45 seconds",
         "Slide 9 displays our comprehensive technology stack. "
         "For programming, we used Python 3.10 for machine learning and backend logic, and Vanilla ES6+ JavaScript for client interactivity. "
         "For NLP and Machine Learning, we utilized Scikit-Learn, Pandas, NumPy, and Joblib. "
         "For the backend and database, we leveraged Flask 3.0 and SQLite 3. "
         "For visualization, we implemented Chart.js 4 and FontAwesome 6 icons. "
         "All technologies are lightweight, open-source, and engineered for high portability on standard hardware."),

        ("SLIDE 10: METHODOLOGY & WORKFLOW",
         "Estimated Speaking Time: 50 seconds",
         "Slide 10 details our eight-phase execution lifecycle. "
         "We started by curating 100,000 Warangal patient feedback reviews with balanced ground-truth annotations across 12 hospitals. "
         "In Phase 2, we sanitized the text using regex, converted to lowercase, and removed non-clinical stopwords while preserving vital negations like 'no', 'not', and 'unclean'. "
         "In Phase 3, we extracted sublinear TF-IDF representations across 83 domain vocabulary features. "
         "In Phase 4, we trained an L2-regularized Logistic Regression model using an 80:20 stratified split. "
         "In Phases 5 and 6, we mapped the six grievance aspects, formulated the SQI index, integrated Telugu report deconstruction with audio, "
         "and deployed the persistent full-stack dashboard."),

        ("SLIDE 11: MODULE DESCRIPTION",
         "Estimated Speaking Time: 45 seconds",
         "Slide 11 breaks down our four primary software modules: "
         "Module 1 is the Preprocessor and Tokenizer in `nlp_engine.py`, responsible for cleaning, negation protection, and suffix lemmatization. "
         "Module 2 is the 3-Class Sentiment and Grievance Engine in `train_model.py` and `nlp_engine.py`, predicting sentiment valence and issue categories. "
         "Module 3 is the Hospital Quality Benchmarker, calculating composite 0-100 SQI scores and cross-hospital comparative rankings. "
         "And Module 4 is the REST API Controller and Database Manager in `web_server.py` and `database.py`, exposing 10 JSON routes and handling SQLite operations."),

        ("SLIDE 12: IMPLEMENTATION & CODE HIGHLIGHTS",
         "Estimated Speaking Time: 50 seconds",
         "Slide 12 presents two key code listings. "
         "Listing 1 shows our `FeedbackClassifier` class: it loads serialized `.joblib` pipelines, vectorizes clean text, predicts 3-class sentiment, "
         "extracts the primary operational issue, and computes the review's SQI score with sub-15ms execution latency. "
         "Listing 2 shows our Flask POST endpoint `/api/feedbacks/submit`: it receives patient input, triggers NLP inference, "
         "creates a structured record with unique tracking ID, sentiment, and urgency level, and persists it into the SQLite `feedbacks` table."),

        ("SLIDE 13: PROJECT DEMONSTRATION / UI",
         "Estimated Speaking Time: 45 seconds",
         "Slide 13 showcases the user interface of our live web application. "
         "The dashboard includes 1-click clinical review presets covering doctor praise, staff rudeness, OPD delays, and hygiene complaints. "
         "When a review is submitted, the system instantly renders a dynamic sentiment badge (Positive, Neutral, Negative), a confidence progress bar, "
         "and an issue tag. Below, administrators can monitor the live SQLite database feed, filter records by hospital, "
         "and toggle ticket statuses from 'Pending' to 'Resolved'. The portal also includes a clinical report simplifier with Telugu voice audio."),

        ("SLIDE 14: RESULTS & PERFORMANCE BENCHMARKS",
         "Estimated Speaking Time: 50 seconds",
         "Slide 14 presents our quantitative findings. "
         "Evaluated on a rigorous holdout test set of 20,000 Warangal patient reviews, our sentiment model achieved an outstanding 93.8% overall accuracy "
         "with a Macro F1-score of 0.94. "
         "Our multi-aspect grievance classifier attained 88.9% accuracy across the six healthcare categories. "
         "Average inference latency was just 12.4 milliseconds per review on standard CPU hardware. "
         "The confusion matrix confirms minimal misclassifications between positive and negative classes, ensuring highly reliable grievance triage."),

        ("SLIDE 15: HOSPITAL SERVICE QUALITY COMPARISON (WARANGAL)",
         "Estimated Speaking Time: 55 seconds",
         "Slide 15 presents our regional benchmarking findings across Warangal hospitals. "
         "Rohini Super Speciality ranked highest with an SQI of 84.2 and 78% positive reviews, with doctor expertise receiving high praise; its main area for improvement is OPD queue wait time. "
         "MaxCare Hospital scored 82.5, excelling in diagnostic facilities and ward cleanliness, with complaints centered on pharmacy billing transparency. "
         "St. Ann's Hospital scored 79.8, commended for compassionate nursing staff behavior. "
         "MGM Government Hospital scored 62.5: while senior doctors were praised for their diagnostic skill and zero-cost care, it faces severe overcrowding, "
         "with 34% of negative reviews citing long waiting times and 18.2% citing cleanliness issues. "
         "Across Warangal, the top patient complaints were Waiting Time (34%), Staff Behavior (22.5%), and Cleanliness (18.2%)."),

        ("SLIDE 16: TESTING AND VALIDATION",
         "Estimated Speaking Time: 40 seconds",
         "Slide 16 details our software quality assurance. "
         "We conducted comprehensive testing across unit, integration, and performance levels. "
         "Our 20 systematic test cases (TC-01 through TC-20) verified text cleaning, negation handling, 3-class sentiment prediction, "
         "grievance aspect assignment, SQI mathematical boundaries, SQLite CRUD operations, and CORS headers. "
         "All 20 test cases achieved a 100% pass rate. Stress testing with 100 concurrent queries on SQLite exhibited zero database lock contention."),

        ("SLIDE 17: ADVANTAGES, LIMITATIONS & FUTURE ROADMAP",
         "Estimated Speaking Time: 50 seconds",
         "Slide 17 summarizes the practical advantages, current limitations, and future roadmap of our system. "
         "Our key advantage is real-time, automated feedback auditing that pinpoints exact operational bottlenecks and eliminates manual survey delays. "
         "Our current limitation is that the primary NLP model is trained on English review text with regional transliterations. "
         "For future work, we plan to: "
         "1. Extend NLP sentiment classification to native Telugu script and Hindi reviews. "
         "2. Incorporate voice audio input via speech recognition for non-literate outpatients. "
         "3. Add automated SMS and WhatsApp alerts to hospital superintendents when severe grievances occur. "
         "And 4. Integrate directly with Hospital Information Systems (HIS)."),

        ("SLIDE 18: REFERENCES & ACKNOWLEDGEMENTS / THANK YOU",
         "Estimated Speaking Time: 35 seconds",
         "Finally, Slide 18 presents our key academic references following IEEE citation standards. "
         "On behalf of Katakam Priya and Ch. Harshini, we express our profound gratitude to our project guide, Mr. Rupesh Mishra sir, "
         "Assistant Professor in the Department of Computer Science and Engineering, and our department faculty for their invaluable guidance throughout this project. "
         "Thank you very much for your time and kind attention. We now warmly welcome your questions and feedback for our viva voce defense.")
    ]

    for title, est_time, speech_text in slides_speech:
        p_hdr = doc.add_paragraph(); p_hdr.paragraph_format.space_before = Pt(14); p_hdr.paragraph_format.space_after = Pt(2)
        r_hdr = p_hdr.add_run(title)
        r_hdr.font.name = "Times New Roman"; r_hdr.font.size = Pt(13); r_hdr.font.bold = True; r_hdr.font.color.rgb = RGBColor(15, 23, 42)

        p_time = doc.add_paragraph(); p_time.paragraph_format.space_after = Pt(4)
        r_time = p_time.add_run(f"[{est_time}]")
        r_time.font.name = "Times New Roman"; r_time.font.size = Pt(10); r_time.font.italic = True; r_time.font.color.rgb = RGBColor(2, 132, 199)

        p_sp = doc.add_paragraph(); p_sp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_sp.paragraph_format.space_after = Pt(10); p_sp.paragraph_format.line_spacing = 1.3
        r_sp = p_sp.add_run(speech_text)
        r_sp.font.name = "Times New Roman"; r_sp.font.size = Pt(11); r_sp.font.color.rgb = RGBColor(51, 65, 85)

    doc.save(SPEECH_DOCX_PATH)
    file_size = os.path.getsize(SPEECH_DOCX_PATH)
    print(f"SUCCESS: Generated {SPEECH_DOCX_PATH} ({file_size / 1024:.1f} KB)")

if __name__ == '__main__':
    build_speech_doc()
