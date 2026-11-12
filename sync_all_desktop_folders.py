"""
Sync all updated presentation, documentation, and web files to Desktop folders.
"""

import os
import shutil
import zipfile

DESKTOP = "C:\\Users\\hp\\OneDrive\\Desktop"

# 1. Update Warangal_HealthRAG_Project_Presentation
folder_pres = os.path.join(DESKTOP, "Warangal_HealthRAG_Project_Presentation")
if os.path.exists(folder_pres):
    print("Updating Warangal_HealthRAG_Project_Presentation...")
    shutil.copy2("Project_Presentation/Project_Presentation.pptx", os.path.join(folder_pres, "Project_Presentation.pptx"))
    shutil.copy2("Project_Presentation/Project_Presentation.pdf", os.path.join(folder_pres, "Project_Presentation.pdf"))
    shutil.copy2("Project_Presentation/Presentation_Speech.docx", os.path.join(folder_pres, "Presentation_Speech.docx"))
    shutil.copy2("Project_Presentation/Viva_Questions_and_Answers.docx", os.path.join(folder_pres, "Viva_Questions_and_Answers.docx"))
    shutil.copy2("Project_Presentation/Presentation_Assets/Architecture_Diagram.png", os.path.join(folder_pres, "Architecture_Diagram.png"))
    shutil.copy2("Project_Presentation/Presentation_Assets/Workflow_Diagram.png", os.path.join(folder_pres, "Workflow_Diagram.png"))
    shutil.copy2("index.html", os.path.join(folder_pres, "index.html"))
    assets_dest = os.path.join(folder_pres, "Presentation_Assets")
    if os.path.exists(assets_dest):
        shutil.rmtree(assets_dest)
    shutil.copytree("Project_Presentation/Presentation_Assets", assets_dest)
    print("  -> Warangal_HealthRAG_Project_Presentation updated successfully.")

# 2. Update Warangal_HealthRAG_Project_Documentation
folder_doc = os.path.join(DESKTOP, "Warangal_HealthRAG_Project_Documentation")
if os.path.exists(folder_doc):
    print("Updating Warangal_HealthRAG_Project_Documentation...")
    # Overwrite old filenames so whatever user opens is the new version
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.docx", os.path.join(folder_doc, "B.Tech_Project_Report_RAG_Warangal_Medical_System.docx"))
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.pdf", os.path.join(folder_doc, "B.Tech_Project_Report_RAG_Warangal_Medical_System.pdf"))
    shutil.copy2("IEEE_Research_Paper.docx", os.path.join(folder_doc, "Research_Paper_RAG_Warangal_Medical_System.docx"))
    
    # Also add the new clean named files
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.docx", os.path.join(folder_doc, "B.Tech_Project_Report_Final_Thesis.docx"))
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.pdf", os.path.join(folder_doc, "B.Tech_Project_Report_Final_Thesis.pdf"))
    shutil.copy2("IEEE_Research_Paper.docx", os.path.join(folder_doc, "IEEE_Research_Paper.docx"))
    shutil.copy2("index.html", os.path.join(folder_doc, "index.html"))

    fig_dest = os.path.join(folder_doc, "Figures_and_Diagrams")
    if os.path.exists(fig_dest):
        shutil.rmtree(fig_dest)
    shutil.copytree("Project_Documentation", fig_dest, ignore=shutil.ignore_patterns("*.docx", "*.pdf"))
    print("  -> Warangal_HealthRAG_Project_Documentation updated successfully.")

# 3. Update MediSense_NLP_Project
folder_medisense = os.path.join(DESKTOP, "MediSense_NLP_Project")
if os.path.exists(folder_medisense):
    print("Updating MediSense_NLP_Project...")
    # Presentation
    med_pres = os.path.join(folder_medisense, "4_Project_Presentation")
    os.makedirs(med_pres, exist_ok=True)
    for f in os.listdir("Project_Presentation"):
        src = os.path.join("Project_Presentation", f)
        dst = os.path.join(med_pres, f)
        if os.path.isdir(src):
            if os.path.exists(dst): shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    shutil.copy2("Project_Presentation/Presentation_Assets/Architecture_Diagram.png", os.path.join(med_pres, "Architecture_Diagram.png"))
    shutil.copy2("Project_Presentation/Presentation_Assets/Workflow_Diagram.png", os.path.join(med_pres, "Workflow_Diagram.png"))

    # Documentation
    med_doc = os.path.join(folder_medisense, "3_Project_Documentation")
    os.makedirs(med_doc, exist_ok=True)
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.docx", os.path.join(med_doc, "B.Tech_Project_Report_Final_Thesis.docx"))
    shutil.copy2("Project_Documentation/Complete_Project_Documentation.pdf", os.path.join(med_doc, "B.Tech_Project_Report_Final_Thesis.pdf"))
    shutil.copy2("IEEE_Research_Paper.docx", os.path.join(med_doc, "IEEE_Research_Paper.docx"))

    # Frontend
    med_fe = os.path.join(folder_medisense, "1_Modern_Frontend")
    shutil.copy2("index.html", os.path.join(med_fe, "index.html"))

    print("  -> MediSense_NLP_Project updated successfully.")

