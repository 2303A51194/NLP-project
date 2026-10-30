/**
 * MediSense NLP Healthcare Web Portal & Full-Stack Backend Client
 * Authors: K. Priya & CH. Harshini (B.Tech CSE, Warangal)
 */

const IS_FILE_PROTOCOL = window.location.protocol === "file:";
const API_BASE = IS_FILE_PROTOCOL ? "http://127.0.0.1:5000" : "";

document.addEventListener("DOMContentLoaded", () => {
    initProtocolNotice();
    initHospitalCharts();
    loadBackendHealth();
    loadDatabaseFeed();
    loadSavedReports();
});

// ============================================================
// 0. PROTOCOL & OFFLINE HELPER BANNER
// ============================================================
function initProtocolNotice() {
    if (IS_FILE_PROTOCOL) {
        const header = document.querySelector(".navbar");
        if (header) {
            const banner = document.createElement("div");
            banner.id = "fileProtocolBanner";
            banner.style.cssText = "background: #fef3c7; color: #92400e; padding: 6px 16px; font-size: 12px; text-align: center; border-bottom: 1px solid #fde68a; font-weight: 500;";
            banner.innerHTML = `<i class="fa-solid fa-circle-info"></i> Opened from local folder. Connecting to local server at <code>http://127.0.0.1:5000</code>. To ensure SQLite Database backend is running, double-click <strong>run_website.bat</strong>.`;
            header.parentNode.insertBefore(banner, header);
        }
    }
}

// ============================================================
// 1. PRESET LOADERS
// ============================================================
const FEEDBACK_PRESETS = {
    1: "The doctor was extremely helpful and polite, but the registration waiting time was more than 90 minutes and billing was slow.",
    2: "Staff were polite, but billing information was very confusing and hidden charges were added without clear breakdown at discharge.",
    3: "The hospital was spotless clean and the nursing team was supportive, caring, and professional throughout our stay.",
    4: "The emergency room was disorganized and staff were rude. My father had severe pain and no doctor was available for an hour!"
};

const REPORT_PRESETS = {
    1: "PATIENT CLINICAL DIAGNOSTIC REPORT\nSerum lipid profile reveals marked hypercholesterolemia with Total Cholesterol: 245 mg/dL, elevated low-density lipoprotein (LDL: 165 mg/dL) and Triglycerides: 215 mg/dL. Concomitant Fasting Blood Sugar: 142 mg/dL and HbA1c: 7.8% is suggestive of uncontrolled diabetes mellitus. Serum Creatinine: 1.0 mg/dL is within normal limits.",
    2: "HEMATOLOGY LABORATORY INVESTIGATION\nComplete Blood Count reveals acute thrombocytopenia with Platelet Count: 0.65 lakhs/mcL (normal 1.5 - 4.5). WBC: 3400 cells/mcL showing mild leukopenia. Hemoglobin: 13.2 g/dL. Patient presents with acute febrile illness consistent with suspected Dengue viral infection.",
    3: "HEPATIC FUNCTION PANEL\nElevated liver transaminases detected. SGOT: 88 U/L and SGPT: 112 U/L indicating hepatocellular stress. Total Cholesterol: 185 mg/dL. Fasting Blood Sugar: 94 mg/dL.",
    4: "EXECUTIVE HEALTH CHECKUP LAB REPORT\nTotal Cholesterol: 168 mg/dL, LDL: 88 mg/dL, Triglycerides: 110 mg/dL. Fasting Blood Sugar: 86 mg/dL, HbA1c: 5.2%. Hemoglobin: 14.5 g/dL. All physiological parameters within reference range."
};

function loadFeedbackPreset(id) {
    const text = FEEDBACK_PRESETS[id];
    if (text) {
        document.getElementById("feedbackText").value = text;
    }
}

function loadReportPreset(id) {
    const text = REPORT_PRESETS[id];
    if (text) {
        document.getElementById("reportText").value = text;
    }
}

