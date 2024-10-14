from flask import Flask, render_template, request
import yfinance as yf
from datetime import datetime
import pytz
import requests

app = Flask(__name__)

def get_stock_info(symbol):
    """Fetch stock info using Yahoo Finance (yfinance)."""
    try:
        stock = yf.Ticker(symbol)
        stock_info = stock.info

        # Check if valid stock data is available
        if not stock_info or 'currentPrice' not in stock_info:
            return {"error": f"No data found for symbol '{symbol}'. Please enter a valid stock symbol."}

        # Set the timezone to 'PDT' (Pacific Daylight Time)
        current_time = datetime.now(pytz.timezone('America/Los_Angeles')).strftime('%a %b %d %H:%M:%S PDT %Y')
        company_name = stock_info.get('longName', symbol)
        stock_price = stock_info['currentPrice']

        # Check for 'previousClose' and calculate change
        previous_close = stock_info.get('previousClose', None)
        if previous_close:
            change = stock_price - previous_close
            change_percent = (change / previous_close) * 100
        else:
            change = 'N/A'
            change_percent = 'N/A'

        # Format the change and change percent values properly
        formatted_change = f"{'+' if isinstance(change, (int, float)) and change > 0 else ''}{change:.2f}"
        formatted_change_percent = f"{'+' if isinstance(change_percent, (int, float)) and change_percent > 0 else ''}{change_percent:.2f}%"

        # Return the stock data
        return {
            'current_time': current_time,
            'company_name': company_name,
            'symbol': symbol.upper(),
            'stock_price': f"{stock_price:.2f}",
            'formatted_change': formatted_change,
            'change_percent': formatted_change_percent,
            'error': None
        }

    except requests.exceptions.ConnectionError:
        return {"error": "Network error: Please check your internet connection and try again."}
    except Exception as e:
        return {"error": f"Error retrieving stock data: {str(e)}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        stock_data = get_stock_info(symbol)

    return render_template('index.html', stock_data=stock_data)

if __name__ == '__main__':
    app.run(debug=True)
