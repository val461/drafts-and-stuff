import yfinance as yf
import os
import pandas as pd

CACHE_DIR = "stock_data_cache"

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def download_data(symbol):
    """Downloads or loads cached data for the given stock symbol."""
    ensure_cache_dir()
    file_path = f"{CACHE_DIR}/{symbol}.csv"
    if os.path.exists(file_path):
        print(f"Loading cached data for {symbol}")
        return pd.read_csv(file_path, index_col="Date", parse_dates=True)

    print(f"Downloading data for {symbol}")
    data = yf.download(symbol, period='1mo', interval='1d')
    if not data.empty:
        data.to_csv(file_path)
    return data

def is_marubozu(row, threshold=0.02, body_threshold=0.10):
    body_size = abs(row['Close'] - row['Open'])
    candle_range = row['High'] - row['Low']
    upper_wick = row['High'] - max(row['Close'], row['Open'])
    lower_wick = min(row['Close'], row['Open']) - row['Low']

    return (body_size / candle_range >= 0.90 and
            upper_wick / candle_range < threshold and
            lower_wick / candle_range < threshold and
            body_size / row['Close'] > body_threshold and
            body_size / row['Close'] < 0.20)

def screen_stocks(symbols):
    results = []
    for symbol in symbols:
        data = download_data(symbol)
        if data.empty or len(data) < 20:
            continue
        data['Marubozu'] = data.apply(is_marubozu, axis=1)

        for i in range(20, len(data)):
            if data.iloc[i]['Marubozu'] and not data.iloc[i-20:i]['Marubozu'].any():
                results.append((symbol, data.index[i], data.iloc[i]['Close']))
    return results

def main():
    # Usage
    symbols = ['AAPL', 'TSLA', 'MSFT']
    results = screen_stocks(symbols)
    print("Marubozu found in:")
    print(results)

if __name__ == "__main__":
    main()
