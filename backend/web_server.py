"""
MediSense NLP Web Server (Flask Full-Stack Healthcare Backend & API)
Authors: K. Priya & CH. Harshini
Department of Computer Science & Engineering, Warangal
"""

import os
import time
import json
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory

import nlp_engine as nlp
import database as db

# Resolve Frontend Directory
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

app = Flask(__name__)

# Enable CORS for requests from file:// or other local ports
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
    return response

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
        return response

# Look for dataset in backend or parent directory
HOSPITAL_DATA_FILE = os.path.join(os.path.dirname(__file__), "warangal_hospital_service_quality_feedback_100k.csv")
if not os.path.exists(HOSPITAL_DATA_FILE):
    HOSPITAL_DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "warangal_hospital_service_quality_feedback_100k.csv")

CACHED_STATS = None


def get_hospital_stats():
    """Computes aggregated benchmark stats across the 100k dataset and live database."""
    global CACHED_STATS
    if CACHED_STATS is not None:
        return CACHED_STATS

    if not os.path.exists(HOSPITAL_DATA_FILE):
        return {"error": "Dataset not found"}

    df = pd.read_csv(HOSPITAL_DATA_FILE, nrows=25000)

    # 1. Hospital-wise stats
    hosp_group = df.groupby("hospital_name").agg({
        "overall_satisfaction_score": "mean",
        "waiting_time_min": "mean",
        "service_quality_index": "mean",
        "feedback_id": "count"
    }).reset_index()

    hosp_group.columns = ["hospital_name", "avg_satisfaction", "avg_waiting_time", "avg_sqi", "record_count"]
    hosp_group["avg_satisfaction"] = hosp_group["avg_satisfaction"].round(1)
    hosp_group["avg_waiting_time"] = hosp_group["avg_waiting_time"].round(1)
    hosp_group["avg_sqi"] = hosp_group["avg_sqi"].round(1)
    hosp_group = hosp_group.sort_values(by="avg_satisfaction", ascending=False)

    # 2. Issues breakdown
    issues_series = df["primary_issue"].value_counts().head(6)
    issues_data = [{"issue": k, "count": int(v)} for k, v in issues_series.items()]

    # 3. Overall metrics
    CACHED_STATS = {
        "total_records": len(df),
        "mean_satisfaction": round(float(df["overall_satisfaction_score"].mean()), 1),
        "mean_waiting_time": round(float(df["waiting_time_min"].mean()), 1),
        "mean_sqi": round(float(df["service_quality_index"].mean()), 1),
        "hospitals": hosp_group.to_dict(orient="records"),
        "issues": issues_data
    }
    return CACHED_STATS


# ============================================================
# 1. FRONTEND SERVING ROUTES
# ============================================================
@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "css"), filename)


@app.route("/js/<path:filename>")
def serve_js(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "js"), filename)


@app.route("/audio/<path:filename>")
def serve_audio(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "audio"), filename)


