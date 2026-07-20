import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from streamlit.components.v1 import html

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti's Portfolio",
    page_icon="🎓",
    layout="wide"
)
 
# --- Session State ---
if "home_open" not in st.session_state:
    st.session_state.home_open = False
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None
if "selected_certificate" not in st.session_state:
    st.session_state.selected_certificate = None

# --- Data ---
projects = {
    "Tourism in Korea Analysis": {
        "emoji": "🌍",
        "short": "Analyzing post-pandemic recovery trends using official Korean tourism statistics.",
        "detail": """
### What I did
- Collected and studied tourism trend data related to Korea.
- Cleaned and organized the data for analysis.
- Identified recovery patterns after the pandemic.
- Created insights for understanding tourism growth and seasonality.

### Tools Used
- Python
- Pandas
- Data visualization libraries
- Streamlit

### Outcome
- Built a data-driven analysis of tourism recovery.
- Highlighted trend changes and key travel patterns.
- Strengthened my skills in exploratory data analysis and storytelling.
"""
    },
    "Tata Forge: GenAI Analytics": {
        "emoji": "💻",
        "short": "Risk profiling, predictive modeling, and data storytelling using AI-driven analytics.",
        "detail": """
### What I did
- Worked on understanding business data and identifying risk patterns.
- Used AI-based thinking to support analytics workflow.
- Built insights from structured data.
- Focused on data storytelling for decision-making.

### Tools Used
- Python
- Pandas
- Analytical reasoning
- Presentation and reporting tools

### Outcome
- Improved my understanding of AI-enabled analytics.
- Learned how to turn raw data into useful business insights.
- Strengthened my communication and problem-solving approach.
"""
    },
    "Virtual Mentorship Bridge": {
        "emoji": "🤝",
        "short": "A platform connecting students with mentors, built during the Symbiosis Hackathon.",
        "detail": """
### What I did
- Helped design a platform idea for student-mentor connection.
- Focused on solving a real student support problem.
- Contributed to the concept, planning, and presentation.
- Worked in a team environment with deadlines.

### Tools Used
- Hackathon workflow
- Team collaboration
- Presentation tools
- Problem-solving framework

### Outcome
- Built teamwork and leadership experience.
- Improved my ability to convert a social problem into a digital solution.
- Gained practical exposure to innovation and fast execution.
"""
    }
}

certificates = {
    "Research Paper": {
        "emoji": "📊",
        "short": "Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways",
        "detail": """
### Paper Title
Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways

### About the paper
- This research studies traffic incidents across major expressways in Seoul.
- It uses official Seoul Open Data to identify spatial and seasonal patterns.
- The analysis highlights high-risk corridors and time-based incident trends.
- It connects data analysis with smart city mobility planning.
"""
    },
    "NPTEL Elite Certification": {
        "emoji": "🎓",
        "short": "Developing Soft Skills and Personality (Score: 77%)",
        "detail": """
### Certification
NPTEL Elite Certification in Developing Soft Skills and Personality
"""
    },
    "Symbiosis Skill Hackathon 2026": {
        "emoji": "🏆",
        "short": "National-level participant, Team: Rebel Teachies",
        "detail": """
### Event
Symbiosis Skill Hackathon 2026
"""
    },
    "Forage: GenAI Powered Data Analytics": {
        "emoji": "💼",
        "short": "Completed a practical job simulation in June 2026.",
        "detail": """
### Program
Forage: GenAI Powered Data Analytics
"""
    }
}

