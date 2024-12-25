@echo off

REM Navigate to the project root directory
cd /d "%~dp0.."

REM Activate the virtual environment if it exists
IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) ELSE (
    echo Virtual environment not found. Please create one first.
    exit /b 1
)

REM Run pytest with coverage
pytest --cov=src --cov-report=html tests/

REM Notify user
echo Test coverage report generated in the 'htmlcov' directory.