@echo off
title SQLGuard - Static SQL Injection Scanner
cd /d "%~dp0"

if "%~1"=="" (
    echo Enter path to Python file or folder to scan:
    set /p TARGET=
) else (
    set TARGET=%~1
)

python cli.py "%TARGET%"
pause
