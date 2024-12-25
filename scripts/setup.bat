@echo off

:: Navigate to the project root directory
cd /d "%~dp0.."

:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run the main script
python -m src.main