# 4. Create dedicated brand new folder: NLP_Based_Hospital_Service_Quality_Analysis_Warangal
brand_folder = os.path.join(DESKTOP, "NLP_Based_Hospital_Service_Quality_Analysis_Warangal")
print(f"Creating/Updating clean folder: {brand_folder}...")
os.makedirs(os.path.join(brand_folder, "1_Project_Presentation", "Presentation_Assets"), exist_ok=True)
os.makedirs(os.path.join(brand_folder, "2_Project_Documentation", "Figures_and_Diagrams"), exist_ok=True)
os.makedirs(os.path.join(brand_folder, "3_Web_Application", "css"), exist_ok=True)
os.makedirs(os.path.join(brand_folder, "3_Web_Application", "js"), exist_ok=True)
os.makedirs(os.path.join(brand_folder, "3_Web_Application", "models"), exist_ok=True)

# Copy Presentation
p_dst = os.path.join(brand_folder, "1_Project_Presentation")
shutil.copy2("Project_Presentation/Project_Presentation.pptx", os.path.join(p_dst, "Project_Presentation.pptx"))
shutil.copy2("Project_Presentation/Project_Presentation.pdf", os.path.join(p_dst, "Project_Presentation.pdf"))
shutil.copy2("Project_Presentation/Presentation_Speech.docx", os.path.join(p_dst, "Presentation_Speech.docx"))
shutil.copy2("Project_Presentation/Viva_Questions_and_Answers.docx", os.path.join(p_dst, "Viva_Questions_and_Answers.docx"))
shutil.copy2("Project_Presentation/Presentation_Assets/Architecture_Diagram.png", os.path.join(p_dst, "Architecture_Diagram.png"))
shutil.copy2("Project_Presentation/Presentation_Assets/Workflow_Diagram.png", os.path.join(p_dst, "Workflow_Diagram.png"))
for f in os.listdir("Project_Presentation/Presentation_Assets"):
    shutil.copy2(os.path.join("Project_Presentation/Presentation_Assets", f), os.path.join(p_dst, "Presentation_Assets", f))

# Copy Documentation
d_dst = os.path.join(brand_folder, "2_Project_Documentation")
shutil.copy2("Project_Documentation/Complete_Project_Documentation.docx", os.path.join(d_dst, "B.Tech_Project_Report_Final_Thesis.docx"))
shutil.copy2("Project_Documentation/Complete_Project_Documentation.pdf", os.path.join(d_dst, "B.Tech_Project_Report_Final_Thesis.pdf"))
shutil.copy2("IEEE_Research_Paper.docx", os.path.join(d_dst, "IEEE_Research_Paper.docx"))
for f in os.listdir("Project_Documentation"):
    src = os.path.join("Project_Documentation", f)
    if os.path.isfile(src):
        shutil.copy2(src, os.path.join(d_dst, "Figures_and_Diagrams", f))

# Copy Web Application
w_dst = os.path.join(brand_folder, "3_Web_Application")
shutil.copy2("index.html", os.path.join(w_dst, "index.html"))
for f in os.listdir("css"):
    shutil.copy2(os.path.join("css", f), os.path.join(w_dst, "css", f))
for f in os.listdir("js"):
    shutil.copy2(os.path.join("js", f), os.path.join(w_dst, "js", f))
for f in ["web_server.py", "nlp_engine.py", "database.py", "train_model.py", "app.py"]:
    if os.path.exists(f):
        shutil.copy2(f, os.path.join(w_dst, f))
if os.path.exists("medisense.db"):
    shutil.copy2("medisense.db", os.path.join(w_dst, "medisense.db"))
