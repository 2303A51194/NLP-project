@echo off
title GitHub Login
color 0B
echo ===================================================================
echo                     GITHUB LOGIN CLI
echo ===================================================================
echo.
echo Launching GitHub Web authentication...
echo.
gh auth login --web -h github.com -p https
echo.
pause
