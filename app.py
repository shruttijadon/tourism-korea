import streamlit as st
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

# --- CSS Styling ---
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
h1, h2, h3, h4 {
    color: #ffb6c1 !important;
}
div.stButton > button {
    background: linear-gradient(90deg, #ffb6c1, #a393eb);
    color: white;
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
        st.markdown("""
        <div class="project-card">
            <h3>Tap to know more about me</h3>
            <p>Explore my academic journey, skills, projects, and research work.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Hello, I'm Shruti ✨", key="home_open_btn"):
            st.session_state.home_open = True
            st.rerun()
    else:
        st.markdown("""
        As a **3rd-year B.Tech Computer Science student**, I am deeply committed to exploring the intersection of
        **data analytics, AI, and human-centered design**. My goal is to pursue an M.Tech in Data Science and AI in South Korea
        through the GKS Scholarship and build solutions that create real social impact.
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Academic Year", "3rd Year")
        with col2:
            st.metric("Target Degree", "M.Tech AI")
        with col3:
            st.metric("Target Year", "2028")

        if st.button("Hide intro", key="home_hide_btn"):
            st.session_state.home_open = False
            st.rerun()

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write(
        "I am Shruti Jadon, a third-year B.Tech Computer Science student with a strong interest in data analytics, AI, and smart city research. "
        "I enjoy transforming complex data into meaningful insights that can support better decisions and real-world solutions."
    )

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("My Approach")
        st.write(
            "I am currently focusing on building a strong foundation in data-driven analytics. "
            "My learning journey includes Python, visualization, research methods, and practical problem solving. "
            "I want to develop solutions that are not only technically strong but also useful for people."
        )
    with col2:
        st.subheader("Why Korea? 🇰🇷")
        st.write(
            "I am inspired by South Korea’s innovation ecosystem, smart city development, and strong academic environment. "
            "Through GKS, I want to grow in a research-focused setting and contribute to meaningful data science work."
        )

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Roadmap 📈")
    c1, c2 = st.columns(2)
    c1.write(
        "### ✅ Core Competencies\n"
        "- Python (Pandas, NumPy)\n"
        "- Data Visualization\n"
        "- Web Development (Streamlit)\n"
        "- Communication Skills\n"
        "- Power BI"
    )
    c2.write(
        "### 📌 Strategic Roadmap\n"
        "- Advanced SQL\n"
        "- Machine Learning\n"
        "- Research Methods\n"
        "- Data Storytelling\n"
        "- Dashboard Design"
    )

# --- PROJECTS ---
elif choice == "Projects":
    st.header("Projects & Leadership 🚀")
    st.write("Click on any project to see what I did, the tools I used, and the outcome of my work.")

    for title, data in projects.items():
        st.markdown(f"""
        <div class="project-card">
            <h3>{data["emoji"]} {title}</h3>
            <p>{data["short"]}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"View details: {title}", key=f"proj_{title}"):
            st.session_state.selected_project = title
            st.session_state.selected_certificate = None
            st.rerun()

    if st.session_state.selected_project:
        st.markdown("---")
        st.markdown("<div id='project-details'></div>", unsafe_allow_html=True)
        st.subheader(f"Details: {st.session_state.selected_project}")
        st.markdown(projects[st.session_state.selected_project]["detail"])

        html("""
        <script>
        setTimeout(function() {
            const el = window.parent.document.getElementById('project-details');
            if (el) el.scrollIntoView({behavior: 'smooth', block: 'start'});
        }, 150);
        </script>
        """, height=0)

        if st.button("Close project details", key="close_project"):
            st.session_state.selected_project = None
            st.rerun()

# --- CERTIFICATIONS & RESEARCH ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    st.info("📊 Research Paper: 'Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways'")
    st.write(
        "This section includes my research paper and certifications. The paper focuses on traffic incident analysis, hotspot detection, and seasonal trend study using Seoul expressway data."
    )

    st.markdown("### Research Paper")
    st.markdown("""
    <div class="project-card">
        <h3>📊 Research Paper</h3>
        <p>Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("View research paper details", key="research_btn"):
        st.session_state.selected_certificate = "Research Paper"
        st.session_state.selected_project = None
        st.rerun()

    st.markdown("---")
    st.markdown("### Certifications")
    for title in ["NPTEL Elite Certification", "Symbiosis Skill Hackathon 2026", "Forage: GenAI Powered Data Analytics"]:
        data = certificates[title]
        st.markdown(f"""
        <div class="project-card">
            <h3>{data["emoji"]} {title}</h3>
            <p>{data["short"]}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"View details: {title}", key=f"cert_{title}"):
            st.session_state.selected_certificate = title
            st.session_state.selected_project = None
            st.rerun()

    if st.session_state.selected_certificate:
        st.markdown("---")
        st.subheader(f"Details: {st.session_state.selected_certificate}")
        st.markdown(certificates[st.session_state.selected_certificate]["detail"])

        if st.button("Close certificate/research details", key="close_cert"):
            st.session_state.selected_certificate = None
            st.rerun()

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Journey (Target: 2028) 🎓")
    st.write(
        "I want to pursue the GKS Scholarship because it will help me study in a strong academic and research environment while building the skills needed for my future in Data Science and AI."
    )
    st.write(
        "My long-term goal is to use data science for smart city research, urban mobility, and social impact projects. Korea’s advanced digital ecosystem, research culture, and global outlook make it the right place for my higher studies."
    )
    st.write(
        "Through GKS, I hope to grow as a researcher, improve my technical and communication skills, and contribute to collaboration between India and South Korea."
    )

    st.markdown("#### Why I want GKS")
    st.write(
        "- To pursue higher studies in Data Science and AI.\n"
        "- To learn in a globally advanced academic environment.\n"
        "- To work on research that can solve real-world problems.\n"
        "- To build an international perspective and stronger career foundation."
    )

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    with st.form("contact"):
        st.text_input("Your Name")
        st.text_input("Your Email")
        st.text_area("Your Message")
        if st.form_submit_button("Send Some Sunshine"):
            st.success("Message received!")
