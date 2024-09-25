import streamlit as st
import pandas as pd
import altair as alt

st.image("images/tritons_logo.png", width=100)  
st.title("UMSL Basketball Analytics")
st.write("2023-2024 Season")


# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/men/clean/23-24/seasonStats.csv")

seasonStats = load_data()

# Sidebar options
st.sidebar.header('Select Options')
# Limit Y-axis options to specific fields
y_axis_options = ['FG%', '3PT%','FT%','PPG','OREB',
    'DREB', 'REB', 'AVG REB', 'PF', 'A', 'TO', 'STL', 'BLK', 'eFG%', 'TS%', 'A/TO', 'Usage Rate', 'Box +/-']  # Specify only the fields you want
y_axis = st.sidebar.selectbox('Stat', y_axis_options)
x_axis = st.sidebar.selectbox('Per', ['Minutes Played', 'Games Played'])

# Create Altair scatter plot
scatter = alt.Chart(seasonStats).mark_circle(size=60).mark_point().encode(
    x=alt.X(x_axis, title=x_axis.capitalize()),
    y=alt.Y(y_axis, title=y_axis.capitalize()),
    tooltip=['Player', 'Number', x_axis, y_axis],
    color = 'Player'
).interactive()  # Enables zooming and panning

# Display plot
st.altair_chart(scatter, use_container_width=True)

# Additional details under the scatter plot
st.write(f"Details for the selected {y_axis} vs {x_axis}")

# Display filtered table based on user input
# Sort data by the selected Y-axis value
table_data = seasonStats[['Number', 'Player', x_axis, y_axis]].sort_values(by=y_axis, ascending=False)
st.dataframe(table_data, hide_index=True, use_container_width=True)

