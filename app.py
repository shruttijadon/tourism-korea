import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti Jadon | GKS Scholar Aspirant", 
    page_icon="🎓", 
    layout="wide"
)

# --- Aesthetic CSS (Professional Dark Theme) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #f1f5f9; }
    [data-testid="stSidebar"] { background-color: rgba(15, 23, 42, 0.9) !important; }
    
    .card {
        background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px;
    }
    h1, h2, h3 { color: #38bdf8 !important; }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #0f172a !important; color: white !important; border: 1px solid #334155 !important;
    }
    
    .footer { border-top: 1px solid #334155; padding-top: 20px; margin-top: 50px; color: #64748b; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Projects", "Research & Certifications", "GKS Journey", "Contact"]
    choice = st.radio("Go to", menu)

# --- HOME ---
if choice == "Home":
    st.title("Shruti Jadon")
    st.subheader("B.Tech Computer Science | Data Analytics | GKS 2028 Aspirant")
    st.markdown("---")
    st.write("A dedicated engineering student from India aiming to bridge the gap between data-driven innovation and human-centric policy design through the Global Korea Scholarship.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Current Academic Year", "3rd Year")
    c2.metric("Target Research", "M.Tech in AI")
    c3.metric("Goal Year", "2028")

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I?")
    st.write("I am an engineering student who believes that data is the key to solving modern socio-economic challenges. My professional approach combines technical rigor with the discipline I have cultivated as a trained dancer.")
    st.subheader("Vision for Korea")
    st.write("I am deeply interested in South Korea’s digital innovation ecosystem and aim to leverage my AI and data analytics background to contribute to Korea's smart city and policy-making initiatives.")

# --- SKILLS & PROJECTS ---
elif choice == "Skills & Projects":
    st.header("Technical Competencies")
    col1, col2 = st.columns(2)
    col1.write("✅ Python (Pandas, NumPy)\n✅ Data Visualization\n✅ Web Development (Streamlit)")
    col2.write("📌 Advanced SQL & Analytics\n📌 Machine Learning\n📌 Research Methodology")
    
    st.header("Selected Projects")
    st.markdown("""
    <div class="card"><h3>🌍 Tourism in Korea (2019-2024)</h3><p>Data-driven analysis of post-pandemic recovery trends.</p></div>
    <div class="card"><h3>💻 Tata Forge GenAI Analytics</h3><p>Predictive modeling for risk profiling and delinquency.</p></div>
    <div class="card"><h3>💻 Virtual Mentorship Bridge</h3><p>Platform design to enhance student-mentor connectivity.</p></div>
    """, unsafe_allow_html=True)

# --- RESEARCH & CERTIFICATIONS ---
elif choice == "Research & Certifications":
    st.header("Research & Achievements")
    st.info("📊 **Research Publication:** 'Data-Driven Traffic Incident Analysis and Risk Prediction for Smart City Mobility: A Case Study of Seoul Expressways'")
    st.markdown("""
    <div class="card"><h4>🎓 NPTEL Elite Certification</h4><p>Soft Skills and Personality Development (Score: 77%)</p></div>
    <div class="card"><h4>🏆 Symbiosis Skill Hackathon 2026</h4><p>National Level Participant (Team: Rebel Teachies)</p></div>
    """, unsafe_allow_html=True)

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Scholarship Roadmap (2028)")
    st.write("My application strategy focuses on demonstrating alignment between my research on Seoul's smart city mobility and South Korea’s future academic/technological goals.")
    st.success("Target: 9+ SGPA | Advanced ML Research | Strategic Networking")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch")
    col_left, col_right = st.columns([1, 1])
    with col_left:
        with st.form("contact"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            st.form_submit_button("Send Message")
    with col_right:
        st.write("📧 **Email:** shrutijadon1306@gmail.com")
        st.write("📍 **Location:** Indore, Madhya Pradesh, India")

    st.markdown('<div class="footer">© 2026 Shruti Jadon | Portfolio for GKS Scholarship Application</div>', unsafe_allow_html=True)
