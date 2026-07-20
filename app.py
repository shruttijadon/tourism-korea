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
    st.info("Goal: Secure GKS Scholarship for MTech in Data Science/AI at South Korean university (Sept 2028)")

elif choice == "About Me":
    st.header("Who Am I? 👋")
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.write("""
        **Shruti** - B.Tech Computer Science Student (3rd Year)
        
        I'm passionate about understanding how **data can drive decision-making** in real-world scenarios. 
        Currently transitioning my focus from general Korea projects to **data-driven analytics and AI**.
        
        **Why Korea?** I'm fascinated by Korea's technological advancement and how they've leveraged data 
        for policy-making and business growth, especially during the COVID-19 recovery.
        """)
    
    with col2:
        st.markdown("**Interest in Korea** 🇰")
        st.write("• Tech innovation & data culture")
        st.write("• Tourism recovery case study")
        st.write("• Future studies opportunity")

elif choice == "Skills & Learning":
    st.header("Technical Skills & Learning Path 📚")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Skills")
        st.write("✅ **Excel** - Data cleaning, basic charts")
        st.write("✅ **Python** - Basics, Pandas")
        st.write("✅ **Data Visualization** - Charts, trends analysis")
    
    with col2:
        st.subheader("Currently Learning & Planning")
        st.write("📌 **Online Courses (Planning to take):**")
        st.write("• AI & Machine Learning")
        st.write("• SQL for data analytics")
        st.write("• Advanced Data Visualization")
    
    st.markdown("---")
    st.info("Focus: Shifting from general Korea-focused projects to specialized Data Science and AI skills")

elif choice == "Projects":
    st.header("My Projects 🔧")
    
    st.markdown("### ✨ Featured Project")
    st.markdown("""
    <div class="project-card">
    <h3>🌍 Tourism in Korea (2019-2024): A Data-Driven Analysis</h3>
    <p><b>Subtitle:</b> Analyzing how foreign visitor numbers & Korea tourism trends changed during and after the pandemic, 
    using official Korean statistics</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Project Breakdown")
    
    with st.expander("Problem Question"):
        st.write("""
        How did the number of foreign visitors to Korea change from 2019 to 2024, 
        and what does this tell us about tourism recovery after COVID-19?
        """)
    
    with st.expander("Data Source"):
        st.write("""
        Official Korean Statistics from:
        - MCIT Tourism Data (Ministry of Culture, Sports & Tourism)
        - Annual foreign visitor numbers
        - Outbound Korean traveler statistics
        """)
    
    with st.expander("Tools Used"):
        st.write("""
        Excel - Data cleaning and basic charts
        Python (Pandas) - Advanced data processing
        Visualization - Line charts and bar charts
        """)
    
    with st.expander("Methodology"):
        st.write("""
        Step 1: Cleaned table of visitor numbers by year
        Step 2: Calculated year-on-year changes (percent increase/decrease)
        Step 3: Created line charts and bar charts to visualize trends
        """)
    
    with st.expander("Key Findings"):
        st.write("""
        Key Data Points:
        - Foreign visitor numbers dropped sharply in 2020 due to COVID-19
        - Tourism started recovering from post-COVID onwards
        - By 2020-24, impact reflected in pre-covid comparison
        - Pattern: Korean outbound travel mirrors inbound tourism trends
        - Shift observed: From outbound to inbound tourism post-pandemic
        """)
    
    st.markdown("---")
    st.markdown("### 🔜 Coming Soon")
    st.write("Korea Intra-Tourism Comparison - Analyzing domestic vs international tourism patterns")

elif choice == "GKS Journey":
    st.header("My GKS Scholarship Journey 🎓")
    
    st.write("""
    **Target:** Global Korea Scholarship (GKS) - MTech in Data Science/AI
    
    **Enrollment Goal:** September 2028
    """)
    
    st.subheader("Why GKS and South Korea?")
    st.write("""
    Academic Excellence - Aiming for 9+ SGPA by end of Semester 5 (Dec 2026)
    
    Data-Driven Research - Interested in R&D focusing on how data analytics can support 
    business policies and decision-making
    
    Korea Connection - My tourism data project demonstrates understanding of Korean statistics, 
    policy-making, and how data can drive economic recovery and growth
    
    Cultural Exchange - Keen to contribute to India-Korea collaboration in tech and research
    """)
    
    st.info("Current Focus: Semester 5 (Dec 2026) preparation to maintain 9+ SGPA for strong GKS profile")

elif choice == "Contact":
    st.header("Get In Touch 📬")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Connect With Me")
        st.write("Email: your.email@example.com")
        st.write("GitHub: github.com/yourprofile")
        st.write("LinkedIn: linkedin.com/in/yourprofile")
    
    with col2:
        st.subheader("Send Me a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            subject = st.selectbox("Subject", ["General Inquiry", "Project Collaboration", "GKS Discussion"])
            submit = st.form_submit_button("Send Message")
            
            if submit:
                if name and email and message:
                    st.success(f"Thank you, {name}! Your message has been received.")
                    st.info("I will get back to you soon!")
                else:
                    st.error("Please fill all fields before submitting.")
