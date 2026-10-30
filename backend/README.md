# MediSense NLP - Backend Architecture
**Authors:** K. Priya & CH. Harshini  
**Department:** Computer Science & Engineering, Warangal  

This directory contains the complete Python backend, REST API engine, and SQLite database for the MediSense NLP Healthcare system.

---

### Folder Contents
| File / Directory | Description |
| :--- | :--- |
| `web_server.py` | Flask REST API server; serves frontend assets & handles all NLP inference and database CRUD endpoints. |
| `database.py` | SQLite database manager (`medisense.db`) with schemas for patient feedback, medical reports, hospitals, and consultation appointments. |
| `nlp_engine.py` | Core Natural Language Processing pipeline: TF-IDF vectorizer, Logistic Regression sentiment & issue classifier, biomarker extractor, and Telugu report simplifier. |
| `train_model.py` | Supervised NLP model training script on 100,000 Warangal hospital patient reviews. |
| `medisense.db` | Active SQLite relational database containing stored patient records. |
| `models/` | Serialized machine learning models (`sentiment_model.joblib`, `issue_model.joblib`, `tfidf_vectorizer.joblib`, `metrics_summary.json`). |
| `run_backend.bat` | 1-Click launcher to start the Flask backend server on `http://127.0.0.1:5000`. |

---

### How to Run Backend Alone
Double-click `run_backend.bat` or run:
```bash
python web_server.py
```
Backend will start on `http://127.0.0.1:5000`.
