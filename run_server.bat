@echo off
REM Script to start the Todo Application Backend server

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the server
python start_server.py