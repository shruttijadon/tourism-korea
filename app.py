import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti's Portfolio",
    page_icon="🎓",
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .project-card {
        background-color: #ffffff;
        padding: 25px;
        border-left: 5px solid #003366;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .tag-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        background-color: #e7f1ff;
        color: #003366;
        font-size: 0.8rem;
        margin-right: 4px;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Learning", "Projects", "GKS Journey", "Contact"]
    choice = st.radio("Go to", menu)
    st.markdown("---")
    st.caption("Built with ❤️ in Indore\nby a future GKS scholar.")

# --- HOME ---
if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech Computer Science | Data & AI Enthusiast | GKS 2028 Aspirant")
    st.markdown("---")

    st.markdown("""
    ### 🎯 My Professional Vision
    As a 3rd-year engineering student from India, I 
