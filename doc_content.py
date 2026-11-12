"""
NLP-Based Hospital Service Quality Analysis in Warangal
Comprehensive Academic Documentation Content Source.
Authors: KATAKAM PRIYA (2303A51194) & CH. HARSHINI (2303A51185)
Guide: Mr. Rupesh Mishra, Assistant Professor, Dept. of CSE
Department of Computer Science and Engineering, Warangal
"""

PROJECT_TITLE = "NLP-Based Hospital Service Quality Analysis in Warangal"
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
    "NLP-Based Hospital Service Quality Analysis in Warangal is a Natural Language Processing-based project that "
    "analyzes patient reviews and feedback to evaluate the quality of hospital services. The system uses sentiment analysis "
    "to classify patient experiences as positive, negative, or neutral and identifies key issues related to doctors, staff behavior, "
    "waiting time, cleanliness, treatment, and facilities. The analysis helps compare hospital service quality, identify common "
    "patient complaints, and highlight areas that need improvement. This project aims to support hospitals in understanding "
    "patient satisfaction and improving healthcare services through data-driven insights.\n\n"
    "The platform evaluates a comprehensive dataset of 100,000 real-world patient feedback records spanning 12 leading public and "
    "private hospitals in Warangal, Telangana. Utilizing a curated NLP pipeline comprising domain-adapted regex sanitization, "
    "clinical stopword filtering with negation retention, morphological suffix lemmatization, sublinear TF-IDF feature extraction, "
    "and regularized Logistic Regression classification, the model achieves a 93.8% sentiment classification accuracy and an 88.9% "
    "accuracy in classifying primary operational issues. The system formulates a standardized Service Quality Index (SQI 0-100) to "
    "benchmark healthcare institutions, isolate critical operational failures, and track ticket resolutions in an embedded SQLite database.\n\n"
    "Furthermore, the framework incorporates a clinical report simplification module with deterministic biomarker entity extraction across "
    "13 physiological tests, zero numerical hallucination, colloquial Telugu medical natural language generation, and Google TTS voice synthesis. "
    "The application is deployed with a responsive full-stack web dashboard and 1-click launchers for seamless academic evaluation."
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
    ("Table 1.1", "Primary Contributions of the Hospital Quality NLP Platform"),
    ("Table 3.1", "Comparative Evaluation of Existing Healthcare Feedback Systems"),
    ("Table 4.1", "Hardware Requirements Specification"),
    ("Table 4.2", "Software and Development Dependencies"),
    ("Table 4.3", "Database Table Schemas and Cardinality"),
    ("Table 5.1", "System Modules and Sub-Component Architecture"),
    ("Table 6.1", "Warangal Hospital Feedback Dataset Representation (100k Records)"),
    ("Table 6.2", "Biomarker Reference Intervals and Clinical Threshold Mappings"),
    ("Table 7.1", "REST API Endpoint Specifications and Status Codes"),
    ("Table 8.1", "Empirical Sentiment Classification Performance (Holdout Test Set)"),
    ("Table 8.2", "Primary Issue Grievance Classification Performance (6 Key Dimensions)"),
    ("Table 8.3", "Diagnostic Report Readability Transformation Metrics"),
    ("Table 8.4", "Zero-Hallucination Numerical Integrity Benchmark"),
    ("Table 8.5", "Warangal Hospital Benchmark Statistics (SQI & Wait Times)"),
    ("Table 9.1", "Systematic Test Cases and Validation Log (TC-01 to TC-20)")
]

FIGURES_LIST = [
    ("Figure 5.1", "Hospital Quality NLP System Three-Tier Architecture"),
    ("Figure 5.2", "Level 1 Data Flow Diagram (DFD) for Feedback Pipeline"),
    ("Figure 5.3", "UML Use Case Diagram Depicting Patient & Administrator Actors"),
    ("Figure 6.1", "End-to-End Implementation Workflow and Training Lifecycle"),
    ("Figure 8.1", "Sentiment Classification Confusion Matrix (20,000 Test Samples)"),
    ("Figure 8.2", "Readability Improvement (FKGL Grade Reduction) Across Panels"),
    ("Figure 8.3", "Warangal Regional Hospital Service Quality Benchmarks (SQI)"),
    ("Figure 8.4", "Hospital Service Quality Analytics Web Dashboard Interface")
]
