import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Load the clean CSV file
df = pd.read_csv("../data/men/clean/23-24/player_stats.csv")

# Create a Streamlit app
st.title("UMSL Basketball Analytics")

# Add filters
opponent_filter = st.selectbox("Select Opponent", df["Opponent"].unique())
# Apply filters
df_filtered = df[df["Opponent"] == opponent_filter]

# Display filtered data
with st.expander("Player Stats Spreadsheet"):
    st.dataframe(df_filtered, hide_index=True)



df_filtered_sorted = df_filtered.sort_values(by="TS%", ascending=True)

# Create a horizontal bar chart for true shooting percentage
st.write("True Shooting Percentage:")
st.altair_chart(
    alt.Chart(df_filtered_sorted)
    .mark_bar()
    .encode(
        x="TS%",
        y=alt.Y("Player", sort="-x"),
        color="FGA"
    )
)

# Create a Scatterplot chart Box +/- vs. Minutes Played
st.write("Box +/- vs Minutes Played:")
st.altair_chart(
    alt.Chart(df_filtered_sorted)
    .mark_point()
    .encode(
        x="Box +/-",
        y="MIN",
        color="Player",
        tooltip=["Player", "Box +/-", "MIN"]
    )
)


