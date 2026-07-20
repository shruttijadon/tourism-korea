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
    .main { background-color: #f8f9fa; }
    .project-card {
        background-color: #ffffff; padding: 25px; border-left: 5px solid #003366;
        border-radius: 8px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Learning", "Projects", "Certifications & Research", "GKS Journey", "Contact"]
    choice = st.sidebar.radio("Go to", menu)

# --- HOME ---
if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech Computer Science | Data Enthusiast | GKS Aspirant")
    st.markdown("---")
    
    st.markdown("""
    ### 🎯 My Professional Vision
    As a 3rd-year engineering student, I am deeply committed to exploring the intersection of **data analytics and human-centric design**. 
    I believe in leveraging data to solve real-world problems and am currently channeling my academic and project work 
    toward a single-minded goal: **securing the GKS Scholarship to pursue an M.Tech in Data Science and AI at a 
    premier South Korean university by September 2028.**
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric(label="Academic Year", value="3rd Year")
    with col2: st.metric(label="Target Degree", value="M.Tech AI")
    with col3: st.metric(label="Target Year", value="2028")
        
    st.info("💡 Currently focusing on building data-driven projects that bridge technical innovation with policy impact.")

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")
    st.write("I bridge the gap between complex data and real-world impact. By day, I am an engineering student dedicated to mastering data analytics and AI; by night, I am a trained dancer. This duality defines my professional approach—I blend the analytical rigor of data science with the creative discipline I’ve cultivated through years of performance.")
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("My Approach")
        st.write("I am currently transitioning my focus from general computer science to **data-driven analytics and AI**. My work is defined by a commitment to transforming raw data into actionable, human-centric solutions.")
    with col2:
        st.subheader("Why Korea? 🇰🇷")
        st.write("I am fascinated by Korea’s technological ecosystem and how the nation leverages big data to drive policy-making and business growth. I am eager to contribute my technical skills to the next wave of global AI-driven innovation.")

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Strategic Roadmap 📈")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Core Competencies")
        st.write("✅ **Data Manipulation:** Python (Pandas, NumPy), Excel")
        st.write("✅ **Data Visualization:** Trend analysis, storytelling with data")
        st.write("✅ **Web Development:** Streamlit, basic UI/UX")
    
    with col2:
        st.subheader("Strategic Roadmap (2026-2028)")
        st.write("📌 **Advanced Analytics:** SQL for large-scale data")
        st.write("📌 **Machine Learning:** AI for socio-economic forecasting")
        st.write("📌 **Research Methods:** Academic foundations for grad studies")
    
    st.divider()
    st.info("**Core Focus:** Integrating technical proficiency with Korea-specific case studies to prepare for advanced graduate research.")

# --- PROJECTS ---
elif choice == "Projects":
    st.header("Projects & Leadership 🚀")
    
    st.markdown("""
    <div class="project-card">
    <h3>🌍 Tourism in Korea (2019-2024): A Data-Driven Analysis</h3>
    <p>Analyzing post-pandemic recovery data to understand shifts in consumer behavior using official Korean statistics.</p>
    </div>
    
    <div class="project-card">
    <h3>💻 Tata Forge: GenAI Powered Data Analytics</h3>
    <p><b>Focus:</b> Exploratory data analysis, risk profiling, predictive modeling with AI, and business intelligence reporting.</p>
    </div>
    
    <div class="project-card">
    <h3>💻 Virtual Mentorship Bridge</h3>
    <p><b>Role: Lead Developer</b><br>
    Designed a web-based platform to connect students with mentors, demonstrating a move from ideation to full deployment.</p>
    </div>
    
    <div class="project-card">
    <h3>🥗 Recipe Finder Website</h3>
    <p>A web application built using JavaScript and APIs to fetch live data for recipes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("👥 Academic Leadership")
    st.write("**Role: Class Representative (CR)** - Managing communication between faculty and students, honing essential leadership and organizational skills.")

# --- CERTIFICATIONS & RESEARCH (NEW SECTION) ---
elif choice == "Certifications & Research":
    st.header("Certifications & Research 📜")
    
    st.subheader("📝 Research Publication")
    st.info("📊 **Paper:** 'Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways'")
    
    st.subheader("🏅 Detailed Certifications")
    st.markdown("""
    <div class="project-card">
    <h4>🎓 NPTEL Elite Certification: Developing Soft Skills and Personality</h4>
    <p>Completed an intensive 8-week certification course (Aug-Oct 2025) focused on enhancing professional soft skills, communication, and personality development. Achieved a consolidated score of <b>77%</b> through assignments and proctored examinations conducted by IIT Kanpur.</p>
    </div>
    
    <div class="project-card">
    <h4>🏆 Symbiosis Skill Hackathon 2026: National Level Participation</h4>
    <p>Participated in a 36-hour national-level hackathon organized by the School of Computer Science and IT, Symbiosis University of Applied Sciences. Represented team <b>Rebel Teachies</b>, focused on rapid web development and innovative problem-solving.</p>
    </div>
    
    <div class="project-card">
    <h4>💼 Forage: GenAI Powered Data Analytics Job Simulation</h4>
    <p>Completed a comprehensive professional job simulation (June 2026) involving practical scenarios in exploratory data analysis, risk profiling, predictive modeling with AI, and business intelligence reporting, bridging the gap between technical competency and strategic decision-making.</p>
    </div>
    """, unsafe_allow_html=True)

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Scholarship Journey (Target: 2028) 🎓")
    
    st.info("**Core Vision:** Secure the GKS Scholarship to study how South Korea leverages data for socio-economic growth.")

    st.subheader("📍 Phase 1: Foundation (Current)")
    st.write("- Technical skill building (Python/Data Science).")
    st.write("- Deploying real-world projects.")
    
    st.subheader("⚙️ Phase 2: Specialization (Next 12 Months)")
    st.write("- Advanced ML and SQL focus.")
    st.write("- Researching professors and target universities in Korea.")
    
    st.subheader("🎓 Phase 3: Application (2027-2028)")
    st.write("- Finalizing GKS Personal Statement and Study Plan.")
    st.write("- Maintaining 9+ SGPA.")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    st.write("I am open to collaborations and discussions regarding Data Science and research opportunities.")
    if st.button("Email Me"):
        st.write("Email: shrutijadon1306@gmail.com")
