import streamlit as st

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

### What I worked on
- Data collection from official open data sources.
- Data cleaning and preprocessing.
- Exploratory analysis of incident patterns.
- Visualization of traffic trends and hotspot behavior.

### Tools Used
- Python
- Pandas
- Data visualization
- Statistical analysis
- Research writing

### Key Findings
- Certain expressways showed higher incident concentration.
- Monthly and seasonal changes affected incident frequency.
- The study supports proactive city planning and better traffic risk prediction.

### Why it matters
This paper reflects my interest in using data science to solve real urban problems and improve smart city mobility.
"""
    },
    "NPTEL Elite Certification": {
        "emoji": "🎓",
        "short": "Developing Soft Skills and Personality (Score: 77%)",
        "detail": """
### Certification
NPTEL Elite Certification in Developing Soft Skills and Personality

### What I learned
- Communication basics
- Professional behavior
- Confidence building
- Team interaction and personal development

### Why it matters
This certification strengthened my communication and presentation abilities, which are important for both academics and research.
"""
    },
    "Symbiosis Skill Hackathon 2026": {
        "emoji": "🏆",
        "short": "National-level participant, Team: Rebel Teachies",
        "detail": """
### Event
Symbiosis Skill Hackathon 2026

### My role
- National-level participant
- Team member of Rebel Teachies
- Contributed to idea development and problem solving

### Skills gained
- Teamwork
- Fast thinking
- Innovation
- Practical solution building

### Why it matters
This experience taught me how to work under pressure while building meaningful ideas with a team.
"""
    },
    "Forage: GenAI Powered Data Analytics": {
        "emoji": "💼",
        "short": "Completed a practical job simulation in June 2026.",
        "detail": """
### Program
Forage: GenAI Powered Data Analytics

### What I did
- Completed a practical analytics simulation.
- Explored how generative AI supports data workflows.
- Practiced analysis and decision-making in a professional context.

### Tools / Exposure
- Data analytics workflow
- AI-driven insight generation
- Business problem solving

### Why it matters
It gave me industry-style exposure and improved my confidence in working with modern analytics tools.
"""
    }
}

# --- CSS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d242e 100%);
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.2) !important;
}
.project-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 22px;
    border-radius: 20px;
    border: 1px solid rgba(255, 182, 193, 0.2);
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease, border 0.3s ease;
}
.project-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(255, 182, 193, 0.5);
}
.project-card.active {
    border: 2px solid #ffb6c1;
    background: rgba(255, 182, 193, 0.10);
}
.detail-panel {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,182,193,0.25);
    border-radius: 22px;
    padding: 24px;
    backdrop-filter: blur(14px);
    min-height: 520px;
}
.small-muted {
    color: #c9c9c9;
    font-size: 0.95rem;
}
h1, h2, h3, h4 {
    color: #ffb6c1 !important;
}
div.stButton > button {
    background: linear-gradient(90deg, #ffb6c1, #ff9aa2);
    color: white;
    border: none;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
