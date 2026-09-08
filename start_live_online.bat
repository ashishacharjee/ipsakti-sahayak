@echo off
title IP-SAKTI Sahayak - Live Online Tunnel
echo ===================================================
echo   IP-SAKTI Sahayak (SIH 2026) - Live Online Launcher
echo ===================================================
echo.
echo Starting FastAPI server in background...
start /B python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
timeout /t 3 >nul
echo.
echo Starting secure public Cloudflare Tunnel...
echo Your public HTTPS link will appear below:
echo ===================================================
.\cloudflared.exe tunnel --url http://127.0.0.1:8000 --no-autoupdate
pause