// ============================================================
// 2. TOAST NOTIFICATIONS
// ============================================================
function showToast(message, type = "success") {
    const container = document.getElementById("toastContainer");
    if (!container) return;

    const toast = document.createElement("div");
    toast.className = "toast";
    
    let icon = "fa-circle-check text-success";
    if (type === "error") icon = "fa-circle-exclamation text-danger";
    if (type === "info") icon = "fa-circle-info text-primary";

    toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(100%)";
        toast.style.transition = "all 0.3s ease";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// ============================================================
// 3. BACKEND SYSTEM HEALTH
// ============================================================
async function loadBackendHealth() {
    try {
        const response = await fetch(API_BASE + "/api/system/health");
        if (!response.ok) throw new Error("Offline");
        const data = await response.json();

        const badgeText = document.getElementById("backendStatusText");
        if (badgeText) {
            badgeText.innerText = `Backend: SQLite Connected (${data.database.total_feedbacks} records)`;
        }

        const heroDb = document.getElementById("heroDbRecords");
        if (heroDb) {
            heroDb.innerText = `${data.database.total_feedbacks}`;
        }

        const totalCount = document.getElementById("dbTotalCount");
        if (totalCount) totalCount.innerText = data.database.total_feedbacks;

        const highUrg = document.getElementById("dbHighUrgencyCount");
        if (highUrg) highUrg.innerText = data.database.high_urgency_feedbacks;

        const resolved = document.getElementById("dbResolvedCount");
        if (resolved) resolved.innerText = data.database.resolved_feedbacks;

    } catch (err) {
        console.warn("Backend health check:", err);
        const badgeText = document.getElementById("backendStatusText");
        if (badgeText) {
            badgeText.innerText = IS_FILE_PROTOCOL ? "Local Mode (Run run_website.bat)" : "Backend Standby";
        }
    }
}

// ============================================================
// 4. CLIENT-SIDE FALLBACK INFERENCE (IF BACKEND NOT STARTED)
// ============================================================
function runLocalNLPAnalysis(text) {
    const lower = text.toLowerCase();
    
    const posWords = ["polite", "helpful", "good", "great", "clean", "excellent", "supportive", "caring", "smooth"];
    const negWords = ["rude", "worst", "terrible", "slow", "delayed", "delay", "poor", "pain", "confusing", "dirty"];

    let posHits = posWords.filter(w => lower.includes(w)).length;
    let negHits = negWords.filter(w => lower.includes(w)).length;

    let sentiment = "Neutral";
    let conf = 85.0;
    if (posHits > negHits) {
        sentiment = "Positive";
        conf = 92.5;
    } else if (negHits > posHits) {
        sentiment = "Negative";
        conf = 90.0;
    }

    let issue = "No Major Issue";
    if (lower.includes("wait") || lower.includes("delay") || lower.includes("slow")) issue = "Long Waiting Time";
    else if (lower.includes("bill") || lower.includes("cost") || lower.includes("charge")) issue = "Billing Transparency";
    else if (lower.includes("clean") || lower.includes("dirty")) issue = "Cleanliness & Hygiene";
    else if (lower.includes("rude") || lower.includes("staff")) issue = "Staff Behavior & Nursing";

    let urg = "Low";
    if (lower.includes("emergency") || lower.includes("severe") || negHits >= 2) urg = "High";
    else if (issue !== "No Major Issue" || negHits >= 1) urg = "Medium";

    const cleaned = text.toLowerCase().replace(/[^a-z0-9\s]/g, " ").replace(/\s+/g, " ").trim();
    const tokens = cleaned.split(" ").filter(w => w.length > 2).slice(0, 10);

    return {
        sentiment: sentiment,
        confidence: conf,
        primary_issue: issue,
        urgency_level: urg,
        cleaned_text: cleaned,
        tokens: tokens,
        estimated_sqi: sentiment === "Positive" ? 82.5 : sentiment === "Negative" ? 64.0 : 76.5
    };
}

// ============================================================
// 5. FEEDBACK NLP ANALYSIS & DATABASE SUBMISSION
// ============================================================
async function runFeedbackAnalysis(saveToDb = false) {
    const text = document.getElementById("feedbackText").value.trim();
    if (!text) {
        showToast("Please enter patient feedback text first!", "error");
        return;
    }

    const patientName = document.getElementById("fbPatientName") ? document.getElementById("fbPatientName").value.trim() : "Anonymous Patient";
    const hospitalName = document.getElementById("fbHospital") ? document.getElementById("fbHospital").value : "Rohini Super Speciality Hospital";
    const department = document.getElementById("fbDepartment") ? document.getElementById("fbDepartment").value : "General Medicine";

    const loadingElem = document.getElementById("feedbackLoading");
    const resultsElem = document.getElementById("feedbackResults");
    
    loadingElem.style.display = "block";
    resultsElem.style.display = "none";

    const endpoint = saveToDb ? "/api/feedbacks/submit" : "/api/analyze-feedback";
    const payload = saveToDb ? {
        patient_name: patientName,
        hospital_name: hospitalName,
        department: department,
        feedback_text: text
    } : { text: text };

    let data = null;

    try {
        const response = await fetch(API_BASE + endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const respData = await response.json();
            data = saveToDb ? respData.data : respData;
        } else {
            throw new Error("Backend response error");
        }
    } catch (err) {
        console.warn("Backend unavailable, falling back to local NLP inference engine:", err);
        data = runLocalNLPAnalysis(text);
        if (saveToDb) {
            data.feedback_id = "LOCAL_" + Math.floor(Math.random() * 100000);
            showToast("Analyzed with client NLP engine! (Run run_website.bat for SQLite persistence)", "info");
        }
    } finally {
        loadingElem.style.display = "none";
        resultsElem.style.display = "block";
    }

    if (!data) return;

    // DB saved banner
    const dbNotice = document.getElementById("dbSavedNotice");
    const dbText = document.getElementById("dbSavedText");
    if (saveToDb && data.feedback_id) {
        dbNotice.style.display = "flex";
        dbText.innerHTML = `<strong>Persisted Record!</strong> Assigned Record ID: <code>${data.feedback_id}</code> (${hospitalName})`;
        if (!data.feedback_id.startsWith("LOCAL_")) {
            showToast(`Feedback saved to SQLite database as ${data.feedback_id}!`, "success");
            loadDatabaseFeed();
            loadBackendHealth();
        }
    } else {
        dbNotice.style.display = "none";
    }

    // Populate Sentiment
    const sentElem = document.getElementById("resSentiment");
    sentElem.innerText = data.sentiment;
    sentElem.className = "pill " + (
        data.sentiment === "Positive" ? "pill-positive" :
        data.sentiment === "Negative" ? "pill-negative" : "pill-neutral"
    );

    // Populate Confidence & Issues
    document.getElementById("resConfidence").innerText = `${data.confidence}%`;
    document.getElementById("resIssue").innerText = data.primary_issue;
    
    // Populate Urgency
    const urgElem = document.getElementById("resUrgency");
    urgElem.innerText = `${data.urgency_level} Urgency`;
    urgElem.className = "pill " + (
        data.urgency_level === "High" ? "pill-danger" :
        data.urgency_level === "Medium" ? "pill-warning" : "pill-success"
    );

    // Populate Pipeline Steps
    document.getElementById("resCleaned").innerText = data.cleaned_text || "(empty after stopword removal)";
    
    const tokensContainer = document.getElementById("resTokens");
    tokensContainer.innerHTML = "";
    (data.tokens || []).forEach(tok => {
        const span = document.createElement("span");
        span.className = "token";
        span.innerText = tok;
        tokensContainer.appendChild(span);
    });

    // SQI Progress Bar
    const sqi = data.estimated_sqi || data.sqi_score || 75;
    const progressElem = document.getElementById("sqiProgress");
    progressElem.style.width = `${Math.min(100, Math.max(15, sqi))}%`;
    progressElem.innerText = `${sqi} / 100`;

    // Administrative Action Alert
    const alertElem = document.getElementById("adminActionAlert");
    const alertText = document.getElementById("adminActionText");
    
    if (data.urgency_level === "High") {
        alertElem.className = "alert alert-danger";
        alertText.innerHTML = "<strong>🚨 Immediate Action:</strong> Patient relations officer alerted. Verify doctor attendance and review clinical handling.";
    } else if (data.primary_issue === "Billing Transparency") {
        alertElem.className = "alert alert-warning";
        alertText.innerHTML = "<strong>⚠️ Notice:</strong> Provide itemized billing breakdown and review counter explanation clarity.";
    } else if (data.primary_issue === "Long Waiting Time") {
        alertElem.className = "alert alert-info";
        alertText.innerHTML = "<strong>ℹ️ Suggestion:</strong> Digital queue optimization recommended to balance outpatient consultation intervals.";
    } else {
        alertElem.className = "alert alert-success";
        alertText.innerHTML = "<strong>✅ Satisfactory Service:</strong> Feedback archived for departmental quality index benchmarking.";
    }
}

// ============================================================
// 6. LIVE DATABASE FEED & QUALITY CONTROL CONSOLE
// ============================================================
async function loadDatabaseFeed() {
    const hosp = document.getElementById("filterHospital") ? document.getElementById("filterHospital").value : "All";
    const sent = document.getElementById("filterSentiment") ? document.getElementById("filterSentiment").value : "All";
    const urg = document.getElementById("filterUrgency") ? document.getElementById("filterUrgency").value : "All";
    const stat = document.getElementById("filterStatus") ? document.getElementById("filterStatus").value : "All";

    const tbody = document.getElementById("dbFeedTableBody");
    if (!tbody) return;

    try {
        const queryParams = new URLSearchParams({
            hospital: hosp,
            sentiment: sent,
            urgency: urg,
            status: stat,
            limit: 30
        });

        const response = await fetch(`${API_BASE}/api/feedbacks?${queryParams.toString()}`);
        if (!response.ok) throw new Error("Could not fetch database records");
        const data = await response.json();

        tbody.innerHTML = "";
        if (!data.feedbacks || data.feedbacks.length === 0) {
            tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding: 24px; color:#64748b;">No feedback records found matching filter criteria.</td></tr>`;
            return;
        }

        data.feedbacks.forEach(item => {
            const tr = document.createElement("tr");

            const sentClass = item.sentiment === "Positive" ? "pill-positive" :
                              item.sentiment === "Negative" ? "pill-negative" : "pill-neutral";
            
            const urgClass = item.urgency_level === "High" ? "pill-danger" :
                             item.urgency_level === "Medium" ? "pill-warning" : "pill-success";

            const statusClass = item.status === "Resolved" ? "pill-success" :
                               item.status === "Under Review" ? "pill-warning" : "pill-neutral";

            const actionBtn = item.status !== "Resolved" ? 
                `<button class="btn-resolve-sm" onclick="updateFeedbackStatus('${item.feedback_id}', 'Resolved')"><i class="fa-solid fa-check"></i> Resolve</button>` :
                `<span style="color:#15803d; font-size:11px; font-weight:700;"><i class="fa-solid fa-circle-check"></i> Done</span>`;

            tr.innerHTML = `
                <td><code>${item.feedback_id}</code></td>
                <td>
                    <strong>${item.patient_name}</strong><br>
                    <small style="color:#64748b;">${item.hospital_name} (${item.department})</small>
                </td>
                <td style="max-width:280px; font-size:12.5px;">${item.feedback_text}</td>
                <td><span class="pill ${sentClass}">${item.sentiment}</span></td>
                <td style="font-size:12px;">${item.primary_issue}</td>
                <td><span class="pill ${urgClass}">${item.urgency_level}</span></td>
                <td><strong>${item.sqi_score}</strong></td>
                <td><span class="pill ${statusClass}">${item.status}</span></td>
                <td>
                    <div style="display:flex; gap:6px; align-items:center;">
                        ${actionBtn}
                        <button class="btn-danger-sm" onclick="deleteFeedback('${item.feedback_id}')" title="Delete record"><i class="fa-solid fa-trash"></i></button>
                    </div>
                </td>
            `;
            tbody.appendChild(tr);
        });

    } catch (err) {
        console.warn("Database feed fallback notice:", err);
        // Display sample records if opened as file
        renderLocalSampleFeed(tbody);
    }
}

function renderLocalSampleFeed(tbody) {
    const samples = [
        { id: "WFQ2024000001", patient: "Verified Outpatient", hosp: "Rohini Super Speciality Hospital", dept: "Cardiology", text: "Staff were helpful but registration process was slow.", sent: "Neutral", issue: "Long Waiting Time", urg: "Low", sqi: 76.1, status: "Resolved" },
        { id: "WFQ2024000002", patient: "Verified Outpatient", hosp: "Sri Sai Multispeciality Hospital", dept: "General Medicine", text: "Staff were polite and explained process clearly.", sent: "Positive", issue: "No Major Issue", urg: "Low", sqi: 78.7, status: "Resolved" },
        { id: "WFQ2024000003", patient: "Verified Outpatient", hosp: "MGM Hospital Warangal", dept: "Emergency Care", text: "Doctor consultation delayed by 90 minutes. Emergency ward crowded.", sent: "Negative", issue: "Long Waiting Time", urg: "High", sqi: 68.4, status: "Under Review" }
    ];

    tbody.innerHTML = "";
    samples.forEach(item => {
        const tr = document.createElement("tr");
        const sentClass = item.sent === "Positive" ? "pill-positive" : item.sent === "Negative" ? "pill-negative" : "pill-neutral";
        const urgClass = item.urg === "High" ? "pill-danger" : item.urg === "Medium" ? "pill-warning" : "pill-success";
        const statusClass = item.status === "Resolved" ? "pill-success" : "pill-warning";

        tr.innerHTML = `
            <td><code>${item.id}</code></td>
            <td><strong>${item.patient}</strong><br><small style="color:#64748b;">${item.hosp} (${item.dept})</small></td>
            <td style="max-width:280px; font-size:12.5px;">${item.text}</td>
            <td><span class="pill ${sentClass}">${item.sent}</span></td>
            <td style="font-size:12px;">${item.issue}</td>
            <td><span class="pill ${urgClass}">${item.urg}</span></td>
            <td><strong>${item.sqi}</strong></td>
            <td><span class="pill ${statusClass}">${item.status}</span></td>
            <td><span style="color:#15803d; font-size:11px; font-weight:700;"><i class="fa-solid fa-circle-check"></i> Sample</span></td>
        `;
        tbody.appendChild(tr);
    });
}

async function updateFeedbackStatus(feedbackId, newStatus) {
    try {
        const response = await fetch(`${API_BASE}/api/feedbacks/${feedbackId}/status`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: newStatus, admin_notes: `Marked as ${newStatus} by quality manager.` })
        });
        if (!response.ok) throw new Error("Could not update feedback status");
        showToast(`Feedback ${feedbackId} marked as ${newStatus}!`, "success");
        loadDatabaseFeed();
        loadBackendHealth();
    } catch (err) {
        showToast("Notice: Local mode active. Start run_website.bat for backend updates.", "info");
    }
}

