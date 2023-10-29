import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
#@st.cache
st.cache_data 
def load_data():
    df = pd.read_csv("vgsales.csv")
    return df

data = load_data()

# Title and introduction
st.title("Video Game Sales Dashboard")
st.write("Explore video game sales, ratings, and platforms using this interactive dashboard.")

# Display raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)

# Filter data by platform
platforms = data['Platform'].unique()
platform_filter = st.multiselect("Select platforms:", platforms, default=platforms)
filtered_data = data[data['Platform'].isin(platform_filter)]

# Bar chart for the top N games by global sales
st.subheader("Top N Games by Global Sales")
top_n = st.number_input("Select the top N games:", min_value=5, max_value=100, value=10, step=1)
top_games = filtered_data.nlargest(top_n, "Global_Sales")
fig = px.bar(top_games, x="Name", y="Global_Sales", color="Platform", hover_name="Name", text="Global_Sales")
st.plotly_chart(fig)

# Pie chart for platform market share
st.subheader("Platform Market Share")
platform_share = filtered_data.groupby("Platform")["Global_Sales"].sum().reset_index()
fig2 = px.pie(platform_share, names="Platform", values="Global_Sales", title="Platform Market Share")
st.plotly_chart(fig2)

# Scatter plot for Year vs. Global Sales
st.subheader("Year vs. Global Sales")
fig3 = px.scatter(filtered_data, x="Year", y="Global_Sales", color="Platform", hover_name="Name", opacity=0.6)
st.plotly_chart(fig3)
