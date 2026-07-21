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

# --- Data: Projects ---
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

# --- Data: Certifications & Research ---
certificates = {
    "Research Paper": {
        "emoji": "📊",
        "short": "Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways",
        "detail": """
### Research Focus & Overview
- **Title:** Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways
- **Core Objective:** Investigates traffic incidents across major expressways in Seoul utilizing official Seoul Open Data to uncover spatial and seasonal behavioral patterns.
- **Methodology & Impact:** Employs predictive analytics to pinpoint high-ranking risk corridors and time-based incident trends, directly bridging raw data processing with smart city mobility planning and intelligent transportation frameworks.
"""
    },
    "NPTEL Elite Certification": {
        "emoji": "🎓",
        "short": "Developing Soft Skills and Personality (Score: 77% - Elite)",
        "detail": """
### Certification Details
- **Program:** NPTEL Elite Certification in Developing Soft Skills and Personality
- **Performance:** Achieved an Elite score of 77%.
- **Value:** Highlights strong professional communication, collaborative capability, and interpersonal competencies suited for rigorous international academic and research environments.
"""
    },
    "Symbiosis Skill Hackathon 2026": {
        "emoji": "🏆",
        "short": "National-level participant, Team: Rebel Teachies",
        "detail": """
### Event Summary
- **Hackathon:** Symbiosis Skill Hackathon 2026
- **Team:** Rebel Teachies
- **Contribution:** Engaged in high-pressure, rapid-execution software prototyping, translating complex user requirements into practical digital solutions like the Virtual Mentorship Bridge under strict deadlines.
"""
    },
    "Forage: GenAI Powered Data Analytics": {
        "emoji": "💼",
        "short": "Completed a practical job simulation in June 2026 focusing on GenAI analytics.",
        "detail": """
### Simulation Scope
- **Program:** Forage GenAI Powered Data Analytics Job Simulation
- **Key Focus:** Applied generative AI tools and structured workflows to business risk profiling, data storytelling, and advanced predictive modeling simulations.
- **Outcome:** Strengthened capabilities in converting unstructured data inputs into practical, actionable analytical decisions.
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
    menu = ["Home", "About Me", "Skills & Learning", "Projects", "Certifications & Research", "KGKS Journey", "Contact"]
    choice = st.radio("Go to", menu)

# --- HOME ---
if choice == "Home":
    st.title("Hi there, I'm Shruti ✨")
    st.subheader("B.Tech Computer Science | Machine Learning & AI | KGKS Aspirant")
    st.markdown("---")

    if not st.session_state.home_open:
        st.markdown('<div class="project-card"><h3>Tap to know more about me</h3><p>Explore my academic journey, core machine learning skills, projects, and research work.</p></div>', unsafe_allow_html=True)
        if st.button("Hello, I'm Shruti ✨", key="home_open_btn"):
            st.session_state.home_open = True
            st.rerun()
    else:
        st.markdown("As a **3rd-year B.Tech Computer Science student**, I am deeply focused on **Machine Learning, Deep Learning, and AI Convergence Engineering** to build intelligent data-driven systems.")
        col1, col2, col3 = st.columns(3)
        col1.metric("Academic Year", "3rd Year")
        col2.metric("Target Degree", "M.Tech AI & Convergence")
        col3.metric("Target Year", "2028")
        if st.button("Hide intro", key="home_hide_btn"):
            st.session_state.home_open = False
            st.rerun()

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("I am a 3rd-year B.Tech Computer Science student with a core focus on Machine Learning, Deep Learning, and AI Convergence Engineering. My technical expertise lies in building predictive models, time-series forecasting, and robust neural networks using Python and PyTorch. Driven by a passion for advanced research and intelligent systems, I am actively preparing for my M.Tech research journey via the KGKS scholarship track.")

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Roadmap 📈")
    c1, c2 = st.columns(2)
    c1.write("### ✅ Core Competencies\n- Python, PyTorch, Scikit-Learn\n- Predictive Modeling & Time-Series\n- Data Preprocessing & Regularization\n- Streamlit Deployment & Git")
    c2.write("### 📌 Strategic Research Roadmap\n- Deep Neural Networks & Computer Vision\n- Smart City Mobility & Incident Prediction\n- Advanced Research Methodologies")

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
            fig.patch.set_facecolor('none')
            ax.set_facecolor('none')
            ax.plot(df['Year'], df['Inbound'], marker='o', label='Inbound', color='#ffb6c1')
            ax.plot(df['Year'], df['Outbound'], marker='s', label='Outbound', color='#a393eb')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.set_xlabel('Year', color='white')
            ax.set_ylabel('Visitors', color='white')
            ax.set_title('Tourism Recovery Trend', color='white')
            ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
            ax.grid(True, color='white', linestyle='--', alpha=0.3)
            st.pyplot(fig)

        if st.button("Close project details", key="close_project"):
            st.session_state.selected_project = None
            st.rerun()

# --- CERTIFICATIONS & RESEARCH ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    for title, data in certificates.items():
        st.markdown(f'<div class="project-card"><h3>{data["emoji"]} {title}</h3><p>{data["short"]}</p></div>', unsafe_allow_html=True)
        if st.button(f"View details: {title}", key=f"cert_btn_{title}"):
            st.session_state.selected_certificate = title
            st.rerun()

    if st.session_state.selected_certificate:
        st.markdown("---")
        st.subheader(f"Details: {st.session_state.selected_certificate}")
        st.markdown(certificates[st.session_state.selected_certificate]["detail"])
        if st.button("Close certificate details", key="close_cert"):
            st.session_state.selected_certificate = None
            st.rerun()

# --- KGKS JOURNEY ---
elif choice == "KGKS Journey":
    st.header("My KGKS Journey (Target: 2028) 🎓")
    st.write("Targeting an M.Tech admission in Computer & AI Convergence Engineering at KIT via the KGKS scholarship, backed by targeted machine learning research and proactive faculty collaboration.")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    st.write("Feel free to reach out for machine learning research collaborations, technical discussions, or professional networking!")
