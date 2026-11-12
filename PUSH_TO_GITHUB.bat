@echo off
title Push MediSense NLP to GitHub (2303A51194/NLP-project)
color 0B
echo ===================================================================
echo     PUSHING MEDISENSE NLP TO GITHUB
echo     Target: https://github.com/2303A51194/NLP-project
echo ===================================================================
echo.
echo Attempting to push to main branch...
echo.

git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===================================================================
    echo [SUCCESS] Code pushed successfully to https://github.com/2303A51194/NLP-project !
    echo ===================================================================
) else (
    echo.
    echo ===================================================================
    echo [PERMISSION ERROR] 
    echo Your computer is signed into GitHub as '2303A51185'.
    echo GitHub blocked access because '2303A51185' does not have write
    echo permission to '2303A51194/NLP-project'.
    echo.
    echo TO FIX THIS:
    echo 1. Open: https://github.com/2303A51194/NLP-project/settings/access
    echo 2. Click 'Add people' and invite '2303A51185' with Write access.
    echo 3. Run this file (PUSH_TO_GITHUB.bat) again!
    echo ===================================================================
)
echo.
pause
