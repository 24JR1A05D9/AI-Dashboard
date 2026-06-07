import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix AI Dashboard", layout="wide")

# Load data
df = pd.read_csv("netflix_titles.csv")

# Clean data
df.drop_duplicates(inplace=True)

# Title
st.title("🎬 Netflix AI Dashboard")

# ---------------- KPI SECTION ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", len(df))
col2.metric("Movies", (df['type'] == 'Movie').sum())
col3.metric("TV Shows", (df['type'] == 'TV Show').sum())
col4.metric("Countries", df['country'].nunique())

# ---------------- FILTERS ----------------
st.sidebar.header("🔍 Filters")

type_filter = st.sidebar.selectbox("Type", df['type'].dropna().unique())
country_filter = st.sidebar.selectbox("Country", df['country'].dropna().unique())

filtered_df = df[(df['type'] == type_filter) & (df['country'] == country_filter)]

# ---------------- DATA PREVIEW ----------------
st.subheader("📊 Filtered Data")
st.dataframe(filtered_df)

# ---------------- VISUALIZATION 1 ----------------
st.subheader("🎭 Content Type Distribution")
fig1 = px.pie(df, names='type', title="Movies vs TV Shows")
st.plotly_chart(fig1)

# ---------------- VISUALIZATION 2 ----------------
st.subheader("🌍 Top Countries")
top_countries = df['country'].value_counts().head(10).reset_index()
top_countries.columns = ['country', 'count']

fig2 = px.bar(top_countries, x='country', y='count')
st.plotly_chart(fig2)

# ---------------- VISUALIZATION 3 ----------------
st.subheader("📅 Releases Over Years")
year_data = df['release_year'].value_counts().sort_index().reset_index()
year_data.columns = ['year', 'count']

fig3 = px.line(year_data, x='year', y='count')
st.plotly_chart(fig3)

# ---------------- VISUALIZATION 4 ----------------
st.subheader("⭐ Ratings Distribution")
fig4 = px.histogram(df, x='rating')
st.plotly_chart(fig4)

# ---------------- VISUALIZATION 5 ----------------
st.subheader("🎬 Top Genres")
genre = df['listed_in'].value_counts().head(10).reset_index()
genre.columns = ['genre', 'count']

fig5 = px.bar(genre, x='genre', y='count')
st.plotly_chart(fig5)