import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti's Portfolio", 
    page_icon="🚀", 
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3em; 
        background-color: #003366; color: white; font-weight: bold;
    }
    .card { 
        background-color: white; padding: 20px; border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; 
    }
    .project-card {
        background-color: #e8f4f8; padding: 25px; border-left: 5px solid #003366;
        border-radius: 8px; margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Projects", "Skills & Learning", "GKS Journey", "Contact"]
    choice = st.sidebar.radio("Go to", menu)

# --- SECTIONS ---

if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech Computer Science | Data Enthusiast | Korea Focused")
    st.write("3rd Year student exploring data analytics and its application in real-world decision-making.")
    st.write("")
    st.info("🎯 **Goal**: Secure GKS Scholarship for
