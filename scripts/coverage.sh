#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")/.."

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Please create one first."
    exit 1
fi

# Run pytest with coverage
pytest --cov=src --cov-report=html tests/

# Notify user
echo "Test coverage report generated in the 'htmlcov' directory."