@echo off
echo Starting GitHub Profile Explorer Web Application...
cd /d "%~dp0\github-profile-explorer"
start http://localhost:5173/?user=2303a51831
call npx vite --host 0.0.0.0 --port 5173
pause
