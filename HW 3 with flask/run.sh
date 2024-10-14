#!/bin/bash
# Script to set up environment, install dependencies, and run Flask app

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
  echo "Virtual environment activated."
else
  # If no virtual environment exists, create one
  echo "Creating virtual environment..."
  python3 -m venv venv
  source venv/bin/activate
  echo "Virtual environment created and activated."
fi

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Set environment variables for Flask
export FLASK_APP=app.py
export FLASK_ENV=development  # Enables debug mode

# Run the Flask app
echo "Starting Flask app..."
flask run
