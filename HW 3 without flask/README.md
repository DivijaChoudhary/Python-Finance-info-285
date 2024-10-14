# Flask Stock Info App

This is a simple Flask web application that retrieves real-time stock data using the Yahoo API. Users can enter a stock symbol (e.g., ADBE for Adobe) and get the latest stock price, price change, and percentage change.

## Features:
- Fetches real-time stock prices using Yahoo Api.
- Displays company name, stock price, and changes in a web interface.
- Handles errors such as invalid stock symbols and network issues.

## Installation:
1. **Create and activate a virtual environment (optional but recommended):**
    python -m venv venv
    source venv/bin/activate   # On Mac/Linux
    venv\Scripts\activate      # On Windows

2. **Install the dependencies:**
    pip install -r requirements.txt

3. **Run the application:** 
   python main.py



