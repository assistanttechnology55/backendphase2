@echo off
REM Setup script for Todo Application Backend

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

echo Setup complete! To start the server, run:
echo venv\Scripts\activate && python start_server.py