# --- CSS Styling ---
st.markdown("""
<style>
/* Global text color set to white for visibility */
.stApp, p, div, span, label, li, h1, h2, h3, h4, .stRadio label {
    color: #ffffff !important;
}
.stApp {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d242e 100%);
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.3) !important;
}
.project-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 22px;
    border-radius: 20px;
    border: 1px solid rgba(255, 182, 193, 0.2);
    margin-bottom: 15px;
}
h1, h2, h3, h4 {
    color: #ffb6c1 !important;
}
div.stButton > button {
    background: linear-gradient(90deg, #ffb6c1, #a393eb);
    color: white !important;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Learning", "Projects", "Certifications & Research", "GKS Journey", "Contact"]
    choice = st.radio("Go to", menu)

# --- HOME ---
if choice == "Home":
    st.title("Hi there, I'm Shruti ✨")
    st.subheader("B.Tech Computer Science | Data Enthusiast | GKS Aspirant")
    st.markdown("---")

    if not st.session_state.home_open:
        st.markdown('<div class="project-card"><h3>Tap to know more about me</h3><p>Explore my academic journey, skills, projects, and research work.</p></div>', unsafe_allow_html=True)
        if st.button("Hello, I'm Shruti ✨", key="home_open_btn"):
            st.session_state.home_open = True
            st.rerun()
    else:
        st.markdown("As a **3rd-year B.Tech Computer Science student**, I am deeply committed to exploring the intersection of **data analytics, AI, and human-centered design**.")
        col1, col2, col3 = st.columns(3)
        col1.metric("Academic Year", "3rd Year")
        col2.metric("Target Degree", "M.Tech AI")
        col3.metric("Target Year", "2028")
        if st.button("Hide intro", key="home_hide_btn"):
            st.session_state.home_open = False
            st.rerun()

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("I am Shruti Jadon, a third-year B.Tech Computer Science student with a strong interest in data analytics, AI, and smart city research.")

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Roadmap 📈")
    c1, c2 = st.columns(2)
    c1.write("### ✅ Core Competencies\n- Python\n- Data Visualization\n- Web Development\n- Power BI")
    c2.write("### 📌 Strategic Roadmap\n- Machine Learning\n- Research Methods\n- Data Storytelling")

# --- PROJECTS ---
elif choice == "Projects":
    st.header("Projects & Leadership 🚀")
    for title, data in projects.items():
        st.markdown(f'<div class="project-card"><h3>{data["emoji"]} {title}</h3><p>{data["short"]}</p></div>', unsafe_allow_html=True)
        if st.button(f"View details: {title}", key=f"proj_{title}"):
            st.session_state.selected_project = title
            st.rerun()

    if st.session_state.selected_project:
        st.markdown("---")
        st.subheader(f"Details: {st.session_state.selected_project}")
        st.markdown(projects[st.session_state.selected_project]["detail"])
        
        if st.session_state.selected_project == "Tourism in Korea Analysis":
            st.write("#### South Korea Tourism Recovery (2020-2024)")
            data = {'Year': [2020, 2021, 2022, 2023, 2024], 'Inbound': [2500, 1000, 3200, 11000, 16500], 'Outbound': [500, 200, 700, 2300, 3000]}
            df = pd.DataFrame(data)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(df['Year'], df['Inbound'], marker='o', label='Inbound', color='#ffb6c1')
            ax.plot(df['Year'], df['Outbound'], marker='s', label='Outbound', color='#a393eb')
            ax.set_title('Tourism Recovery Trend', color='white')
            ax.tick_params(colors='white')
            ax.legend(facecolor='black', labelcolor='white')
            st.pyplot(fig)

        if st.button("Close project details", key="close_project"):
            st.session_state.selected_project = None
            st.rerun()

# --- CERTIFICATIONS & RESEARCH ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    for title in ["Research Paper", "NPTEL Elite Certification", "Symbiosis Skill Hackathon 2026", "Forage: GenAI Powered Data Analytics"]:
        if st.button(f"View: {title}", key=f"cert_{title}"):
            st.session_state.selected_certificate = title
            st.rerun()
    if st.session_state.selected_certificate:
        st.markdown(certificates[st.session_state.selected_certificate]["detail"])

# --- GKS JOURNEY & CONTACT ---
elif choice == "GKS Journey":
    st.header("My GKS Journey (Target: 2028) 🎓")
elif choice == "Contact":
    st.header("Get In Touch 📬")
