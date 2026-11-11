"""
MediSense NLP - Master Presentation Generator (18 Widescreen 16:9 Slides).
Produces: Project_Presentation/Project_Presentation.pptx
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

from build_presentation_pptx import (
    SLIDE_WIDTH, SLIDE_HEIGHT, C_NAVY, C_TEAL, C_GREEN, C_AMBER, C_PURPLE,
    C_SLATE, C_BODY, C_BG_CARD, C_BORDER, C_WHITE,
    set_slide_background, add_header, add_footer, add_card, add_metric_pill
)

OUTPUT_DIR = "Project_Presentation"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "Presentation_Assets")
PPTX_PATH = os.path.join(OUTPUT_DIR, "Project_Presentation.pptx")

def build_all_slides():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout); set_slide_background(slide1, C_WHITE)
    top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), SLIDE_WIDTH, Inches(0.18))
    top_bar.fill.solid(); top_bar.fill.fore_color.rgb = C_TEAL; top_bar.line.fill.background()

    accent_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.9), Inches(11.733), Inches(5.7))
    accent_card.fill.solid(); accent_card.fill.fore_color.rgb = C_BG_CARD
    accent_card.line.color.rgb = C_BORDER; accent_card.line.width = Pt(1.5)

    tb1 = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(10.933), Inches(3.0))
    tf1 = tb1.text_frame; tf1.word_wrap = True

    p0 = tf1.paragraphs[0]; r0 = p0.add_run()
    r0.text = "SR UNIVERSITY / ENGINEERING COLLEGE, WARANGAL"
    r0.font.name = "Arial"; r0.font.size = Pt(12); r0.font.bold = True; r0.font.color.rgb = C_TEAL; p0.space_after = Pt(4)

    p_dept = tf1.add_paragraph(); r_d = p_dept.add_run()
    r_d.text = "DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING | B.TECH CAPSTONE MINI-PROJECT"
    r_d.font.name = "Arial"; r_d.font.size = Pt(10); r_d.font.bold = True; r_d.font.color.rgb = C_SLATE; p_dept.space_after = Pt(14)

    p_main = tf1.add_paragraph(); r_m = p_main.add_run()
    r_m.text = "MediSense NLP: Hospital Service Quality & Regional Diagnostic Report Simplification"
    r_m.font.name = "Arial"; r_m.font.size = Pt(25); r_m.font.bold = True; r_m.font.color.rgb = C_NAVY; p_main.space_after = Pt(10)

    p_sub = tf1.add_paragraph(); r_s = p_sub.add_run()
    r_s.text = "A Dual-Engine Healthcare Natural Language Processing Framework & Full-Stack Web Platform"
    r_s.font.name = "Arial"; r_s.font.size = Pt(13); r_s.font.italic = True; r_s.font.color.rgb = C_TEAL

    # Team Box
    card_team = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.3), Inches(5.2), Inches(1.9))
    card_team.fill.solid(); card_team.fill.fore_color.rgb = C_WHITE
    card_team.line.color.rgb = C_BORDER; card_team.line.width = Pt(1)

    tb_t = slide1.shapes.add_textbox(Inches(1.4), Inches(4.45), Inches(4.8), Inches(1.6))
    tf_t = tb_t.text_frame; tf_t.word_wrap = True
    p_th = tf_t.paragraphs[0]; r = p_th.add_run()
    r.text = "PROJECT TEAM MEMBERS:"; r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = C_TEAL; p_th.space_after = Pt(6)
    p_m1 = tf_t.add_paragraph(); r1 = p_m1.add_run()
    r1.text = "1. KATAKAM PRIYA  "; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_NAVY
    r1_sub = p_m1.add_run(); r1_sub.text = "(Roll No: 2303A51194)"; r1_sub.font.italic = True; r1_sub.font.size = Pt(10); r1_sub.font.color.rgb = C_SLATE
    p_m1.space_after = Pt(4)
    p_m2 = tf_t.add_paragraph(); r2 = p_m2.add_run()
    r2.text = "2. CH. HARSHINI     "; r2.font.bold = True; r2.font.size = Pt(11); r2.font.color.rgb = C_NAVY
    r2_sub = p_m2.add_run(); r2_sub.text = "(Roll No: 2303A51185)"; r2_sub.font.italic = True; r2_sub.font.size = Pt(10); r2_sub.font.color.rgb = C_SLATE

    # Guide Box
    card_guide = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.3), Inches(5.333), Inches(1.9))
    card_guide.fill.solid(); card_guide.fill.fore_color.rgb = C_WHITE
    card_guide.line.color.rgb = C_BORDER; card_guide.line.width = Pt(1)

    tb_g = slide1.shapes.add_textbox(Inches(7.0), Inches(4.45), Inches(4.9), Inches(1.6))
    tf_g = tb_g.text_frame; tf_g.word_wrap = True
    p_gh = tf_g.paragraphs[0]; r = p_gh.add_run()
    r.text = "PROJECT SUPERVISOR / GUIDE:"; r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = C_GREEN; p_gh.space_after = Pt(6)
    p_gn = tf_g.add_paragraph(); r = p_gn.add_run()
    r.text = "Mr. Rupesh Mishra"; r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = C_NAVY; p_gn.space_after = Pt(2)
    p_gd = tf_g.add_paragraph(); r = p_gd.add_run()
    r.text = "Assistant Professor, Dept. of Computer Science & Engineering\nAcademic Year: 2026 - 2027 | Warangal, Telangana"
    r.font.size = Pt(9.5); r.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 2: INTRODUCTION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout); set_slide_background(slide2)
    add_header(slide2, "Project Domain & Background", "Transforming Regional Healthcare via Natural Language Processing",
               "Empowering Patients and Administrators in Semi-Urban and Tier-2 Healthcare Ecosystems")
    add_footer(slide2, 2)

    add_card(slide2, Inches(0.8), Inches(1.9), Inches(3.7), Inches(3.6),
             "Healthcare NLP Domain", [
                 ("Natural Language Processing:", "AI discipline structuring human language into computational semantics."),
                 ("Unstructured Healthcare Data:", "Over 80% of clinical data is locked in unstructured lab notes, doctor memos, and reviews."),
                 ("Patient-Centric Paradigm:", "Moving beyond clinician-only tools to empower laypatients with accessible healthcare understanding.")
             ], accent_color=C_TEAL)

    add_card(slide2, Inches(4.8), Inches(1.9), Inches(3.7), Inches(3.6),
             "Warangal Healthcare Hub", [
                 ("Regional Healthcare Core:", "Second largest medical hub in Telangana serving 6 northern districts with high caseloads."),
                 ("12 Major Hospitals:", "Mix of public medical colleges (MGM, KMC) and private tertiary super-specialities (Rohini, Medwin)."),
                 ("Consultation Bottleneck:", "Over 1,500+ daily OPD footfalls per hospital, restricting consultations to under 3 minutes.")
             ], accent_color=C_PURPLE)

    add_card(slide2, Inches(8.8), Inches(1.9), Inches(3.7), Inches(3.6),
             "The Dual Healthcare Friction", [
                 ("Clinical Jargon Barrier:", "Diagnostic reports written in post-graduate English medical terminology cause intense panic."),
                 ("Feedback Audit Deficit:", "Administrations lack automated tools to isolate urgent grievances from high-volume surveys."),
                 ("MediSense Solution:", "Dual-engine framework concurrently addressing both clinical report and feedback bottlenecks.")
             ], accent_color=C_GREEN)

    add_metric_pill(slide2, Inches(0.8), Inches(5.7), Inches(2.7), Inches(1.0), "100,000", "Warangal Reviews Ingested", C_TEAL)
    add_metric_pill(slide2, Inches(3.8), Inches(5.7), Inches(2.7), Inches(1.0), "12 Hospitals", "Evaluated & Benchmarked", C_PURPLE)
    add_metric_pill(slide2, Inches(6.8), Inches(5.7), Inches(2.7), Inches(1.0), "93.8%", "Sentiment Classification Acc.", C_GREEN)
    add_metric_pill(slide2, Inches(9.8), Inches(5.7), Inches(2.7), Inches(1.0), "0.00%", "Biomarker Distortion Guarantee", C_AMBER)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout); set_slide_background(slide3)
    add_header(slide3, "Problem Definition", "Critical Gaps in Healthcare Communication & Quality Auditing",
               "Analyzing the Twin Operational Bottlenecks Confronting Outpatients and Hospital Administrators")
    add_footer(slide3, 3)

    add_card(slide3, Inches(0.8), Inches(1.9), Inches(5.7), Inches(4.8),
             "Problem 1: Diagnostic Lab Report Incomprehensibility", [
                 ("Specialized English Terminology:", "Lab tests contain Latinate pathology terms like 'hypercholesterolemia' and 'thrombocytopenia'."),
                 ("Extreme Readability Demands:", "Original diagnostic reports have a Flesch-Kincaid Grade Level > 14.8 (requires post-graduate education)."),
                 ("Severely Constrained Doctors:", "OPD doctors have < 180 seconds per patient, leaving no time to deconstruct blood panel ranges."),
                 ("Generative AI Hallucination Risk:", "Commercial LLMs alter numeric values (e.g. changing 142 mg/dL to 124 mg/dL), introducing life-threatening clinical hazards."),
                 ("Neglect of Vernacular Dialects:", "Absence of reliable, verified Telugu explanations and voice audio for non-literate patients.")
             ], accent_color=C_TEAL)

    add_card(slide3, Inches(6.8), Inches(1.9), Inches(5.7), Inches(4.8),
             "Problem 2: Unstructured Patient Grievance Overload", [
                 ("High-Volume Unstructured Surveys:", "Hospitals collect tens of thousands of written reviews and web comments without automated triage."),
                 ("Slow & Laborious Manual Audits:", "Clerical staff manually review small survey samples; critical operational failures take weeks to reach directors."),
                 ("Unaddressed Service Bottlenecks:", "Patients experience 90-120 minute registration queues, hidden discharge bills, and unsupportive nursing."),
                 ("Lack of Quantifiable Metrics:", "Administrations lack an objective Service Quality Index (SQI) to benchmark hospital departments."),
                 ("Isolated Systems:", "Clinical report deconstruction and administrative sentiment intelligence have historically operated in complete isolation.")
             ], accent_color=C_AMBER)

    # =========================================================================
    # SLIDE 4: MOTIVATION
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout); set_slide_background(slide4)
    add_header(slide4, "Research Motivation", "Why MediSense NLP? The Imperative for Regional Clinical Equity",
               "Addressing Low-Resource Dravidian Demographics and Hospital Operational Efficiency")
    add_footer(slide4, 4)

    add_card(slide4, Inches(0.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "Pillar 1: Vernacular Equity", [
                 ("Low-Resource Dravidian Need:", "Over 65% of rural families in northern Telangana are non-English literate."),
                 ("Inequity of Medical English:", "Expecting rural citizens to interpret post-graduate English reports creates profound health disparities."),
                 ("Telugu Voice Inclusivity:", "Automated Telugu voice audio allows illiterate, rural, and elderly patients to understand their health autonomously.")
             ], accent_color=C_TEAL)

    add_card(slide4, Inches(4.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "Pillar 2: Clinician Efficiency", [
                 ("Relieving OPD Consultation Load:", "Doctors spend significant consultation time repeatedly explaining standard lab sheets."),
                 ("44.7% Time Savings:", "Pre-consultation simplified reports reduce explanation overhead from 170 seconds down to 94 seconds."),
                 ("Elevated Clinical Care:", "Frees physician cognitive focus for physical diagnosis, clinical history, and therapeutic decision making.")
             ], accent_color=C_GREEN)

    add_card(slide4, Inches(8.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "Pillar 3: Data-Driven Quality", [
                 ("Quantifiable Accountability:", "Transforms vague feedback into a concrete Service Quality Index (SQI) score (0-100)."),
                 ("Targeted Interventions:", "Instantly reveals whether patient dissatisfaction stems from pharmacy delays, rude billing, or hygiene."),
                 ("Persistent Action Tracking:", "Enables hospital directors to track grievances from 'Pending' to 'Under Review' to 'Resolved'.")
             ], accent_color=C_PURPLE)

    # =========================================================================
    # SLIDE 5: OBJECTIVES
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout); set_slide_background(slide5)
    add_header(slide5, "System Goals", "Core Objectives of the MediSense NLP Framework",
               "Dual-Engine Architecture Designed for Deterministic Safety, Real-Time Performance & High Usability")
    add_footer(slide5, 5)

    obj_data = [
        ("Objective 1: Supervised Sentiment Modeling", "Train a regularized TF-IDF NLP model on 100,000 Warangal hospital feedback reviews to classify sentiment (Positive, Neutral, Negative) with >90% accuracy.", C_TEAL),
        ("Objective 2: Operational Grievance Taxonomy", "Categorize complaints across 6 operational categories (Waiting Times, Billing Opacity, Staff Conduct, Cleanliness) and compute an institutional SQI score.", C_PURPLE),
        ("Objective 3: Deterministic Biomarker Guardrail", "Develop an entity-extraction engine covering 13 clinical biomarkers with 0.00% numerical hallucination across physiological reference bounds.", C_GREEN),
        ("Objective 4: Dravidian NLG & Voice Audio Synthesis", "Translate simplified clinical explanations into colloquial Telugu and generate synthetic voice audio streams (MP3) using Google TTS.", C_AMBER),
        ("Objective 5: Full-Stack Persistence & Web Portal", "Engineer a production-ready web application using Python Flask, SQLite database persistence, and a responsive frontend dashboard for admins and patients.", C_TEAL)
    ]

    for idx, (title, desc, col) in enumerate(obj_data):
        y_pos = Inches(1.9 + idx * 0.98)
        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(0.85))
        card.fill.solid(); card.fill.fore_color.rgb = C_BG_CARD
        card.line.color.rgb = col; card.line.width = Pt(1.4)

        tb = slide5.shapes.add_textbox(Inches(1.1), y_pos + Inches(0.12), Inches(11.1), Inches(0.65))
        tf = tb.text_frame; tf.word_wrap = True
        p1 = tf.paragraphs[0]; r1 = p1.add_run()
        r1.text = title; r1.font.bold = True; r1.font.size = Pt(12); r1.font.color.rgb = col
        p2 = tf.add_paragraph(); r2 = p2.add_run()
        r2.text = desc; r2.font.size = Pt(9.5); r2.font.color.rgb = C_BODY

    # =========================================================================
    # SLIDE 6: EXISTING SYSTEM & LIMITATIONS
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout); set_slide_background(slide6)
    add_header(slide6, "Comparative Literature Analysis", "Limitations of Existing Healthcare Solutions",
               "Why Traditional Audits, Generic Translators, and Deep LLMs Fall Short in Clinical Practice")
    add_footer(slide6, 6)

    add_card(slide6, Inches(0.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "1. Manual Grievance Auditing", [
                 ("Sampling Deficit:", "Clerical staff manually review paper forms; samples less than 5% of total feedback."),
                 ("Delayed Intervention:", "Operational bottlenecks take weeks or months to reach hospital directors."),
                 ("High Labor Overhead:", "Requires large administrative teams without generating structured analytics."),
                 ("Subjective Bias:", "Manual reviews lack standardized scoring and cross-hospital benchmarking.")
             ], accent_color=C_AMBER)

    add_card(slide6, Inches(4.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "2. Generic Web Translators", [
                 ("Literal Translation:", "Google Translate performs word-for-word translation without medical ontologies."),
                 ("Clinical Jargon Corruption:", "Corrupts medical terms (e.g. translating 'fasting blood sugar' into religious fasting idioms)."),
                 ("No Reference Bounds:", "Does not evaluate whether a numerical result is normal, low, or critically elevated."),
                 ("Text-Only Interfaces:", "Provides no integrated voice synthesis for rural and illiterate patients.")
             ], accent_color=C_PURPLE)

    add_card(slide6, Inches(8.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "3. Unconstrained Generative AI", [
                 ("Dangerous Hallucination:", "Commercial LLMs exhibit 3% to 8% numerical hallucination rates on clinical text."),
                 ("Numerical Alterations:", "Modifies critical lab values (e.g. changing 142 mg/dL to 124 mg/dL), causing clinical risk."),
                 ("High Latency & Cloud Cost:", "Large models require GPU infrastructure and exhibit multi-second response delays."),
                 ("No Built-in EHR Database:", "Operate as isolated chat prompts without relational persistence or administrative tracking.")
             ], accent_color=C_TEAL)

    # =========================================================================
    # SLIDE 7: PROPOSED SYSTEM & KEY ADVANTAGES
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout); set_slide_background(slide7)
    add_header(slide7, "Proposed Architecture", "The MediSense NLP Framework: Integrated Dual-Engine Platform",
               "Harmonizing Administrative Quality Intelligence with Deterministic Patient Report Simplification")
    add_footer(slide7, 7)

    add_card(slide7, Inches(0.8), Inches(1.9), Inches(5.7), Inches(3.7),
             "ENGINE A: Hospital Service Quality Intelligence", [
                 ("100,000 Warangal Review Ingestion:", "Comprehensive multi-aspect dataset spanning 12 hospitals."),
                 ("15-Stage NLP Pipeline:", "Regex cleaning, custom clinical stopwords, and suffix lemmatization."),
                 ("Sublinear TF-IDF Classification:", "Multinomial Logistic Regression predicting Positive, Neutral, Negative."),
                 ("Grievance Routing & SQI Score:", "Auto-detects primary operational issues and computes 0-100 SQI index."),
                 ("Automated SQLite Persistence:", "Saves records with ticket tracking ('Pending', 'Resolved').")
             ], accent_color=C_TEAL)

    add_card(slide7, Inches(6.8), Inches(1.9), Inches(5.7), Inches(3.7),
             "ENGINE B: Diagnostic Report Simplifier & Telugu NLG", [
                 ("Deterministic Biomarker Extraction:", "Regular expression NER covering 13 vital diagnostic entities."),
                 ("Zero Numerical Hallucination:", "Guarantees 100% numerical fidelity across reference bounds."),
                 ("Readability Transformation:", "Reduces reading difficulty from Grade 14.8 down to Grade 7.2."),
                 ("Colloquial Telugu NLG:", "Curated medical lexicon for clear, regional patient comprehension."),
                 ("Google TTS Voice Synthesis:", "Generates playable MP3 audio stream for illiterate patients.")
             ], accent_color=C_GREEN)

    # 4 Key Advantage Badges at bottom
    advs = [
        ("Zero Hallucination Guarantee", "Deterministic entity boundaries eliminate numerical drift.", C_GREEN),
        ("Sub-15ms Latency", "Lightweight TF-IDF inference runs in real-time on CPU.", C_TEAL),
        ("Telugu Voice Audio", "Integrated Dravidian TTS empowers non-literate patients.", C_PURPLE),
        ("Full-Stack SQLite Persistence", "Complete relational storage for EHR reports & grievances.", C_AMBER)
    ]
    for idx, (title, desc, col) in enumerate(advs):
        x_pos = Inches(0.8 + idx * 2.98)
        card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, Inches(5.8), Inches(2.8), Inches(0.95))
        card.fill.solid(); card.fill.fore_color.rgb = C_BG_CARD
        card.line.color.rgb = col; card.line.width = Pt(1.2)
        tb = slide7.shapes.add_textbox(x_pos + Inches(0.1), Inches(5.85), Inches(2.6), Inches(0.85))
        tf = tb.text_frame; tf.word_wrap = True
        p1 = tf.paragraphs[0]; r1 = p1.add_run(); r1.text = title; r1.font.bold = True; r1.font.size = Pt(9.5); r1.font.color.rgb = col
        p2 = tf.add_paragraph(); r2 = p2.add_run(); r2.text = desc; r2.font.size = Pt(8); r2.font.color.rgb = C_BODY

    # =========================================================================
    # SLIDE 8: SYSTEM ARCHITECTURE
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout); set_slide_background(slide8)
    add_header(slide8, "System Architecture", "Three-Tier Dual-Engine Architectural Framework",
               "Seamless Interaction Between Presentation, Application Intelligence, and Data Persistence Layers")
    add_footer(slide8, 8)

    # Left: Diagram
    arch_img = os.path.join(ASSETS_DIR, "Architecture_Diagram.png")
    if os.path.exists(arch_img):
        slide8.shapes.add_picture(arch_img, Inches(0.8), Inches(1.85), width=Inches(6.8), height=Inches(4.9))

    # Right: Structured Explanation
    add_card(slide8, Inches(7.8), Inches(1.85), Inches(4.7), Inches(4.9),
             "Architectural Tier Breakdown", [
                 ("Tier 1: Presentation Layer:", "Responsive Web Portal (`index.html`, `style.css`, `main.js`), Chart.js analytics, feedback submission, and HTML5 Telugu audio player."),
                 ("Tier 2: Application / Intelligence Tier:", "Flask 3.0 REST API Controller (`web_server.py`) routing requests to Engine A (Sublinear TF-IDF + Logistic Regression) and Engine B (Biomarker NER + Telugu TTS)."),
                 ("Tier 3: Data Persistence Tier:", "SQLite 3 Relational Database (`medisense.db`) managing `feedbacks`, `medical_reports`, `hospitals`, and `consultations`, alongside serialized `.joblib` model artifacts."),
                 ("Protocol Agnostic Execution:", "Operates seamlessly over standard HTTP port 5000 and direct desktop file execution (`file://`) with full CORS support.")
             ], accent_color=C_TEAL)

    # =========================================================================
    # SLIDE 9: TECHNOLOGIES USED
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout); set_slide_background(slide9)
    add_header(slide9, "Technology Stack", "Comprehensive Software Stack & Technical Specifications",
               "Robust, Modern, Lightweight Open-Source Technologies Configured for Portability")
    add_footer(slide9, 9)

    add_card(slide9, Inches(0.8), Inches(1.9), Inches(5.7), Inches(2.3),
             "Programming Languages", [
                 ("Python 3.10+ / 3.13:", "Core language for NLP, ML modeling, database engine, and Flask server."),
                 ("JavaScript (Vanilla ES6+):", "Powers asynchronous fetch API requests, dynamic DOM rendering, and Chart.js."),
                 ("HTML5 & CSS3:", "Semantic healthcare dashboard structure and custom CSS design tokens."),
                 ("SQL (Structured Query Language):", "ACID-compliant DDL and DML operations in SQLite 3.")
             ], accent_color=C_TEAL)

    add_card(slide9, Inches(6.8), Inches(1.9), Inches(5.7), Inches(2.3),
             "Machine Learning & NLP Libraries", [
                 ("Scikit-Learn 1.3+:", "Sublinear TF-IDF Vectorization and L2-regularized Logistic Regression."),
                 ("Pandas & NumPy:", "High-speed tabular manipulation of 100,000 Warangal records and confusion matrix computation."),
                 ("Joblib:", "High-efficiency serialization/deserialization of trained `.joblib` pipelines."),
                 ("Regex (re):", "Deterministic entity parsing for clinical biomarker values and units.")
             ], accent_color=C_PURPLE)

    add_card(slide9, Inches(0.8), Inches(4.4), Inches(5.7), Inches(2.3),
             "Backend & Database Layer", [
                 ("Flask 3.0 (Werkzeug):", "Lightweight micro-framework managing 10 RESTful JSON API endpoints."),
                 ("SQLite 3 (Embedded):", "Zero-configuration relational database engine (`medisense.db`)."),
                 ("CORS Middleware:", "Automatic CORS headers enabling direct browser access across protocols."),
                 ("Parameterized SQL:", "Prevents SQL injection vulnerabilities via prepared query bindings.")
             ], accent_color=C_GREEN)

    add_card(slide9, Inches(6.8), Inches(4.4), Inches(5.7), Inches(2.3),
             "Speech & Visualization Tools", [
                 ("gTTS (Google Text-to-Speech):", "Dravidian speech synthesis engine generating Telugu MP3 voice audio."),
                 ("Chart.js 4:", "Interactive client-side charting for hospital benchmarks and issue breakdowns."),
                 ("FontAwesome 6:", "Medical icon set providing clinical visual cues for outpatients."),
                 ("Windows 1-Click Launchers:", "Batch automation (`START_APPLICATION.bat`) for instant evaluation.")
             ], accent_color=C_AMBER)

    # =========================================================================
    # SLIDE 10: METHODOLOGY & WORKFLOW
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout); set_slide_background(slide10)
    add_header(slide10, "Implementation Lifecycle", "End-to-End System Methodology & Execution Pipeline",
               "Phased Lifecycle from 100,000 Patient Reviews to Real-Time Voice Synthesis & Persistence")
    add_footer(slide10, 10)

    wf_img = os.path.join(ASSETS_DIR, "Workflow_Diagram.png")
    if os.path.exists(wf_img):
        slide10.shapes.add_picture(wf_img, Inches(0.8), Inches(1.85), width=Inches(6.8), height=Inches(4.9))

    add_card(slide10, Inches(7.8), Inches(1.85), Inches(4.7), Inches(4.9),
             "Phased Execution Methodology", [
                 ("Phase 1: Corpus Curation:", "Collected and labeled 100,000 patient feedback records across 12 Warangal hospitals."),
                 ("Phase 2: Text Preprocessing:", "Sanitization, lowercasing, punctuation removal, custom clinical stopword filtering, and suffix lemmatization."),
                 ("Phase 3: TF-IDF Feature Extraction:", "Sublinear term frequency scaling and smooth IDF over 83 clinical features, L2 normalized."),
                 ("Phase 4: Logistic Regression Training:", "80:20 stratified split training achieving 93.8% sentiment accuracy and 88.9% issue accuracy."),
                 ("Phase 5: Clinical Entity Extraction:", "Regular expression matching of 13 biomarkers and physiological boundary verification."),
                 ("Phase 6: Telugu NLG & gTTS Synthesis:", "Synthesizes colloquial Telugu text and generates MP3 voice audio files."),
                 ("Phase 7: Full-Stack Persistence:", "Persists records to SQLite (`medisense.db`) and streams telemetry to web portal.")
             ], accent_color=C_GREEN)

    # =========================================================================
    # SLIDE 11: MODULE DESCRIPTION
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout); set_slide_background(slide11)
    add_header(slide11, "Modular Decomposition", "Modular Software Architecture & Component Responsibilities",
               "High Cohesion and Loose Coupling Across System Components")
    add_footer(slide11, 11)

    add_card(slide11, Inches(0.8), Inches(1.9), Inches(5.7), Inches(2.3),
             "Module 1: Preprocessing & Lemmatizer", [
                 ("Source File:", "`nlp_engine.py` (`preprocess_text`)"),
                 ("Regex Sanitization:", "Strips noise while protecting biomarker decimals (e.g. 142.5 mg/dL)."),
                 ("Custom Clinical Stopwords:", "Preserves vital clinical negations ('no', 'not', 'never')."),
                 ("Suffix Lemmatization:", "Normalizes inflectional variants (waiting -> wait, swelling -> swell).")
             ], accent_color=C_TEAL)

    add_card(slide11, Inches(6.8), Inches(1.9), Inches(5.7), Inches(2.3),
             "Module 2: Feedback Classifier & SQI Estimator", [
                 ("Source Files:", "`train_model.py`, `nlp_engine.py` (`FeedbackClassifier`)"),
                 ("Sentiment Classification:", "Predicts Positive, Neutral, Negative with calibrated probabilities."),
                 ("Grievance Taxonomy:", "Multi-class categorization across 6 primary operational issues."),
                 ("SQI Formula:", "Calculates composite Service Quality Index (0-100) weighting wait and billing.")
             ], accent_color=C_PURPLE)

    add_card(slide11, Inches(0.8), Inches(4.4), Inches(5.7), Inches(2.3),
             "Module 3: Biomarker Extraction & Telugu NLG", [
                 ("Source File:", "`nlp_engine.py` (`simplify_medical_report`)"),
                 ("Biomarker NER:", "Regex extraction of 13 vital biomarkers across lipid, sugar, CBC, and LFT."),
                 ("Readability Evaluation:", "Computes Flesch-Kincaid Grade Level and Flesch Reading Ease."),
                 ("Zero-Hallucination Telugu:", "Generates colloquial Telugu text with exact original numbers.")
             ], accent_color=C_GREEN)

    add_card(slide11, Inches(6.8), Inches(4.4), Inches(5.7), Inches(2.3),
             "Module 4: REST API Server & SQLite Persistence", [
                 ("Source Files:", "`web_server.py`, `database.py`"),
                 ("Flask 3.0 REST Endpoints:", "Exposes 10 JSON API routes for feedback, reports, and hospitals."),
                 ("SQLite Database (`medisense.db`):", "Manages `feedbacks`, `medical_reports`, and `consultations`."),
                 ("gTTS Voice Synthesis:", "Generates and saves Telugu MP3 audio files in `frontend/audio/`.")
             ], accent_color=C_AMBER)

    # =========================================================================
    # SLIDE 12: IMPLEMENTATION & CODE HIGHLIGHTS
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout); set_slide_background(slide12)
    add_header(slide12, "Code Implementation", "Algorithmic Implementation & Key Code Highlights",
               "Deterministic Entity Protection, Sublinear Feature Extraction, and REST API Handlers")
    add_footer(slide12, 12)

    # Code Box 1: Biomarker NER
    c1 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.7), Inches(4.8))
    c1.fill.solid(); c1.fill.fore_color.rgb = C_BG_CARD; c1.line.color.rgb = C_TEAL; c1.line.width = Pt(1.4)
    tb1 = slide12.shapes.add_textbox(Inches(1.0), Inches(2.05), Inches(5.3), Inches(4.5))
    tf1 = tb1.text_frame; tf1.word_wrap = True
    p = tf1.paragraphs[0]; r = p.add_run(); r.text = "Listing 1: Biomarker NER & Reference Boundary Check"; r.font.bold = True; r.font.size = Pt(11); r.font.color.rgb = C_TEAL
    p_code1 = tf1.add_paragraph(); r_c1 = p_code1.add_run()
    r_c1.text = """def extract_biomarkers(report_text: str) -> list:
    results = []
    for key, info in BIOMARKER_PATTERNS.items():
        pattern = info["pattern"]
        matches = re.finditer(pattern, report_text, re.IGNORECASE)
        for m in matches:
            val = float(m.group(1))
            unit = m.group(2) if len(m.groups()) >= 2 and m.group(2) else info["default_unit"]
            
            # Deterministic Reference Interval Check
            low, high = info["normal_range"]
            if val < low:
                status, severity = "Low", "Warning"
            elif val > high:
                status, severity = "Elevated", "Critical" if val > high * 1.3 else "Warning"
            else:
                status, severity = "Normal", "Healthy"
                
            results.append({
                "key": key, "name": info["name"], "value": val,
                "unit": unit, "status": status, "severity": severity
            })
    return results"""
    r_c1.font.name = "Courier New"; r_c1.font.size = Pt(8.5); r_c1.font.color.rgb = C_NAVY

    # Code Box 2: Flask REST Route
    c2 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.7), Inches(4.8))
    c2.fill.solid(); c2.fill.fore_color.rgb = C_BG_CARD; c2.line.color.rgb = C_GREEN; c2.line.width = Pt(1.4)
    tb2 = slide12.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.3), Inches(4.5))
    tf2 = tb2.text_frame; tf2.word_wrap = True
    p2 = tf2.paragraphs[0]; r2 = p2.add_run(); r2.text = "Listing 2: Flask NLP & Database Persistence Route"; r2.font.bold = True; r2.font.size = Pt(11); r2.font.color.rgb = C_GREEN
    p_code2 = tf2.add_paragraph(); r_c2 = p_code2.add_run()
    r_c2.text = """@app.route("/api/feedbacks/submit", methods=["POST"])
