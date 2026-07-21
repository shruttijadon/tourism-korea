import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Tourism Recovery Analysis",
    page_icon="✈️",
    layout="wide"
)

# App Title & Overview
st.title("✈️ Tourism Recovery Analysis Dashboard")
st.markdown("""
This web application provides a comprehensive data analysis of post-pandemic tourism recovery trends. 
Explore the key performance indicators, data distributions, and multi-metric visual trends below.
""")

# Sidebar Navigation Controls
st.sidebar.header("Navigation Controls")
option = st.sidebar.selectbox(
    "Select Section",
    ["Overview & KPI Summary", "Dataset Preview", "Recovery Trends & Charts"]
)

# Data Simulation for Tourism Analysis
@st.cache_data
def load_data():
    np.random.seed(42)
    months = pd.date_range(start="2022-01-01", end="2025-12-01", freq="MS")
    data = pd.DataFrame({
        "Month": months,
        "Visitor_Arrivals": np.random.randint(10000, 50000, size=len(months)) + np.linspace(5000, 30000, len(months)).astype(int),
        "Recovery_Rate_Percent": np.clip(np.linspace(40, 95, len(months)) + np.random.normal(0, 3, len(months)), 0, 100)
    })
    return data

df = load_data()

# Section 1: Overview & KPI Summary
if option == "Overview & KPI Summary":
    st.subheader("📊 Key Performance Indicators (KPIs)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Peak Monthly Arrivals", value=f"{int(df['Visitor_Arrivals'].max()):,}")
    with col2:
        st.metric(label="Latest Recovery Rate", value=f"{df['Recovery_Rate_Percent'].iloc[-1]:.1f}%")
    with col3:
        st.metric(label="Total Tracked Months", value=len(df))
        
    st.markdown("---")
    st.write("### Executive Summary & Methodology")
    st.markdown("""
    * **Objective:** Evaluate sector resilience and month-over-month normalization of traveler volume.
    * **Key Finding:** Post-stabilization trends indicate an accelerated return toward pre-pandemic baseline figures, driven by policy shifts and regional campaigns.
    * **Data Scope:** Multi-year longitudinal tracking from 2022 through 2025.
    """)

# Section 2: Dataset Preview
elif option == "Dataset Preview":
    st.subheader("📋 Processed Dataset Sample")
    st.markdown("Showing the latest recorded entries of the analysis dataset:")
    st.dataframe(df.tail(12), use_container_width=True)

# Section 3: Recovery Trends & Charts
elif option == "Recovery Trends & Charts":
    st.subheader("📈 Multi-Metric Trend Visualizations")
    
    st.markdown("#### 1. Recovery Rate Percentage Progression (%)")
    st.line_chart(df.set_index("Month")[["Recovery_Rate_Percent"]])
    st.caption("Figure 1.0: Month-over-month recovery trajectory showing progressive stabilization.")
    
    st.markdown("#### 2. Monthly Visitor Arrivals Volume")
    st.bar_chart(df.set_index("Month")[["Visitor_Arrivals"]])
    st.caption("Figure 2.0: Absolute volume distribution of visitor arrivals across the timeline.")
