#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")/.."

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the main script
python -m src.main