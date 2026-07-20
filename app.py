import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti's Portfolio", 
    page_icon="🎓", 
    layout="wide"
)

# --- Aesthetic CSS Styling (The "Glassmorphism" Design) ---
st.markdown("""
    <style>
    /* Global Background - Dark Gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d242e 100%);
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(0,0,0,0.2) !important;
    }
    
    /* Glassmorphism Cards */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 182, 193, 0.2);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    .project-card:hover { transform: translateY(-5px); }
    
    /* Headings in Soft Pink */
    h1, h2, h3 { color: #ffb6c1 !important; }
    
    /* Buttons */
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
    st.markdown("""
    As a 3rd-year engineering student, I am deeply committed to exploring the intersection of **data analytics and human-centric design**. 
    My goal is to secure the GKS Scholarship to pursue an M.Tech in Data Science and AI in South Korea by 2028.
    """)
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Academic Year", "3rd Year")
    with col2: st.metric("Target Degree", "M.Tech AI")
    with col3: st.metric("Target Year", "2028")

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("I bridge the gap between complex data and real-world impact. By day, I am an engineering student dedicated to mastering data analytics and AI; by night, I am a trained dancer. This duality defines my professional approach.")
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("My Approach")
        st.write("I am currently transitioning my focus to **data-driven analytics**. My work is defined by a commitment to transforming raw data into actionable, human-centric solutions.")
    with col2:
        st.subheader("Why Korea? 🇰🇷")
        st.write("I am fascinated by Korea’s technological ecosystem and how the nation leverages big data to drive policy-making.")

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Roadmap 📈")
    c1, c2 = st.columns(2)
    c1.write("### ✅ Core Competencies\n- Python (Pandas, NumPy)\n- Data Visualization\n- Web Dev (Streamlit)")
    c2.write("### 📌 Strategic Roadmap\n- Advanced SQL\n- Machine Learning\n- Research Methods")

# --- PROJECTS ---
elif choice == "Projects":
    st.header("Projects & Leadership 🚀")
    st.markdown("""
    <div class="project-card"><h3>🌍 Tourism in Korea Analysis</h3><p>Analyzing post-pandemic recovery data using official Korean statistics.</p></div>
    <div class="project-card"><h3>💻 Tata Forge: GenAI Analytics</h3><p>Risk profiling, predictive modeling with AI, and data storytelling.</p></div>
    <div class="project-card"><h3>💻 Virtual Mentorship Bridge</h3><p>Platform connecting students with mentors, built during Symbiosis Hackathon.</p></div>
    """, unsafe_allow_html=True)

# --- CERTIFICATIONS & RESEARCH ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    st.info("📊 **Research Paper:** 'Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways'")
    st.markdown("""
    <div class="project-card"><h4>🎓 NPTEL Elite Certification</h4><p>Developing Soft Skills and Personality (Score: 77%)</p></div>
    <div class="project-card"><h4>🏆 Symbiosis Skill Hackathon 2026</h4><p>National Level Participant (Team: Rebel Teachies)</p></div>
    <div class="project-card"><h4>💼 Forage: GenAI Powered Data Analytics</h4><p>Completed practical job simulation in June 2026.</p></div>
    """, unsafe_allow_html=True)

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Journey (Target: 2028) 🎓")
    st.write("Focused on building a profile that bridges Indian academic research with South Korea’s digital innovation ecosystem.")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    with st.form("contact"):
        st.text_input("Your Name")
        st.text_input("Your Email")
        st.text_area("Your Message")
        if st.form_submit_button("Send Some Sunshine"):
            st.success("Message received!")
