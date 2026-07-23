import yfinance as yf
import pandas as pd

def download_corn_data(period="1y", interval="1d"):
    """
    Downloads corn futures price data from Yahoo Finance.

    Parameters:
        period: how far back to pull data (e.g. "1y" = 1 year, "6mo", "5y")
        interval: bar size (e.g. "1d" = daily, "1wk" = weekly)

    Returns:
        A pandas DataFrame with columns: Open, High, Low, Close, Volume
    """
    ticker = "ZC=F"
    data = yf.download(ticker, period=period, interval=interval)
    return data

if __name__ == "__main__":
    corn_data = download_corn_data()
    print(corn_data.head())
    print(f"\nTotal rows downloaded: {len(corn_data)}")

    corn_data.to_csv("data/raw/corn_futures_raw.csv")
    print("Saved to data/raw/corn_futures_raw.csv")