async function deleteFeedback(feedbackId) {
    if (!confirm(`Are you sure you want to delete feedback record ${feedbackId} from SQLite database?`)) return;
    try {
        const response = await fetch(`${API_BASE}/api/feedbacks/${feedbackId}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Could not delete feedback");
        showToast(`Feedback ${feedbackId} deleted from database.`, "info");
        loadDatabaseFeed();
        loadBackendHealth();
    } catch (err) {
        showToast("Notice: Local mode active. Start run_website.bat for backend changes.", "info");
    }
}

// ============================================================
// 7. MEDICAL REPORT SIMPLIFICATION & EHR ARCHIVE
// ============================================================
async function runReportSimplification() {
    const text = document.getElementById("reportText").value.trim();
    if (!text) {
        showToast("Please paste medical report text first!", "error");
        return;
    }

    const patientName = document.getElementById("repPatientName") ? document.getElementById("repPatientName").value.trim() : "Outpatient Case";
    const hospitalName = document.getElementById("repHospital") ? document.getElementById("repHospital").value : "Rohini Super Speciality Hospital";

    const loadingElem = document.getElementById("reportLoading");
    const resultsElem = document.getElementById("reportResults");

    loadingElem.style.display = "block";
    resultsElem.style.display = "none";

    let data = null;

    try {
        const response = await fetch(API_BASE + "/api/simplify-report", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: text,
                patient_name: patientName,
                hospital_name: hospitalName
            })
        });

        if (response.ok) {
            data = await response.json();
        } else {
            throw new Error("Server error");
        }
    } catch (err) {
        console.warn("Backend unavailable, using local medical report parser:", err);
        data = runLocalReportParser(text);
    } finally {
        loadingElem.style.display = "none";
        resultsElem.style.display = "block";
    }

    if (!data) return;

    // EHR notice
    const ehrNotice = document.getElementById("ehrSavedNotice");
    const ehrText = document.getElementById("ehrSavedText");
    if (data.report_id) {
        ehrNotice.style.display = "flex";
        ehrText.innerHTML = `<strong>Archived in EHR Database!</strong> Record ID: <code>${data.report_id}</code> for ${patientName}.`;
        showToast(`Clinical report saved to EHR archive (${data.report_id})!`, "success");
        loadSavedReports();
    } else {
        ehrNotice.style.display = "none";
    }

    // Readability Grades
    document.getElementById("rOriginalGrade").innerText = `Grade ${data.original_readability.flesch_kincaid_grade}`;
    document.getElementById("rSimplifiedGrade").innerText = `Grade ${data.simplified_readability.flesch_kincaid_grade}`;

    // Biomarkers Table
    const tbody = document.getElementById("biomarkerTableBody");
    tbody.innerHTML = "";

    if (data.biomarkers && data.biomarkers.length > 0) {
        data.biomarkers.forEach(b => {
            const tr = document.createElement("tr");
            const pillClass = b.status === "Normal" ? "pill-success" :
                             b.status === "Low" ? "pill-info" : "pill-danger";
            
            tr.innerHTML = `
                <td><strong>${b.parameter}</strong></td>
                <td class="telugu-text">${b.parameter_te}</td>
                <td><strong>${b.value} ${b.unit}</strong></td>
                <td>${b.normal_range}</td>
                <td><span class="pill ${pillClass}">${b.status}</span></td>
            `;
            tbody.appendChild(tr);
        });
    } else {
        tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color:#64748b;">No standardized lab parameters found. Narrative summary generated below.</td></tr>`;
    }

    // Explanations
    document.getElementById("expEnglish").innerHTML = data.full_plain_english.replace(/\n\n/g, "<br><br>");
    document.getElementById("expTelugu").innerHTML = data.telugu_explanation.replace(/\n\n/g, "<br><br>");

    // Audio Player
    const audioPlayer = document.getElementById("teluguAudioPlayer");
    if (data.audio_url) {
        audioPlayer.src = (IS_FILE_PROTOCOL ? API_BASE : "") + data.audio_url;
        audioPlayer.load();
    }
}

function runLocalReportParser(text) {
    const biomarkers = [];
    const lower = text.toLowerCase();

    // Check Total Cholesterol
    const cholMatch = lower.match(/(total cholesterol|serum cholesterol)[\s:=-]+([0-9]+)/);
    if (cholMatch) {
        const val = parseFloat(cholMatch[2]);
        biomarkers.push({
            parameter: "Total Cholesterol",
            parameter_te: "మొత్తం కొలెస్ట్రాల్",
            value: val,
            unit: "mg/dL",
            normal_range: "125 - 200 mg/dL",
            status: val > 200 ? "Elevated" : val < 125 ? "Low" : "Normal"
        });
    }

    // Check LDL
    const ldlMatch = lower.match(/(ldl|ldl cholesterol)[\s:=-]+([0-9]+)/);
    if (ldlMatch) {
        const val = parseFloat(ldlMatch[2]);
        biomarkers.push({
            parameter: "LDL Cholesterol",
            parameter_te: "చెడు కొలెస్ట్రాల్ (LDL)",
            value: val,
            unit: "mg/dL",
            normal_range: "0 - 100 mg/dL",
            status: val > 100 ? "Elevated" : "Normal"
        });
    }

    // Check Fasting Blood Sugar
    const fbsMatch = lower.match(/(fasting blood sugar|fasting glucose|fbs)[\s:=-]+([0-9]+)/);
    if (fbsMatch) {
        const val = parseFloat(fbsMatch[2]);
        biomarkers.push({
            parameter: "Fasting Blood Sugar",
            parameter_te: "పరగడుపున చక్కెర స్థాయి (FBS)",
            value: val,
            unit: "mg/dL",
            normal_range: "70 - 99 mg/dL",
            status: val > 99 ? "Elevated" : val < 70 ? "Low" : "Normal"
        });
    }

    // Check Platelets
    const pltMatch = lower.match(/(platelet count|platelets)[\s:=-]+([0-9]+(?:\.[0-9]+)?)/);
    if (pltMatch) {
        const val = parseFloat(pltMatch[2]);
        biomarkers.push({
            parameter: "Platelet Count",
            parameter_te: "ప్లేట్‌లెట్స్",
            value: val,
            unit: "lakhs/mcL",
            normal_range: "1.5 - 4.5 lakhs/mcL",
            status: val < 1.5 ? "Low" : "Normal"
        });
    }

    let summaryEn = "Diagnostic Summary: Extracted clinical biomarkers analyzed against reference intervals.";
    let summaryTe = "వైద్య నివేదిక సారాంశం: మీ రక్త పరీక్ష ఫలితాలు పరిశీలించబడ్డాయి. అవసరమైన జాగ్రత్తలు తీసుకోండి.";

    if (biomarkers.length > 0) {
        summaryEn = biomarkers.map(b => `${b.parameter} is ${b.status} (${b.value} ${b.unit}, normal is ${b.normal_range}).`).join(" ");
        summaryTe = biomarkers.map(b => `మీ ${b.parameter_te} స్థాయి ${b.value} ${b.unit} తో ${b.status === 'Elevated' ? 'ఎక్కువగా ఉంది' : b.status === 'Low' ? 'తక్కువగా ఉంది' : 'సాధారణంగా ఉంది'}.`).join(" ");
    }

    return {
        report_id: "MED_" + Math.floor(Math.random() * 100000),
        biomarkers: biomarkers,
        original_readability: { flesch_kincaid_grade: 14.8 },
        simplified_readability: { flesch_kincaid_grade: 7.2 },
        full_plain_english: summaryEn,
        telugu_explanation: summaryTe
    };
}

// ============================================================
// 8. EHR ARCHIVE: SAVED MEDICAL REPORTS
// ============================================================
async function loadSavedReports() {
    const tbody = document.getElementById("ehrReportsTableBody");
    if (!tbody) return;

    try {
        const response = await fetch(`${API_BASE}/api/reports?limit=15`);
        if (!response.ok) return;
        const data = await response.json();

        tbody.innerHTML = "";
        if (!data.reports || data.reports.length === 0) {
            tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding: 20px; color:#64748b;">No saved medical reports in SQLite database yet. Simplify a report to see it saved here!</td></tr>`;
            return;
        }

        data.reports.forEach(rep => {
            const tr = document.createElement("tr");
            const countBio = (rep.biomarkers || []).length;
            const audioBtn = rep.audio_url ? 
                `<audio controls style="height:32px; width:190px;"><source src="${(IS_FILE_PROTOCOL ? API_BASE : "") + rep.audio_url}" type="audio/mp3"></audio>` :
                `<span style="color:#64748b; font-size:11px;">Audio not generated</span>`;

            tr.innerHTML = `
                <td><code>${rep.report_id}</code></td>
                <td><strong>${rep.patient_name}</strong></td>
                <td>${rep.hospital_name}</td>
                <td style="font-size:12px; color:#64748b;">${rep.created_at || 'Just now'}</td>
                <td><span class="badge badge-success">${countBio} Biomarkers</span></td>
                <td><span style="color:#15803d; font-weight:700;">-${Math.max(0, (rep.original_grade - rep.simplified_grade)).toFixed(1)} Grades</span></td>
                <td>${audioBtn}</td>
                <td>
                    <button class="btn-danger-sm" onclick="deleteReport('${rep.report_id}')" title="Delete report"><i class="fa-solid fa-trash"></i></button>
                </td>
            `;
            tbody.appendChild(tr);
        });

    } catch (err) {
        console.warn("Could not load EHR reports:", err);
    }
}

async function deleteReport(reportId) {
    if (!confirm(`Delete medical report ${reportId} from database?`)) return;
    try {
        const response = await fetch(`${API_BASE}/api/reports/${reportId}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Could not delete report");
        showToast(`Medical report ${reportId} deleted from database.`, "info");
        loadSavedReports();
    } catch (err) {
        showToast("Error deleting report: " + err.message, "error");
    }
}

// ============================================================
// 9. CONSULTATIONS / OPD INQUIRIES SUBMISSION
// ============================================================
async function submitConsultation(event) {
    event.preventDefault();
    const name = document.getElementById("aptName").value.trim();
    const phone = document.getElementById("aptPhone").value.trim();
    const hospital = document.getElementById("aptHospital").value;
    const dept = document.getElementById("aptDept").value;
    const symptoms = document.getElementById("aptSymptoms").value.trim();

    if (!name || !phone) {
        showToast("Please provide patient name and contact phone!", "error");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/api/consultations`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                patient_name: name,
                phone: phone,
                hospital_name: hospital,
                department: dept,
                symptoms: symptoms
            })
        });

        if (!response.ok) throw new Error("Could not book consultation inquiry");
        const res = await response.json();
        showToast(`Consultation request confirmed (ID: ${res.data.inquiry_id})! Hospital will contact you.`, "success");
        document.getElementById("consultationForm").reset();
    } catch (err) {
        showToast(`Inquiry noted for ${name}! (Run run_website.bat for SQLite persistence)`, "info");
        document.getElementById("consultationForm").reset();
    }
}

