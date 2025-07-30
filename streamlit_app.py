import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("output.csv")

# 🎛 Sidebar filters
st.sidebar.header("Filters")

min_problems = st.sidebar.slider("Minimum Problems Solved", 0, int(df["total_problems_solved"].max()), 0)
min_score = st.sidebar.slider("Minimum Coding Score", 0, int(df["coding_score"].max()), 0)

# Theme Toggle in Sidebar
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

# Apply filters
filtered_df = df[(df["total_problems_solved"] >= min_problems) & (df["coding_score"] >= min_score)]

# Apply theme styling
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: #FAFAFA;
        }
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Title
st.title("GFG NIT Srinagar Student Dashboard")

# Subheader - Top Performers
st.subheader("Top Performers")
top_10 = filtered_df.sort_values(by="total_problems_solved", ascending=False).head(10)
st.dataframe(top_10)

# 🔍 Search by Handle
# 🔍 Search Bar with emoji in same line
col1, col2 = st.columns([0.05, 0.95])
with col1:
    st.markdown("### 🔍")
with col2:
    search_handle = st.text_input("", placeholder="Search by Handle")

if search_handle:
    filtered_df = filtered_df[filtered_df["handle"].str.contains(search_handle, case=False)]

# Subheader - Inactive Students
st.subheader("Inactive Students")
inactive = filtered_df[filtered_df["coding_score"] == 0]
st.write(f"Total inactive students: {len(inactive)}")
st.dataframe(inactive)

# Subheader - Score Distribution
st.subheader("Score Distribution")
filtered_df["total_score"] = (
    filtered_df["coding_score"]
    + filtered_df["total_problems_solved"]
    + filtered_df["potd_longest_streak"]
)
st.bar_chart(filtered_df["total_score"])

# 📥 Download Filtered Data
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(filtered_df)

st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_gfg_data.csv',
    mime='text/csv',
)
