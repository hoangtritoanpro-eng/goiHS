@echo off
title Khoi dong May Chu MS Edge TTS
color 0B
echo ========================================================
echo   HE THONG GOI HOC SINH - AI VOICE CLONING SERVER
echo ========================================================
echo.
echo Dang kiem tra va cai dat thu vien (Neu co)...
pip install edge-tts flask flask-cors --quiet
echo.
echo ========================================================
echo Dang khoi dong AI... Moi lan mo dau se hoi lau 1 chut.
echo Vui long giu nguyen cua so nay khi dang dung he thong!
echo ========================================================
python tts_server.py
pause