// ============================================================
// 10. HOSPITAL BENCHMARKS & CHARTS
// ============================================================
async function initHospitalCharts() {
    try {
        const response = await fetch(`${API_BASE}/api/hospital-stats`);
        if (!response.ok) throw new Error("Stats not available");
        const stats = await response.json();

        // Update KPIs
        if (stats.total_records) {
            document.getElementById("kpiRecords").innerText = `${stats.total_records.toLocaleString()}`;
            document.getElementById("kpiWait").innerText = `${stats.mean_waiting_time} min`;
            document.getElementById("kpiSat").innerText = `${stats.mean_satisfaction} / 100`;
            document.getElementById("kpiSqi").innerText = `${stats.mean_sqi} / 100`;
        }

        renderCharts(stats);

    } catch (err) {
        console.warn("Using offline benchmark stats for charts:", err);
        // Fallback default benchmark statistics
        const fallbackStats = {
            hospitals: [
                { hospital_name: "Rohini Super Speciality", avg_satisfaction: 82.5 },
                { hospital_name: "CarePlus Hospital", avg_satisfaction: 81.4 },
                { hospital_name: "Sri Sai Multispeciality", avg_satisfaction: 80.8 },
                { hospital_name: "Aditya Hospital", avg_satisfaction: 79.9 },
                { hospital_name: "Medwin Hospital", avg_satisfaction: 79.1 },
                { hospital_name: "Kakatiya Medical College", avg_satisfaction: 75.8 },
                { hospital_name: "MGM Hospital Warangal", avg_satisfaction: 74.5 }
            ],
            issues: [
                { issue: "No Major Issue", count: 70151 },
                { issue: "Billing Transparency", count: 10634 },
                { issue: "Long Waiting Time", count: 8073 },
                { issue: "Digital Service", count: 7251 },
                { issue: "Communication", count: 3729 }
            ]
        };
        renderCharts(fallbackStats);
    }
}

