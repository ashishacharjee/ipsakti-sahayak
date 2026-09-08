@echo off
title IP-SAKTI Sahayak - SIH 2026 Server
echo ===================================================
echo   IP-SAKTI Sahayak (SIH 2026 - Problem 26045)
echo   Ministry of Ayush / AIIA
echo   Team: Coders of GNIT
echo ===================================================
echo.
echo Installing / checking requirements...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [WARNING] Pip install encountered an issue, trying to run directly...
)
echo.
echo Starting FastAPI application server on http://127.0.0.1:8000 ...
echo Press Ctrl+C to stop the server.
echo.
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
pause