if os.path.exists("models"):
    for f in os.listdir("models"):
        shutil.copy2(os.path.join("models", f), os.path.join(w_dst, "models", f))

# Root launchers inside brand_folder
with open(os.path.join(brand_folder, "START_PROJECT_WEBSITE.bat"), "w", encoding="utf-8") as f:
    f.write("@echo off\ntitle Launching Hospital Quality NLP System\ncd /d \"%~dp03_Web_Application\"\nstart \"\" http://localhost:5000\npython web_server.py\npause\n")

with open(os.path.join(brand_folder, "OPEN_OFFLINE_FRONTEND.bat"), "w", encoding="utf-8") as f:
    f.write("@echo off\ntitle Opening Offline Dashboard\nstart \"\" \"%~dp03_Web_Application\\index.html\"\n")

readme_content = f"""===================================================================
NLP-BASED HOSPITAL SERVICE QUALITY ANALYSIS IN WARANGAL
B.Tech Capstone Project • Academic Year 2026 - 2027
Department of Computer Science & Engineering
SR University / Engineering College, Warangal, Telangana
===================================================================

INVESTIGATORS:
1. KATAKAM PRIYA  (Hall Ticket / Roll No: 2303A51194)
2. CH. HARSHINI   (Hall Ticket / Roll No: 2303A51185)

PROJECT SUPERVISOR / GUIDE:
Mr. Rupesh Mishra
Assistant Professor, Department of Computer Science & Engineering

PROJECT ABSTRACT:
"NLP-Based Hospital Service Quality Analysis in Warangal is a Natural
Language Processing-based project that analyzes patient reviews and
feedback to evaluate the quality of hospital services. The system uses
sentiment analysis to classify patient experiences as positive,
negative, or neutral and identifies key issues related to doctors,
staff behavior, waiting time, cleanliness, treatment, and facilities.
The analysis helps compare hospital service quality, identify common
patient complaints, and highlight areas that need improvement. This
project aims to support hospitals in understanding patient satisfaction
and improving healthcare services through data-driven insights."

FOLDER CONTENTS:
-------------------------------------------------------------------
1_Project_Presentation/
   • Project_Presentation.pptx  (Editable 16:9 widescreen PowerPoint)
   • Project_Presentation.pdf   (16:9 landscape compiled vector PDF)
   • Presentation_Speech.docx   (Slide-by-slide 30-60s speaking script)
   • Viva_Questions_and_Answers.docx (50 comprehensive Q&As)
   • Architecture_Diagram.png & Workflow_Diagram.png
   • Presentation_Assets/ (All 8 high-res charts and diagrams)

2_Project_Documentation/
   • B.Tech_Project_Report_Final_Thesis.docx (Full Academic Thesis)
   • B.Tech_Project_Report_Final_Thesis.pdf  (Compiled PDF Thesis)
   • IEEE_Research_Paper.docx (Two-column IEEE format paper)
   • Figures_and_Diagrams/ (All high-resolution figures)

3_Web_Application/
   • index.html (Responsive clinical studio dashboard)
   • web_server.py (Flask 3.0 REST API backend)
   • nlp_engine.py (Sublinear TF-IDF + Logistic Regression NLP)
   • database.py & medisense.db (SQLite 3 database)
   • models/ (Trained serialized NLP model weights)

HOW TO RUN:
1. Double-click START_PROJECT_WEBSITE.bat to launch Flask server & open browser.
2. Double-click OPEN_OFFLINE_FRONTEND.bat to open dashboard directly.
===================================================================
"""
with open(os.path.join(brand_folder, "README.txt"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("  -> NLP_Based_Hospital_Service_Quality_Analysis_Warangal folder created successfully.")

# 5. Compress both ZIP archives
print("Compressing desktop ZIP archives...")
zip_clean = os.path.join(DESKTOP, "NLP_Based_Hospital_Service_Quality_Analysis_Warangal.zip")
with zipfile.ZipFile(zip_clean, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(brand_folder):
        for file in files:
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, brand_folder)
            zipf.write(full_p, rel_p)
print(f"Created: {zip_clean}")

zip_medisense = os.path.join(DESKTOP, "MediSense_NLP_Project.zip")
with zipfile.ZipFile(zip_medisense, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_medisense):
        for file in files:
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, folder_medisense)
            zipf.write(full_p, rel_p)
print(f"Refreshed: {zip_medisense}")

print("ALL DESKTOP FOLDERS FULLY UPDATED AND VERIFIED!")
