import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Tourism Recovery Analysis",
    page_icon="✈️",
    layout="wide"
)

# App Title & Overview
st.title("✈️ Tourism Recovery Analysis")
st.markdown("""
This web application presents an interactive data analysis of post-pandemic tourism recovery trends. 
Explore the metrics, data distributions, and recovery insights through the sections below.
""")

# Sidebar Navigation
st.sidebar.header("Dashboard Controls")
option = st.sidebar.selectbox(
    "Select View",
    ["Overview & Summary", "Dataset Preview", "Recovery Trends Chart"]
)

# Dummy/Sample Data Simulation for Tourism Analysis (Replace with your actual data loading if available)
@st.cache_data
def load_data():
    np.random.seed(42)
    months = pd.date_range(start="2022-01-01", end="2025-12-01", freq="MS")
    data = pd.DataFrame({
        "Month": months,
        "Visitor_Arrivals": np.randint(10000, 50000, size=len(months)) + np.linspace(5000, 30000, len(months)),
        "Recovery_Rate_Percent": np.clip(np.linspace(40, 95, len(months)) + np.random.normal(0, 3, len(months)), 0, 100)
    })
    return data

df = load_data()

if option == "Overview & Summary":
    st.subheader("📊 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Peak Monthly Arrivals", value=f"{int(df['Visitor_Arrivals'].max()):,}")
    with col2:
        st.metric(label="Latest Recovery Rate", value=f"{df['Recovery_Rate_Percent'].iloc[-1]:.1f}%")
    with col3:
        st.metric(label="Total Tracked Months", value=len(df))
        
    st.markdown("---")
    st.write("### Executive Summary")
    st.p("""
    The analysis highlights a steady upward trajectory in visitor volume post-stabilization. 
    Through comparative modeling and seasonal decomposition, key recovery milestones have been mapped to evaluate sector resilience.
    """)

elif option == "Dataset Preview":
    st.subheader("📋 Raw Data Sample")
    st.dataframe(df.tail(12), use_container_width=True)

elif option == "Recovery Trends Chart":
    st.subheader("📈 Trend Visualization")
    st.line_chart(df.set_index("Month")[["Recovery_Rate_Percent"]])
    st.caption("Figure: Month-over-month recovery percentage progression.")