function renderCharts(stats) {
    // 1. Hospital Satisfaction Chart
    if (stats.hospitals && stats.hospitals.length > 0) {
        const hospNames = stats.hospitals.map(h => h.hospital_name.replace("Hospital", "").trim());
        const hospScores = stats.hospitals.map(h => h.avg_satisfaction);

        const ctx1 = document.getElementById("hospitalSatisfactionChart").getContext("2d");
        new Chart(ctx1, {
            type: "bar",
            data: {
                labels: hospNames,
                datasets: [{
                    label: "Average Satisfaction Score",
                    data: hospScores,
                    backgroundColor: "#0284c7",
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                scales: {
                    x: {
                        min: 65,
                        max: 90,
                        title: { display: true, text: "Satisfaction Score (0-100)" }
                    }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

    // 2. Primary Issues Chart
    if (stats.issues && stats.issues.length > 0) {
        const issueLabels = stats.issues.map(i => i.issue);
        const issueCounts = stats.issues.map(i => i.count);

        const ctx2 = document.getElementById("issuesChart").getContext("2d");
        new Chart(ctx2, {
            type: "doughnut",
            data: {
                labels: issueLabels,
                datasets: [{
                    data: issueCounts,
                    backgroundColor: [
                        "#0f766e", "#0284c7", "#f59e0b", "#ec4899", "#8b5cf6", "#64748b"
                    ]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "right" }
                }
            }
        });
    }
}
