@echo off
title IP-SAKTI Sahayak - Automated Test Suite
echo ===================================================
echo   Running IP-SAKTI Sahayak 37 Automated Tests
echo ===================================================
echo.
python -m pytest tests/ -v
echo.
pause
