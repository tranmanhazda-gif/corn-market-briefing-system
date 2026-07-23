import pandas as pd

def clean_corn_data(input_path="data/raw/corn_futures_raw.csv",
                     output_path="data/processed/corn_futures_clean.csv"):
    """
    Cleans raw corn futures data:
    - Flattens multi-level columns from yfinance
    - Converts Date to a proper datetime column
    - Checks for and reports missing values
    - Saves a clean CSV ready for analysis
    """
    data = pd.read_csv(input_path, header=[0, 1], index_col=0)

    data.columns = [col[0] for col in data.columns]

    data.index = pd.to_datetime(data.index)
    data.index.name = "Date"

    missing = data.isnull().sum()
    print("Missing values per column:")
    print(missing)

    data = data.dropna(how="all")

    data.to_csv(output_path)
    print(f"\nCleaned data saved to {output_path}")
    print(f"Final shape: {data.shape[0]} rows, {data.shape[1]} columns")

    return data

if __name__ == "__main__":
    clean_corn_data()
    