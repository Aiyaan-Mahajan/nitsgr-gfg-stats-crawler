

import streamlit as st
import pandas as pd

# 🔗 Function to create clickable links
def make_clickable(handle, url):
    return f'<a href="{url}" target="_blank">{handle}</a>'

# 📄 Read CSV
df = pd.read_csv("output.csv")

st.title("GFG NIT Srinagar Student Dashboard")

# 🔝 Top Performers
st.subheader("Top Performers")
top_10 = df.sort_values(by="total_problems_solved", ascending=False).head(10)

# Create clickable handle column
top_10_display = top_10.copy()
top_10_display["handle"] = top_10_display.apply(lambda row: make_clickable(row["handle"], row["profile_url"]), axis=1)

# Show HTML table
st.write(top_10_display.to_html(escape=False, index=False), unsafe_allow_html=True)

# 💤 Inactive Students
st.subheader("Inactive Students")
inactive = df[df["coding_score"] == 0]

# Create clickable handle column
inactive_display = inactive.copy()
inactive_display["handle"] = inactive_display.apply(lambda row: make_clickable(row["handle"], row["profile_url"]), axis=1)

st.write(f"Total inactive students: {len(inactive_display)}")

# Show HTML table
st.write(inactive_display.to_html(escape=False, index=False), unsafe_allow_html=True)

# 📊 Score Distribution
st.subheader("Score Distribution")
df["total_score"] = df["coding_score"] + df["total_problems_solved"] + df["potd_longest_streak"]

st.bar_chart(df["total_score"])
