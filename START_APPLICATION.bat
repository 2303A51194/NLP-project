@echo off
title MediSense NLP - Healthcare Web Platform ^& Backend
color 0A
echo ===================================================================
echo     MEDISENSE NLP: HOSPITAL SERVICE QUALITY ^& REPORT SIMPLIFIER
echo            Full-Stack Web Portal (Backend + Frontend)
echo                 Authors: K. Priya ^& CH. Harshini
echo ===================================================================
echo.
echo [1/3] Loading Backend (Flask + SQLite + NLP Models)...
echo [2/3] Connecting to Frontend Interface...
echo [3/3] Opening Web Browser to http://localhost:5000...
echo.
timeout /t 2 /nobreak >nul
start http://localhost:5000
cd backend
python web_server.py
pause
