@echo off
echo ===================================================
echo Digital Forensics Toolkit (DFT) - Setup & Run
echo ===================================================

echo [1/3] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Python not found or failed to create venv.
    pause
    exit /b
)

echo [2/3] Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies.
    pause
    exit /b
)

echo [3/3] Running DFT GUI...
python gui.py

pause
