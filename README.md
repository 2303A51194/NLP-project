# MediSense NLP — Healthcare Service Quality & Medical Report Simplification

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: Academic](https://img.shields.io/badge/License-Academic%20Research-green.svg?style=for-the-badge)](#)

> **B.Tech Computer Science & Engineering Mini Project**  
> **Authors:** K. Priya & CH. Harshini  
> **Institution:** Department of Computer Science & Engineering, Warangal  

---

## 🏥 Overview

**MediSense NLP** is an end-to-end, dual-engine healthcare natural language processing web platform designed for regional hospital ecosystems:

1. **Hospital Quality & Patient Grievance Intelligence:** Analyzes multi-aspect patient feedback reviews using a 15-stage academic NLP pipeline, categorizing sentiment (Positive, Negative, Neutral) and primary issues (Long Waiting Time, Billing Opacity, Staff Behavior, Cleanliness, Doctor Consultation) across 100,000 Warangal hospital reviews.
2. **Clinical Report Simplifier & Telugu Translation:** Extracts critical biomarkers from diagnostic lab reports with zero numerical hallucination, calculates Flesch-Kincaid readability metrics, translates explanations into colloquial Telugu, and generates synthetic voice audio.
3. **Full-Stack Relational Database Backend:** Built on Python Flask and persistent SQLite (`medisense.db`) with full REST APIs for feedback submissions, EHR report archiving, hospital metrics, and doctor consultation booking.

---

## 📁 Repository Organization

```
priya nlp/
│
├── 📁 backend/                                        # Dedicated Backend & Database Folder
│   ├── web_server.py                                 # Flask REST API Web Server & Static Asset Handler
│   ├── database.py                                   # SQLite Database Manager (medisense.db)
│   ├── nlp_engine.py                                 # Core NLP Pipeline & Telugu TTS Engine
│   ├── train_model.py                                # ML Training on 100,000 Patient Reviews
│   ├── medisense.db                                  # Active SQLite Relational Database
│   ├── run_backend.bat                               # 1-Click Launcher (Backend only)
│   └── 📁 models/                                    # Serialized Machine Learning Models
│       ├── sentiment_model.joblib
│       ├── issue_model.joblib
│       ├── tfidf_vectorizer.joblib
│       └── metrics_summary.json
│
├── 📁 frontend/                                       # Dedicated Frontend Folder
│   ├── index.html                                    # Responsive Healthcare Dashboard UI
│   ├── open_frontend.bat                             # 1-Click Launcher (Frontend only)
│   ├── 📁 css/
│   │   └── style.css                                 # UI Design System (Cards, Badges, Charts)
│   ├── 📁 js/
│   │   └── main.js                                   # REST API Client, Chart.js & Audio Logic
│   └── 📁 audio/                                     # Synthesized Telugu Voice Audio Files (.mp3)
│
├── 📊 warangal_hospital_service_quality_feedback_100k.csv  # 100k Benchmark Dataset
├── 📑 IEEE_Research_Paper.docx                        # Full IEEE Research Paper (Word format)
├── 📑 IEEE_Research_Paper.md                          # IEEE Research Paper (Markdown source)
├── ⚙️ START_APPLICATION.bat                           # 1-Click Full-Stack Launcher (Backend + Browser)
├── ⚙️ run_website.bat                                 # Quick Website Launcher
└── 📄 requirements.txt                                # Python Dependencies
```

---

## 🔬 NLP Architecture & Benchmarks

| Metric / Component | Value | Notes |
| :--- | :--- | :--- |
| **Sentiment Accuracy** | **93.8%** | Stratified 5-Fold Cross Validation on Warangal Dataset |
| **Sentiment F1-Score** | **93.6%** | L2-Regularized Multinomial Logistic Regression |
| **Grievance Issue Accuracy** | **89.4%** | Multi-class Classification across 6 Primary Issue Categories |
| **Biomarker Extraction Precision** | **100.0%** | Deterministic Regex + Clinical Dictionary |
| **Numerical Hallucination Rate** | **0.00%** | Zero clinical value distortion guarantee |
| **Readability Improvement** | **45.2% Reduction** | Flesch-Kincaid Grade Level dropped from 14.2 to 6.8 |
| **Voice Synthesis** | **Telugu (te)** | Automated Text-to-Speech audio generation |

---

## 🚀 Execution Instructions

### Option 1: 1-Click Launch (Windows Recommended)
Simply double-click:
```
START_APPLICATION.bat
```
This automatically boots the Flask backend server on `http://localhost:5000` and opens the web application in your default browser.

### Option 2: Run Backend Separately
```bash
cd backend
python web_server.py
```

### Option 3: Open Frontend Separately
Double-click `frontend/open_frontend.bat` or open `frontend/index.html` directly in any web browser.

---

## 🗄️ Database Schema (`medisense.db`)

- **`feedbacks`**: Stores patient grievance submissions, department routing, sentiment, confidence scores, and administrative status (`Pending`, `Under Review`, `Resolved`).
- **`medical_reports`**: Archives patient diagnostic reports, extracted biomarkers JSON, plain-English summaries, Telugu translations, readability scores, and voice audio links.
- **`hospitals`**: Directory of 12 Warangal healthcare institutions with contact details and bed capacities.
- **`consultation_inquiries`**: Outpatient department (OPD) appointment requests and doctor clinical notes.

---

## 👥 Project Team
- **K. Priya** — CSE Department, Warangal
- **CH. Harshini** — CSE Department, Warangal