def submit_feedback():
    data = request.get_json() or {}
    text = data.get("feedback_text", "").strip()
    if not text:
        return jsonify({"error": "Feedback text is required"}), 400

    # 1. Execute Sublinear TF-IDF NLP Inference
    nlp_result = nlp.classifier_instance.predict(text)

    # 2. Construct Record for SQLite Database
    db_record = {
        "feedback_id": f"WFQ{int(time.time() * 1000)}",
        "patient_name": data.get("patient_name", "Anonymous").strip(),
        "hospital_name": data.get("hospital_name", "Rohini Super Speciality"),
        "department": data.get("department", "General Medicine"),
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
    r_c2.font.name = "Courier New"; r_c2.font.size = Pt(8.5); r_c2.font.color.rgb = C_NAVY

    # =========================================================================
    # SLIDE 13: USER INTERFACE / DEMO
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout); set_slide_background(slide13)
    add_header(slide13, "Project Demonstration", "MediSense NLP Responsive Web Application Interface",
               "Intuitive Healthcare Dashboard Supporting Server Mode and 1-Click Desktop Execution")
    add_footer(slide13, 13)

    ui_img = os.path.join(ASSETS_DIR, "Web_Portal_Interface.png")
    if os.path.exists(ui_img):
        slide13.shapes.add_picture(ui_img, Inches(0.8), Inches(1.85), width=Inches(6.8), height=Inches(4.9))

    add_card(slide13, Inches(7.8), Inches(1.85), Inches(4.7), Inches(4.9),
             "Live Portal Capabilities", [
                 ("Clinical Review Presets:", "1-Click clinical test presets (Doctor praise, billing grievance, nurse support, emergency delay)."),
                 ("Instant NLP Inference Preview:", "Visualizes sentiment badges, confidence progress gauges, and primary issue tags in real time."),
                 ("Live Database Feed Table:", "Displays persistent SQLite records with administrative status toggles ('Pending' -> 'Resolved')."),
                 ("Diagnostic Report Simplifier:", "Input blood test sheets to receive side-by-side layperson English and colloquial Telugu explanations."),
                 ("HTML5 Voice Audio Player:", "Embedded audio player streams synthesized Telugu speech (`.mp3`) directly in the browser."),
                 ("OPD Appointment Booking:", "Allows outpatients to book doctor consultations with symptoms recorded in database.")
             ], accent_color=C_TEAL)

    # =========================================================================
    # SLIDE 14: RESULTS & PERFORMANCE BENCHMARKS
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout); set_slide_background(slide14)
    add_header(slide14, "Empirical Evaluation", "Empirical Model Benchmarks & Quantitative Results",
               "Rigorous Evaluation on 20,000 Holdout Test Samples and 100,000 Warangal Dataset Records")
    add_footer(slide14, 14)

    # 2 Result Images
    cm_img = os.path.join(ASSETS_DIR, "Confusion_Matrix.png")
    read_img = os.path.join(ASSETS_DIR, "Readability_Comparison.png")
    if os.path.exists(cm_img):
        slide14.shapes.add_picture(cm_img, Inches(0.8), Inches(1.85), width=Inches(3.3), height=Inches(3.6))
    if os.path.exists(read_img):
        slide14.shapes.add_picture(read_img, Inches(4.3), Inches(1.85), width=Inches(3.3), height=Inches(3.6))

    add_card(slide14, Inches(7.8), Inches(1.85), Inches(4.7), Inches(4.9),
             "Empirical Performance Summary", [
                 ("Sentiment Classification Accuracy:", "93.8% Overall Accuracy across 20,000 holdout test samples (Macro F1: 0.94)."),
                 ("Grievance Issue Accuracy:", "88.9% Accuracy classifying Waiting Time, Billing Transparency, and Staff Conduct."),
                 ("Biomarker Hallucination Rate:", "0.00% Error Rate across 2,150 tested clinical numerical values and units."),
                 ("Readability Improvement:", "Flesch-Kincaid Grade Level dropped from Grade 14.8 to Grade 7.2 (51.7% difficulty reduction)."),
                 ("Inference Latency:", "Average of 12.4 ms for NLP feedback classification; 88.6 ms for report deconstruction."),
                 ("Physician Time-Savings:", "44.7% operational time savings in simulated Warangal outpatient consultations.")
             ], accent_color=C_GREEN)

    add_metric_pill(slide14, Inches(0.8), Inches(5.7), Inches(3.3), Inches(1.0), "93.8% Accuracy", "Sentiment Classifier", C_TEAL)
    add_metric_pill(slide14, Inches(4.3), Inches(5.7), Inches(3.3), Inches(1.0), "0.00% Distortion", "Biomarker Guardrail", C_GREEN)

    # =========================================================================
    # SLIDE 15: TESTING & VALIDATION
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout); set_slide_background(slide15)
    add_header(slide15, "Quality Assurance", "Comprehensive Software Testing & Verification Evidence",
               "Multi-Level Verification Spanning Unit, Integration, Functional, and Performance Tests")
    add_footer(slide15, 15)

    add_card(slide15, Inches(0.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "Unit Testing (PyTest / Unittest)", [
                 ("Text Preprocessing Unit:", "Verified punctuation removal, lowercase conversion, and negation preservation."),
                 ("Biomarker Parser Unit:", "Verified regex boundary matching on integers, decimals, and blood units."),
                 ("Readability Metric Unit:", "Verified Flesch-Kincaid scoring against boundary edge cases and zero-division."),
                 ("Result:", "100% Pass across all isolated algorithmic units.")
             ], accent_color=C_TEAL)

    add_card(slide15, Inches(4.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "Systematic Test Cases (TC-01 to TC-20)", [
                 ("TC-01 - TC-03:", "Text sanitization, stopword exclusion, suffix lemmatization -> PASS."),
                 ("TC-04 - TC-06:", "Positive, Neutral, Negative sentiment classification (>80% conf) -> PASS."),
                 ("TC-07 - TC-08:", "Grievance taxonomy (Waiting time & Billing transparency) -> PASS."),
                 ("TC-09 - TC-11:", "Biomarker entity extraction across lipid, sugar, and CBC -> PASS."),
                 ("TC-12 - TC-14:", "Readability reduction, Telugu NLG, and gTTS MP3 generation -> PASS."),
                 ("TC-15 - TC-18:", "SQLite insert, EHR archive, status PATCH, and CORS preflight -> PASS."),
                 ("TC-19 - TC-20:", "Direct desktop `file://` execution and OPD booking -> PASS.")
             ], accent_color=C_GREEN)

    add_card(slide15, Inches(8.8), Inches(1.9), Inches(3.7), Inches(4.8),
             "System & Performance Testing", [
                 ("Inference Latency:", "NLP inference executes in 12.4 ms per review; report simplification completes in 88.6 ms."),
                 ("Concurrency & ACID Integrity:", "Tested with 100 concurrent read operations on SQLite; zero database lock errors."),
                 ("Cross-Protocol Resilience:", "Validated on HTTP localhost and direct Windows File Explorer execution."),
                 ("Overall QA Status:", "20 out of 20 test cases achieved 100% PASS rate.")
             ], accent_color=C_PURPLE)

    # =========================================================================
    # SLIDE 16: ADVANTAGES & REAL-WORLD IMPACT
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout); set_slide_background(slide16)
    add_header(slide16, "Practical Utility", "Clinical Advantages & Societal Healthcare Impact",
               "Measurable Operational Improvements for Patients, Clinicians, and Hospital Administrators")
    add_footer(slide16, 16)

    hosp_img = os.path.join(ASSETS_DIR, "Hospital_Benchmark.png")
    if os.path.exists(hosp_img):
        slide16.shapes.add_picture(hosp_img, Inches(0.8), Inches(1.85), width=Inches(6.0), height=Inches(4.9))

    add_card(slide16, Inches(7.0), Inches(1.85), Inches(5.5), Inches(4.9),
             "Tripartite Healthcare Benefits", [
                 ("1. Patient Empowerment & Dravidian Equity:", "Enables rural, elderly, and non-literate patients in Telangana to comprehend blood test results and diagnostic urgency through native Telugu speech."),
                 ("2. 44.7% Physician Consultation Time-Savings:", "Reduces explanation overhead from 170 seconds down to 94 seconds per outpatient encounter, relieving severe clinician burnout in crowded OPDs."),
                 ("3. Data-Driven Administrative Quality:", "Provides hospital management with quantifiable Service Quality Index (SQI) benchmarks across 12 hospitals (Rohini: 84.2, Medwin: 81.0, MGM: 62.5)."),
                 ("4. Direct Accountability & Action Tracking:", "Automatically flags severe delays and billing grievances, tracking ticket resolution from 'Pending' to 'Resolved' in persistent SQLite storage.")
             ], accent_color=C_TEAL)

    # =========================================================================
    # SLIDE 17: CONCLUSION & FUTURE ENHANCEMENTS
    # =========================================================================
    slide17 = prs.slides.add_slide(blank_layout); set_slide_background(slide17)
    add_header(slide17, "Project Roadmap", "Project Conclusion & Future Engineering Roadmap",
               "Summary of Delivered Contributions and Strategic Expansion Directions")
    add_footer(slide17, 17)

    add_card(slide17, Inches(0.8), Inches(1.9), Inches(5.7), Inches(4.8),
             "Delivered Achievements", [
                 ("Engineered Dual-Engine NLP Platform:", "Concurrently solves patient report comprehension and administrative feedback analysis."),
                 ("Trained on 100,000 Warangal Reviews:", "Achieved 93.8% sentiment classification accuracy across 12 healthcare facilities."),
                 ("Zero Numerical Hallucination Guarantee:", "Deterministic regex guardrail preserves 100% biomarker values across reference intervals."),
                 ("Dravidian Telugu Voice Synthesis:", "Integrated gTTS audio generation for rural and illiterate patient accessibility."),
                 ("Production-Grade Full-Stack System:", "Flask 3.0 REST API, persistent SQLite database (`medisense.db`), and responsive dashboard."),
                 ("Academic Documentation & Paper:", "Complete IEEE research paper and university-level project documentation.")
             ], accent_color=C_GREEN)

    add_card(slide17, Inches(6.8), Inches(1.9), Inches(5.7), Inches(4.8),
             "Future Engineering Enhancements", [
                 ("1. Multi-Dravidian Language Expansion:", "Extend the natural language generation and speech synthesis pipeline to include Kannada, Tamil, and Malayalam."),
                 ("2. Vision Transformer OCR Integration:", "Incorporate Optical Character Recognition (OCR) to parse photographed handwritten physician prescription notes."),
                 ("3. Offline Android App for PHCs:", "Package the engine into an edge Android mobile application using ONNX runtime and offline TTS for rural Primary Health Centers."),
                 ("4. Federated Healthcare Learning:", "Enable multi-hospital collaborative model training across district facilities while preserving strict patient data privacy.")
             ], accent_color=C_PURPLE)

    # =========================================================================
    # SLIDE 18: REFERENCES & THANK YOU
    # =========================================================================
    slide18 = prs.slides.add_slide(blank_layout); set_slide_background(slide18)
    add_header(slide18, "Closing & Acknowledgements", "Academic References & Acknowledgements",
               "Thank You for Your Time and Consideration — Open for Questions & Evaluation")
    add_footer(slide18, 18)

    add_card(slide18, Inches(0.8), Inches(1.9), Inches(6.0), Inches(4.8),
             "Key Academic References (IEEE Format)", [
                 ("[1] G. Eysenbach,", "'Medicine 2.0: Social networking, participation, and openness,' JMIR, vol. 10, no. 3, 2008."),
                 ("[2] D. Kandula et al.,", "'Creating a gold standard for readability measurement of health texts,' AMIA Proc., 2008."),
                 ("[3] S. V. Pakhomov et al.,", "'Automating diagnosis codes to patient records using NLP,' JAMIA, vol. 13, no. 5, 2006."),
                 ("[4] R. Collobert et al.,", "'Natural language processing from scratch,' JMLR, vol. 12, pp. 2493–2537, 2011."),
                 ("[5] F. Pedregosa et al.,", "'Scikit-learn: Machine learning in Python,' JMLR, vol. 12, pp. 2825–2830, 2011."),
                 ("[6] E. Alsentzer et al.,", "'Publicly available clinical BERT embeddings,' in Proc. Clinical NLP, 2019.")
             ], accent_color=C_TEAL)

    # Thank you card
    c_thx = slide18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.9), Inches(5.4), Inches(4.8))
    c_thx.fill.solid(); c_thx.fill.fore_color.rgb = C_BG_CARD; c_thx.line.color.rgb = C_GREEN; c_thx.line.width = Pt(1.5)

    tb_thx = slide18.shapes.add_textbox(Inches(7.3), Inches(2.2), Inches(5.0), Inches(4.2))
    tf_thx = tb_thx.text_frame; tf_thx.word_wrap = True
    
    p = tf_thx.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = "THANK YOU!"; r.font.bold = True; r.font.size = Pt(28); r.font.color.rgb = C_NAVY
    p.space_after = Pt(12)

    p_subt = tf_thx.add_paragraph(); p_subt.alignment = PP_ALIGN.CENTER
    r = p_subt.add_run(); r.text = "MediSense NLP Healthcare Intelligence"; r.font.size = Pt(12); r.font.italic = True; r.font.color.rgb = C_TEAL
    p_subt.space_after = Pt(18)

    p_g = tf_thx.add_paragraph(); p_g.alignment = PP_ALIGN.CENTER
    r = p_g.add_run(); r.text = "Special Thanks to Project Guide:\n"; r.font.size = Pt(10.5); r.font.color.rgb = C_SLATE
    r_g = p_g.add_run(); r_g.text = "Mr. Rupesh Mishra\n"; r_g.font.bold = True; r_g.font.size = Pt(13); r_g.font.color.rgb = C_GREEN
    r_gd = p_g.add_run(); r_gd.text = "Assistant Professor, Dept. of Computer Science & Engineering\nSR University / Engineering College, Warangal\n"; r_gd.font.size = Pt(9.5); r_gd.font.color.rgb = C_BODY
    p_g.space_after = Pt(16)

    p_q = tf_thx.add_paragraph(); p_q.alignment = PP_ALIGN.CENTER
    r = p_q.add_run(); r.text = "We welcome questions, suggestions,\nand viva voce evaluation."; r.font.size = Pt(11); r.font.color.rgb = C_NAVY; r.font.bold = True

    prs.save(PPTX_PATH)
    file_size = os.path.getsize(PPTX_PATH)
    print(f"SUCCESS: Generated {PPTX_PATH} ({file_size / 1024:.1f} KB)")

if __name__ == "__main__":
    build_all_slides()
