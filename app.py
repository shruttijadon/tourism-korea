import streamlit as st
import pandas as pd

# --- Page Setup: Configure the browser tab and layout ---
st.set_page_config(
    page_title="Shruti Jadon | Portfolio",
    page_icon="🎓",
    layout="wide"
)

# --- CSS Styling: Custom styles for a clean, professional look ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .project-card {
        background-color: #ffffff;
        padding: 20px;
        border-left: 5px solid #003366;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .tag-pill {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        background-color: #e7f1ff;
        color: #003366;
        font-size: 0.85rem;
        font-weight: bold;
        margin-right: 5px;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Navigation menu ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Projects", "Certifications & Research", "GKS Journey", "Contact"]
    choice = st.radio("Pages", menu)
    st.markdown("---")
    st.caption("Built with ❤️ in Indore\nBy Shruti Jadon")

# --- HOME SECTION ---
if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech Student | Data & AI Enthusiast | GKS 2028 Aspirant")
    st.markdown("---")
    st.write("""
    Hi! I'm Shruti. This portfolio is a snapshot of my engineering journey, my projects, 
    and my passion for bridging data analytics with human-centric design.
    """)

# --- ABOUT ME SECTION ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("""
    I am a Computer Science engineering student based in Indore. 
    - 💻 **By Day:** I am dedicated to mastering Data Analytics and AI.
    - 💃 **By Night:** I am a trained dancer, which helps me stay disciplined and confident.
    """)

# --- SKILLS & PROJECTS SECTION ---
elif choice == "Skills & Projects":
    st.header("Skills & Projects 🚀")
    
    st.subheader("🛠️ Technical Projects")
    st.markdown("""
    <div class="project-card">
        <h3>🌍 Tourism in Korea Analysis</h3>
        <p>Analyzed post-pandemic tourism recovery trends.</p>
        <span class="tag-pill">Python</span><span class="tag-pill">Pandas</span><span class="tag-pill">Data Vis</span>
    </div>
    
    <div class="project-card">
        <h3>💻 Tata Forge: GenAI Data Analytics</h3>
        <p>Executed risk profiling and AI-based delinquency prediction.</p>
        <span class="tag-pill">GenAI</span><span class="tag-pill">Analytics</span>
    </div>
    
    <div class="project-card">
        <h3>💻 Virtual Mentorship Bridge</h3>
        <p>A web platform to connect students with mentors.</p>
        <span class="tag-pill">Streamlit</span><span class="tag-pill">Web Dev</span>
    </div>
    """, unsafe_allow_html=True)

# --- CERTIFICATIONS & RESEARCH SECTION ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    
    st.info("📊 **Research Paper:** 'Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways'")
    
    st.subheader("🏅 Achievements & Certifications")
    st.write("- **NPTEL Elite Certification:** Developing Soft Skills and Personality (77%)")
    st.write("- **Symbiosis Skill Hackathon 2026:** National Level Participant (Team: Rebel Teachies)")
    st.write("- **Forage Job Simulation:** Tata Forge GenAI Analytics")

# --- GKS JOURNEY SECTION ---
elif choice == "GKS Journey":
    st.header("My GKS Journey (Target: 2028) 🎓")
    st.write("My goal is to pursue my Master's in Korea, focusing on how AI and data-driven systems can solve socio-economic challenges.")

# --- CONTACT SECTION ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    st.write("Feel free to reach out via email: **shrutijadon1306@gmail.com**")
    
    with st.form("contact_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your Email")
        msg = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")
        if submit:
            st.success("Thank you! I will get back to you soon.")
