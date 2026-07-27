import streamlit as st
import json

st.set_page_config(page_title="Journal History", layout="wide")
st.title("📖 Journal History")

# Load all entries
with open("data/journal_entries.json", "r") as f:
    entries = json.load(f)

# Search bar
search_term = st.text_input("🔍 Search entries (searches all fields)")

# Filter entries based on search term
if search_term:
    filtered = [
        e for e in entries
        if search_term.lower() in json.dumps(e).lower()
    ]
else:
    filtered = entries

# Sort by date, most recent first
filtered = sorted(filtered, key=lambda e: e["date"], reverse=True)

st.write(f"Showing {len(filtered)} of {len(entries)} entries")

# Display each entry as a clickable, collapsible section
for entry in filtered:
    with st.expander(f"📅 {entry['date']}  —  ${entry['close_price']} ({entry['change']})"):
        st.write(f"**My guess before checking news:** {entry['guess']}")
        st.write(f"**What actually happened:** {entry['actual']}")
        st.write(f"**Bullish factors:** {entry['bullish']}")
        st.write(f"**Bearish factors:** {entry['bearish']}")
        st.write(f"**My opinion:** {entry['opinion']}")
        st.write(f"**Confidence:** {entry['confidence']}")