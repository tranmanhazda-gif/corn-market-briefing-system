import pandas as pd

def add_indicators(input_path="data/processed/corn_futures_clean.csv",
                    output_path="data/processed/corn_futures_indicators.csv"):
    """
    Adds trading indicators to cleaned corn futures data:
    - Daily return (% change day to day)
    - 20/50/100-day moving averages
    - Rolling volatility (20-day)
    """
    data = pd.read_csv(input_path, index_col="Date", parse_dates=True)

    # Daily return: percentage change from previous close to today's close
    data["Daily_Return"] = data["Close"].pct_change() * 100

    # Moving averages: rolling mean of Close over the last N days
    data["MA_20"] = data["Close"].rolling(window=20).mean()
    data["MA_50"] = data["Close"].rolling(window=50).mean()
    data["MA_100"] = data["Close"].rolling(window=100).mean()

    # Rolling volatility: standard deviation of daily returns over last 20 days
    # Higher number = prices swinging more; lower = calmer market
    data["Volatility_20"] = data["Daily_Return"].rolling(window=20).std()

    data.to_csv(output_path)
    print(f"Indicators added and saved to {output_path}")
    print(f"\nLast 5 rows:")
    print(data.tail())

    return data

if __name__ == "__main__":
    add_indicators()
    