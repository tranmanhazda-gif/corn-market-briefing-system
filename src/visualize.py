import pandas as pd
import matplotlib.pyplot as plt

def plot_price_with_ma(input_path="data/processed/corn_futures_indicators.csv",
                        output_path="figures/price_moving_averages.png"):
    """
    Plots closing price with 20/50/100-day moving averages overlaid.
    This is the primary 'is the trend up or down' chart a trader checks first.
    """
    data = pd.read_csv(input_path, index_col="Date", parse_dates=True)

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price", linewidth=1.5, color="black")
    plt.plot(data.index, data["MA_20"], label="20-Day MA", linewidth=1, color="blue")
    plt.plot(data.index, data["MA_50"], label="50-Day MA", linewidth=1, color="orange")
    plt.plot(data.index, data["MA_100"], label="100-Day MA", linewidth=1, color="red")

    plt.title("Corn Futures (ZC=F) — Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (cents per bushel)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")
    plt.close()

if __name__ == "__main__":
    plot_price_with_ma() 
def plot_volume(input_path="data/processed/corn_futures_indicators.csv",
                 output_path="figures/volume.png"):
    """
    Plots daily trading volume as a bar chart.
    Helps identify whether price moves are backed by strong participation
    or are likely noise from thin trading.
    """
    data = pd.read_csv(input_path, index_col="Date", parse_dates=True)

    plt.figure(figsize=(12, 5))
    plt.bar(data.index, data["Volume"], color="steelblue", width=1)

    plt.title("Corn Futures (ZC=F) — Daily Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume (contracts)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")
    plt.close()

if __name__ == "__main__":
    plot_price_with_ma()
    plot_volume()
def plot_daily_returns(input_path="data/processed/corn_futures_indicators.csv",
                        output_path="figures/daily_returns.png"):
    """
    Plots daily returns over time to visualize volatility clustering -
    periods where the market got choppier (often around news/report dates).
    """
    data = pd.read_csv(input_path, index_col="Date", parse_dates=True)

    plt.figure(figsize=(12, 5))
    plt.plot(data.index, data["Daily_Return"], color="darkred", linewidth=0.8)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")

    plt.title("Corn Futures (ZC=F) — Daily Returns (%)")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")
    plt.close()


def plot_return_histogram(input_path="data/processed/corn_futures_indicators.csv",
                           output_path="figures/return_histogram.png"):
    """
    Plots a histogram of daily returns to show what a 'normal' day looks like
    for this market, making unusual moves easy to spot as outliers.
    """
    data = pd.read_csv(input_path, index_col="Date", parse_dates=True)

    plt.figure(figsize=(10, 6))
    plt.hist(data["Daily_Return"].dropna(), bins=40, color="seagreen", edgecolor="black")

    plt.title("Corn Futures (ZC=F) — Distribution of Daily Returns")
    plt.xlabel("Daily Return (%)")
    plt.ylabel("Frequency (number of days)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")
    plt.close()
if __name__ == "__main__":
    plot_price_with_ma()
    plot_volume()
    plot_daily_returns()
    plot_return_histogram()
