import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti Jadon | Portfolio",
    page_icon="🎓",
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    .project-card { background-color: #ffffff; padding: 20px; border-left: 5px solid #003366; border-radius: 8px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .tag-pill { display: inline-block; padding: 4px 10px; border-radius: 999px; background-color: #e7f1ff; color: #003366; font-size: 0.8rem; margin-right: 5px; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Projects", "Certifications & Research", "GKS Journey", "Contact"]
    choice = st.radio("Go to", menu)
    st.markdown("---")
    st.caption("Built for GKS 2028 Aspirations")

# --- HOME ---
if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech CSE Student | Data Analyst | GKS 2028 Aspirant")
    st.markdown("---")
    st.write("I am Shruti Jadon. Passionate about bridging data analytics, AI, and socio-economic research with a focus on South Korea’s digital innovation.")

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("Engineering student from Indore. I combine analytical rigor with creative problem solving.")

# --- SKILLS & PROJECTS ---
elif choice == "Skills & Projects":
    st.header("Skills & Projects 🚀")
    
    st.markdown("""
    <div class="project-card">
        <h3>💻 Tata Forge: GenAI Powered Data Analytics</h3>
        <p>Executed risk profiling, AI-based delinquency prediction, and strategic data storytelling.</p>
        <span class="tag-pill">GenAI</span><span class="tag-pill">Data Analytics</span><span class="tag-pill">Risk Modeling</span>
    </div>
    
    <div class="project-card">
        <h3>🥗 Recipe Finder Website</h3>
        <p>Built a responsive web application to search and discover recipes.</p>
        <span class="tag-pill">Web Development</span><span class="tag-pill">API Integration</span>
    </div>
    """, unsafe_allow_html=True)

# --- CERTIFICATIONS & RESEARCH ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    
    st.subheader("📝 Research Publication")
    st.info("Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways")
    
    st.subheader("🏅 Achievements & Certifications")
    st.write("- **NPTEL Elite Certification:** Developing Soft Skills and Personality (77%)")
    st.write("- **Symbiosis Skill Hackathon 2026:** National Level Participant (Team: Rebel Teachies)")
    st.write("- **Forage Job Simulation:** Tata Forge GenAI Powered Data Analytics")

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Journey (Target: 2028) 🎓")
    st.write("Aligning my research on Seoul's smart city mobility and AI skills to build a strong profile for the GKS scholarship.")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    st.write("📧 **Email:** shrutijadon1306@gmail.com")
    name = st.text_input("Your Name")
    msg = st.text_area("Message")
    if st.button("Send"):
        st.success("Message received!")
