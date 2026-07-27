import streamlit as st
import pandas as pd
import json
from datetime import date

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

# Load journal entries
with open("data/journal_entries.json", "r") as f:
    entries = json.load(f)

# Show only the most recent entry
if entries:
    latest = entries[-1]
    st.subheader(f"📅 {latest['date']}")
    st.write(f"**Close Price:** ${latest['close_price']} | **Change:** {latest['change']}")
    st.write(f"**My guess before checking news:** {latest['guess']}")
    st.write(f"**What actually happened:** {latest['actual']}")
    st.write(f"**Bullish factors:** {latest['bullish']}")
    st.write(f"**Bearish factors:** {latest['bearish']}")
    st.write(f"**My opinion:** {latest['opinion']}")
    st.write(f"**Confidence:** {latest['confidence']}/10")
else:
    st.info("No journal entries yet.")

st.divider()

# Form to add a new entry
with st.expander("➕ Add Today's Entry"):
    with st.form("new_entry_form"):
        entry_date = st.date_input("Date", value=date.today())
        close_price = st.text_input("Close Price ($)")
        change = st.text_input("Change (%)")
        guess = st.text_area("My guess before checking news")
        actual = st.text_area("What actually happened")
        bullish = st.text_area("Bullish factors")
        bearish = st.text_area("Bearish factors")
        opinion = st.text_area("My opinion - where does this go next?")
        confidence = st.slider("Confidence", 1, 10, 5)

        submitted = st.form_submit_button("Save Entry")

        if submitted:
            new_entry = {
                "date": str(entry_date),
                "close_price": close_price,
                "change": change,
                "guess": guess,
                "actual": actual,
                "bullish": bullish,
                "bearish": bearish,
                "opinion": opinion,
                "confidence": str(confidence)
            }
            entries.append(new_entry)
            with open("data/journal_entries.json", "w") as f:
                json.dump(entries, f, indent=2)
            st.success("Entry saved! Refresh to see it as the latest entry.")
