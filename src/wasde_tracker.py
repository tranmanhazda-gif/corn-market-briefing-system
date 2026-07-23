import pandas as pd
import matplotlib.pyplot as plt

def plot_ending_stocks_trend(input_path="data/wasde_tracker.csv",
                               output_path="figures/wasde_ending_stocks.png"):
    """
    Plots corn ending stocks across WASDE releases to show whether
    USDA's supply/demand outlook is tightening or loosening over time.
    """
    data = pd.read_csv(input_path, parse_dates=["release_date"])

    # Focus on the current marketing year for a clean trend line
    current_year = data[data["marketing_year"] == "2026/27"]

    plt.figure(figsize=(10, 5))
    plt.plot(current_year["release_date"], current_year["ending_stocks_bb"],
             marker="o", color="darkgreen", linewidth=2)

    plt.title("Corn Ending Stocks by WASDE Report (2026/27 Marketing Year)")
    plt.xlabel("WASDE Release Date")
    plt.ylabel("Ending Stocks (billion bushels)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")
    plt.close()

if __name__ == "__main__":
    plot_ending_stocks_trend()