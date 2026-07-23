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