@app.route("/<path:filename>")
def serve_root_file(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# ============================================================
# 2. FEEDBACK NLP & DATABASE REST APIS
# ============================================================
@app.route("/api/analyze-feedback", methods=["POST"])
def analyze_feedback():
    """Runs NLP inference on feedback text."""
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No feedback text provided"}), 400

    result = nlp.classifier_instance.predict(text)
    return jsonify(result)


@app.route("/api/feedbacks/submit", methods=["POST"])
def submit_feedback():
    """Analyzes feedback using NLP AND persists it directly into SQLite database."""
    data = request.get_json() or {}
    text = data.get("feedback_text", "").strip()
    if not text:
        return jsonify({"error": "Feedback text is required"}), 400

    # 1. Run NLP pipeline
    nlp_result = nlp.classifier_instance.predict(text)

    # 2. Build record for SQLite database
    db_record = {
        "feedback_id": f"WFQ{int(time.time() * 1000)}",
        "patient_name": data.get("patient_name", "Anonymous Patient").strip() or "Anonymous Patient",
        "hospital_name": data.get("hospital_name", "Rohini Super Speciality Hospital").strip(),
        "department": data.get("department", "General Medicine").strip(),
        "feedback_text": text,
        "cleaned_text": nlp_result.get("cleaned_text", ""),
        "sentiment": nlp_result.get("sentiment", "Neutral"),
        "confidence": nlp_result.get("confidence", 85.0),
        "primary_issue": nlp_result.get("primary_issue", "No Major Issue"),
        "urgency_level": nlp_result.get("urgency_level", "Low"),
        "sqi_score": nlp_result.get("estimated_sqi", 75.0),
        "status": "Under Review" if nlp_result.get("urgency_level") == "High" else "Pending",
        "admin_notes": "Analyzed by MediSense NLP Engine. Auto-assigned to department."
    }

    # 3. Save to database
    saved = db.save_feedback(db_record)
    saved.update(nlp_result)
    return jsonify({
        "success": True,
        "message": "Feedback analyzed and saved to database successfully!",
        "data": saved
    }), 201


@app.route("/api/feedbacks", methods=["GET"])
def get_all_feedbacks():
    """Retrieves feedback records from SQLite with optional filtering."""
    hospital = request.args.get("hospital")
    sentiment = request.args.get("sentiment")
    urgency = request.args.get("urgency")
    status = request.args.get("status")
    limit = int(request.args.get("limit", 50))

    feedbacks = db.get_feedbacks(
        hospital=hospital,
        sentiment=sentiment,
        urgency=urgency,
        status=status,
        limit=limit
    )
    return jsonify({"success": True, "count": len(feedbacks), "feedbacks": feedbacks})


@app.route("/api/feedbacks/<feedback_id>/status", methods=["PATCH"])
def update_feedback_status(feedback_id):
    """Updates feedback resolution status in database (e.g. Pending -> Resolved)."""
    data = request.get_json() or {}
    new_status = data.get("status", "Resolved")
    notes = data.get("admin_notes", "Resolved by hospital quality administrator.")

    updated = db.update_feedback_status(feedback_id, new_status, notes)
    if updated:
        return jsonify({"success": True, "message": f"Feedback {feedback_id} status updated to {new_status}"})
    return jsonify({"error": "Feedback record not found"}), 404


@app.route("/api/feedbacks/<feedback_id>", methods=["DELETE"])
def delete_feedback(feedback_id):
    """Deletes a feedback record from SQLite database."""
    deleted = db.delete_feedback(feedback_id)
    if deleted:
        return jsonify({"success": True, "message": f"Feedback {feedback_id} deleted successfully"})
    return jsonify({"error": "Feedback record not found"}), 404


# ============================================================
# 3. MEDICAL REPORT SIMPLIFICATION & EHR APIS
# ============================================================
@app.route("/api/simplify-report", methods=["POST"])
def simplify_report():
    """Extracts biomarkers, computes readability, generates Telugu translation & audio, and saves to database."""
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No report text provided"}), 400

    patient_name = data.get("patient_name", "Outpatient Case").strip() or "Outpatient Case"
    hospital_name = data.get("hospital_name", "Rohini Super Speciality Hospital").strip()

    # 1. Run NLP report simplifier
    result = nlp.simplify_medical_report(text)

    # 2. Synthesize Telugu voice audio inside frontend/audio/
    audio_dir = os.path.join(FRONTEND_DIR, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    audio_filename = f"telugu_report_{int(time.time())}.mp3"
    audio_abs_path = os.path.join(audio_dir, audio_filename)
    audio_url = f"/audio/{audio_filename}"

    try:
        nlp.generate_telugu_tts(result["telugu_explanation"], output_path=audio_abs_path)
        result["audio_url"] = audio_url
    except Exception as e:
        result["audio_url"] = None
        result["audio_error"] = str(e)

    # 3. Automatically persist to SQLite database (EHR archive)
    report_record = {
        "report_id": f"MED{int(time.time() * 1000)}",
        "patient_name": patient_name,
        "hospital_name": hospital_name,
        "original_text": text,
        "plain_english": result["full_plain_english"],
        "telugu_explanation": result["telugu_explanation"],
        "biomarkers": result["biomarkers"],
        "original_grade": result["original_readability"]["flesch_kincaid_grade"],
        "simplified_grade": result["simplified_readability"]["flesch_kincaid_grade"],
        "audio_url": result.get("audio_url", "")
    }

    try:
        saved_info = db.save_medical_report(report_record)
        result["report_id"] = saved_info["report_id"]
        result["saved_to_db"] = True
    except Exception as e:
        result["saved_to_db"] = False
        result["db_error"] = str(e)

    return jsonify(result)


@app.route("/api/reports", methods=["GET"])
def get_all_reports():
    """Retrieves saved patient medical reports from database."""
    limit = int(request.args.get("limit", 20))
    reports = db.get_medical_reports(limit=limit)
    return jsonify({"success": True, "count": len(reports), "reports": reports})


@app.route("/api/reports/<report_id>", methods=["DELETE"])
def delete_report(report_id):
    """Deletes a saved medical report from database."""
    deleted = db.delete_medical_report(report_id)
    if deleted:
        return jsonify({"success": True, "message": f"Report {report_id} deleted successfully"})
    return jsonify({"error": "Report not found"}), 404


# ============================================================
# 4. HOSPITALS & CONSULTATION APIS
# ============================================================
@app.route("/api/hospitals", methods=["GET"])
def list_hospitals():
    """Returns directory of Warangal hospitals."""
    hospitals = db.get_hospitals()
    return jsonify({"success": True, "hospitals": hospitals})


@app.route("/api/hospital-stats", methods=["GET"])
def hospital_stats():
    """Returns benchmark hospital statistics."""
    stats = get_hospital_stats()
    return jsonify(stats)


@app.route("/api/consultations", methods=["GET", "POST"])
def consultations_handler():
    """GET list of consultations or POST a new appointment request."""
    if request.method == "POST":
        data = request.get_json() or {}
        if not data.get("patient_name") or not data.get("phone"):
            return jsonify({"error": "Patient name and phone number are required"}), 400

        saved = db.save_consultation(data)
        return jsonify({"success": True, "message": "Consultation inquiry booked successfully!", "data": saved}), 201

    inquiries = db.get_consultations(limit=20)
    return jsonify({"success": True, "inquiries": inquiries})


# ============================================================
# 5. BACKEND SYSTEM HEALTH & METRICS
# ============================================================
@app.route("/api/system/health", methods=["GET"])
def system_health():
    """Returns system status, active database counts, model status, and uptime."""
    db_summary = db.get_database_summary()
    model_loaded = (nlp.classifier_instance.model is not None and nlp.classifier_instance.vectorizer is not None)
    return jsonify({
        "status": "online",
        "backend_framework": "Flask 3.0",
        "database": db_summary,
        "nlp_model_loaded": model_loaded,
        "model_type": "TF-IDF + L2 Logistic Regression",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })


# ============================================================
# 6. RUN SERVER
# ============================================================
if __name__ == "__main__":
    print("=" * 65)
    print("MEDISENSE NLP HEALTHCARE BACKEND SERVER RUNNING")
    print(f"Serving Frontend from: {FRONTEND_DIR}")
    print("Backend API & SQLite Database Active at: http://127.0.0.1:5000")
    print("=" * 65)
    app.run(host="0.0.0.0", port=5000, debug=False)
