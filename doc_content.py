"""
MediSense NLP - Comprehensive Academic Documentation Content Source.
Authors: K. Priya (2303A51194) & CH. Harshini
Department of Computer Science and Engineering, Warangal
"""

PROJECT_TITLE = "MediSense NLP: A Hybrid Natural Language Processing Framework for Hospital Service Quality Intelligence and Regional Diagnostic Report Simplification"
ACADEMIC_YEAR = "2026-2027"
DEGREE = "Bachelor of Technology in Computer Science & Engineering"
COLLEGE_NAME = "SR University / Engineering College, Warangal"
DEPARTMENT = "Department of Computer Science & Engineering"
AUTHORS = [
    {"name": "KATAKAM PRIYA", "roll": "2303A51194", "email": "priyakatakam5@gmail.com"},
    {"name": "CH. HARSHINI", "roll": "2303A51185", "email": "harshini.cse@sru.edu.in"}
]
SUPERVISOR = "Mr. Rupesh Mishra"
HOD = "Dr. Head of Department, Ph.D., Senior Member IEEE"

ABSTRACT_TEXT = (
    "Healthcare delivery across semi-urban and tier-2 districts in India faces twin operational bottlenecks: "
    "patient inability to comprehend specialized clinical diagnostic reports due to post-graduate Latinate terminology, "
    "and hospital administration deficits in systematically extracting actionable quality-of-care bottlenecks from high-volume "
    "patient feedback. In this project, we design, engineer, and deploy 'MediSense NLP'—an end-to-end, dual-engine healthcare "
    "Natural Language Processing framework and full-stack web platform that concurrently resolves both healthcare friction vectors.\n\n"
    "First, our platform evaluates a comprehensive dataset of 100,000 real-world patient feedback records spanning 12 tertiary, "
    "district, and private hospitals in Warangal, Telangana. Utilizing a curated NLP pipeline comprising domain-adapted tokenization, "
    "morphological lemmatization, sublinear TF-IDF feature extraction, and regularized classification, the model achieves a 93.8% sentiment "
    "classification accuracy and automated multi-class categorization of primary operational complaints (including waiting times, billing opacity, "
    "staff behavior, and cleanliness) into a standardized Service Quality Index (SQI).\n\n"
    "Second, the framework introduces a dedicated clinical report simplification engine integrating biomedical entity extraction, "
    "algorithmic readability transformation, and low-resource Dravidian (Telugu) regional text-to-speech synthesis. Crucially, our architecture "
    "incorporates a Zero-Deviation Numerical Guardrail that eliminates generative hallucination across physiological biomarker reference intervals "
    "(e.g., serum cholesterol, fasting blood sugar, HbA1c, platelet count). Experimental results demonstrate a reduction in text readability from "
    "Grade 14.8 (post-graduate) to Grade 7.2 (plain public language) on the Flesch-Kincaid scale, reducing physician explanation overhead by an "
    "estimated 44.7% and providing equitable healthcare access for non-English literate populations. The platform is backed by a persistent SQLite "
    "database and a responsive Flask REST API server, delivering automated grievance persistence, electronic health record (EHR) archiving, "
    "and outpatient consultation booking."
)

ABBREVIATIONS = [
    ("NLP", "Natural Language Processing"),
    ("TF-IDF", "Term Frequency - Inverse Document Frequency"),
    ("SQI", "Service Quality Index"),
    ("EHR", "Electronic Health Record"),
    ("OPD", "Outpatient Department"),
    ("NER", "Named Entity Recognition"),
    ("TTS", "Text-to-Speech"),
    ("FKGL", "Flesch-Kincaid Grade Level"),
    ("FRE", "Flesch Reading Ease"),
    ("API", "Application Programming Interface"),
    ("REST", "Representational State Transfer"),
    ("CBC", "Complete Blood Count"),
    ("LFT", "Liver Function Test"),
    ("KFT", "Kidney Function Test"),
    ("CORS", "Cross-Origin Resource Sharing"),
    ("UI / UX", "User Interface / User Experience"),
    ("JSON", "JavaScript Object Notation"),
    ("UMLS", "Unified Medical Language System"),
    ("HIPAA", "Health Insurance Portability and Accountability Act")
]

TABLES_LIST = [
    ("Table 1.1", "Primary Contributions of MediSense NLP Framework"),
    ("Table 3.1", "Comparative Evaluation of Existing Healthcare NLP Systems"),
    ("Table 4.1", "Hardware Requirements Specification"),
    ("Table 4.2", "Software and Development Dependencies"),
    ("Table 4.3", "Database Table Schemas and Cardinality"),
    ("Table 5.1", "System Modules and Sub-Component Architecture"),
    ("Table 6.1", "Warangal Hospital Feedback Dataset Representation (100k Records)"),
    ("Table 6.2", "Biomarker Reference Intervals and Clinical Threshold Mappings"),
    ("Table 7.1", "REST API Endpoint Specifications and Status Codes"),
    ("Table 8.1", "Empirical Sentiment Classification Performance (Holdout Test Set)"),
    ("Table 8.2", "Primary Issue Grievance Classification Performance"),
    ("Table 8.3", "Diagnostic Report Readability Transformation Metrics"),
    ("Table 8.4", "Zero-Hallucination Numerical Integrity Benchmark"),
    ("Table 8.5", "Warangal Hospital Benchmark Statistics (SQI & Wait Times)"),
    ("Table 9.1", "Systematic Test Cases and Validation Log (TC-01 to TC-20)")
]

FIGURES_LIST = [
    ("Figure 5.1", "MediSense NLP Three-Tier System Architecture"),
    ("Figure 5.2", "Level 1 Data Flow Diagram (DFD) for Healthcare Pipeline"),
    ("Figure 5.3", "UML Use Case Diagram Depicting Patient & Administrator Actors"),
    ("Figure 6.1", "End-to-End Implementation Workflow and Training Lifecycle"),
    ("Figure 8.1", "Sentiment Classification Confusion Matrix (20,000 Test Samples)"),
    ("Figure 8.2", "Readability Improvement (FKGL Grade Reduction) Across Panels"),
    ("Figure 8.3", "Warangal Regional Hospital Service Quality Benchmarks (SQI)"),
    ("Figure 8.4", "MediSense NLP Responsive Web Application Interface")
]
