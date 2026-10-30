@echo off
title MediSense NLP - Healthcare Web Platform ^& Backend
color 0A
echo ===================================================================
echo     MEDISENSE NLP: HOSPITAL SERVICE QUALITY ^& REPORT SIMPLIFIER
echo            Full-Stack Web Portal (Backend + Frontend)
echo                 Authors: K. Priya ^& CH. Harshini
echo ===================================================================
echo.
echo Starting Backend Server on http://localhost:5000...
timeout /t 2 /nobreak >nul
start http://localhost:5000
cd backend
python web_server.py
pause
