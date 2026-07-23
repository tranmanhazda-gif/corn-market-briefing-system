import streamlit as st
import pandas as pd

st.set_page_config(page_title="Corn Market Briefing System", layout="wide")

st.title("🌽 Corn Market Briefing System")
st.caption("Daily corn futures briefing for grain merchandisers")

# Load the processed data with indicators
data = pd.read_csv("data/processed/corn_futures_indicators.csv",
                    index_col="Date", parse_dates=True)

# Get the most recent row - "today's" numbers
latest = data.iloc[-1]
previous = data.iloc[-2]

st.header("Current Corn Futures")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Close Price",
    value=f"${latest['Close']:.2f}",
    delta=f"{latest['Daily_Return']:.2f}%"
)

col2.metric(
    label="Volume",
    value=f"{int(latest['Volume']):,}"
)

col3.metric(
    label="20-Day MA",
    value=f"${latest['MA_20']:.2f}"
)

col4.metric(
    label="50-Day MA",
    value=f"${latest['MA_50']:.2f}"
)

st.metric(
    label="100-Day MA",
    value=f"${latest['MA_100']:.2f}"
) 
st.header("Price Charts")

st.image("figures/price_moving_averages.png")
st.markdown("""
**What this tells a trader:** the relationship between price and its moving averages
signals trend direction and momentum. Price trading above a rising 50-day average
generally reflects an uptrend; a break below it can signal weakening momentum.
""")

st.image("figures/volume.png")
st.markdown("""
**What this tells a trader:** volume shows whether a price move has real conviction
behind it. A sharp price move on unusually low volume (like the most recent bar above)
is a signal to be cautious rather than assume the move will continue.
""")
st.header("USDA WASDE Tracker")

wasde = pd.read_csv("data/wasde_tracker.csv", parse_dates=["release_date"])
st.dataframe(wasde, use_container_width=True)

st.image("figures/wasde_ending_stocks.png")
st.markdown("""
**What this tells a trader:** tracking ending stocks across successive WASDE reports
shows whether USDA's supply/demand outlook is tightening or loosening over time.
A falling trend generally supports higher prices; a rising trend generally pressures
prices lower. A single report matters less than the direction of the trend.
""")
st.header("Market Summary")

with open("reports/market_summary.md", "r") as f:
    summary_content = f.read()
st.markdown(summary_content)

st.header("Market Journal")

with open("corn_market_journal.md", "r") as f:
    journal_content = f.read()
st.markdown(journal_content)
