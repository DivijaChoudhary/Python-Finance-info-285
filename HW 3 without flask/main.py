import yfinance as yf
from datetime import datetime
import pytz
import requests

def get_stock_info(symbol):
    """Fetch stock info using Yahoo Finance (yfinance)."""
    try:
        stock = yf.Ticker(symbol)
        stock_info = stock.info

        # Check if stock info is available (invalid symbol handling)
        if not stock_info or 'currentPrice' not in stock_info:
            print(f"No data found for symbol '{symbol}'. Please enter a valid stock symbol.")
            return

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

        # Format the output for change
        change_symbol = '+' if isinstance(change, (int, float)) and change > 0 else ''

        # Display formatted stock information
        print(f"\n{current_time}")
        print(f"{company_name} ({symbol})")
        print(f"{stock_price:.2f} {change_symbol}{change:.2f} ({change_symbol}{change_percent:.2f}%)")

    except requests.exceptions.ConnectionError:
        print("Network error: Please check your internet connection and try again.")
    except Exception as e:
        print(f"Error retrieving stock data: {str(e)}")

if __name__ == "__main__":
    while True:
        # Input stock symbol from user
        symbol = input("\nPlease enter a symbol: ").upper()
        if not symbol:
            break  # Break the loop if no input is provided
        get_stock_info(symbol)
