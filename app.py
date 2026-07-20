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
    .main {
        background-color: #f8f9fa;
    }
    .project-card {
        background-color: #ffffff;
        padding: 25px;
        border-left: 5px solid #003366;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .tag-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        background-color: #e7f1ff;
        color: #003366;
        font-size: 0.8rem;
        margin-right: 4px;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("📍 Navigation")
    menu = ["Home", "About Me", "Skills & Learning", "Projects", "GKS Journey", "Contact"]
    choice = st.radio("Go to", menu)
    st.markdown("---")
    st.caption("Built with ❤️ in Indore\nby a future GKS scholar.")

# --- HOME ---
if choice == "Home":
    st.title("Welcome to My Portfolio 🌟")
    st.subheader("B.Tech Computer Science | Data & AI Enthusiast | GKS 2028 Aspirant")
    st.markdown("---")

    st.markdown("""
    ### 🎯 My Professional Vision
    As a 3rd-year engineering student from India, I am committed to exploring the intersection of **data analytics and human-centric design**.  
    I aim to leverage data to solve real-world socio-economic problems, particularly in the context of Korea’s digital innovation and policy ecosystem.  
    My current academic, project, and leadership work are aligned toward one goal: **securing the Global Korea Scholarship (GKS) to pursue an M.Tech / M.S. in Data Science and AI at a premier South Korean university by September 2028.**
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Academic Year", value="3rd Year")
    with col2:
        st.metric(label="Target Degree", value="M.Tech / M.S. in AI")
    with col3:
        st.metric(label="Target Year", value="2028 (GKS)")

    st.info(
        "💡 Current focus: Building data-driven projects that connect technical innovation with policy and societal impact, "
        "with a specific interest in Korea’s post-pandemic recovery and digital economy."
    )

# --- ABOUT ME ---
elif choice == "About Me":
    st.header("Who Am I? 👋")

    st.write(
        "I am Shruti Jadon, a Computer Science engineering student from Indore, India, who loves bridging the gap "
        "between complex data and real-world impact. By day, I am an engineering student dedicated to mastering data "
        "analytics and AI; by night, I am a trained dancer. This duality defines my professional approach—I blend the "
        "analytical rigor of data science with the creative discipline and stage confidence I’ve cultivated through years of performance."
    )

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.subheader("My Approach")
        st.write(
            "I am transitioning my focus from general computer science to **data-driven analytics and AI**. "
            "My work is defined by a commitment to transforming raw data into actionable, human-centric solutions—"
            "whether that means understanding tourism trends, improving student–mentor access, or exploring socio-economic datasets."
        )
        st.write(
            "- I enjoy designing clean, interpretable dashboards rather than just writing code.\n"
            "- I like connecting statistics with stories about people, policy, and culture.\n"
            "- I am comfortable taking responsibility and representing teams in front of faculty and peers."
        )

    with col2:
        st.subheader("Why Korea? 🇰🇷")
        st.write(
            "Korea inspires me as a country that combines rapid technological growth with strong public digital infrastructure. "
            "I am particularly fascinated by how Korea uses big data for tourism recovery, smart cities, and social policy. "
            "Through the GKS scholarship, I hope to learn from this ecosystem and contribute to the next wave of global AI-driven innovation "
            "linking India and Korea."
        )

    st.markdown("#### Snapshot of Me in Three Words")
    cols = st.columns(3)
    with cols[0]:
        st.success("Data-driven")
    with cols[1]:
        st.info("People-oriented")
    with cols[2]:
        st.warning("Korea-focused")

# --- SKILLS & LEARNING ---
elif choice == "Skills & Learning":
    st.header("Technical Skills & Strategic Roadmap 📈")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Core Competencies")
        st.write("✅ **Programming & Data Manipulation:** Python (Pandas, NumPy), basic data cleaning and preprocessing")
        st.write("✅ **Data Visualization:** Trend analysis, storytelling with data using plots, charts, and dashboards")
        st.write("✅ **Web Development:** Streamlit apps, basic HTML/CSS, simple UI/UX thinking")
        st.write("✅ **Team & Leadership:** Class Representative experience, organizing communication and small initiatives")

        st.markdown("**Current Learning Focus:**")
        st.write("- Improving my Python for data analysis and EDA.")
        st.write("- Practicing end-to-end mini projects (data collection → cleaning → visualization → insights).")

    with col2:
        st.subheader("Strategic Roadmap (2026–2028)")
        st.write("📌 **Advanced Analytics:** SQL for large-scale data and relational databases")
        st.write("📌 **Machine Learning:** Supervised and unsupervised models for socio-economic and tourism forecasting")
        st.write("📌 **Research Methods:** Academic writing, literature review, and Korea-focused case studies")
        st.write("📌 **Global Preparation:** Understanding GKS requirements, shortlisting Korean universities, and exploring professors’ research areas")

        st.markdown("**Milestones I am Targeting:**")
        st.write("- Complete at least 3 Korea-related data projects by mid-2027.")
        st.write("- Maintain 9+ SGPA and strengthen my academic profile.")
        st.write("- Build a portfolio of projects that clearly align with my proposed study plan for GKS.")

    st.divider()
    st.info(
        "**Core Focus:** Integrating technical proficiency with Korea-specific case studies so that my future graduate research proposal is not abstract, but based on concrete work I have already started."
    )

# --- PROJECTS ---
elif choice == "Projects":
    st.header("Projects & Leadership 🚀")

    st.markdown("""
    <div class="project-card">
        <h3>🌍 Tourism in Korea (2019–2024): A Data-Driven Analysis</h3>
        <p><b>Goal:</b> Analyze post-pandemic recovery trends in Korean tourism using official statistics and open data.</p>
        <p><b>What I did:</b> Collected multi-year data, cleaned and structured it in Python, and visualized changes in inbound tourism, seasonal patterns, and recovery pace after COVID-19.</p>
        <p><b>Why it matters for GKS:</b> This project connects directly to Korea’s economy and policy, showing how data science can support evidence-based decision-making for tourism and public planning.</p>
        <span class="tag-pill">Python</span>
        <span class="tag-pill">Pandas</span>
        <span class="tag-pill">Data Visualization</span>
        <span class="tag-pill">Korea Focus</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>💻 Virtual Mentorship Bridge</h3>
        <p><b>Role:</b> Lead Developer</p>
        <p><b>Overview:</b> Designed a web-based platform to connect students with mentors, taking the idea from concept to deployment.</p>
        <p><b>Impact:</b> The project demonstrates my ability to identify a problem in the student community, design a solution, and coordinate its implementation — skills that are essential for contributing to international academic environments.</p>
        <span class="tag-pill">Streamlit</span>
        <span class="tag-pill">Product Thinking</span>
        <span class="tag-pill">Leadership</span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👥 Academic Leadership")
    st.write(
        "**Role: Class Representative (CR)** – I coordinate communication between faculty and students, collect feedback, and help ensure smooth execution of academic activities. "
        "This role has strengthened my leadership, responsibility, and conflict-resolution skills—qualities I intend to carry into my life as an international student in Korea."
    )

# --- GKS JOURNEY ---
elif choice == "GKS Journey":
    st.header("My GKS Scholarship Journey (Target: 2028) 🎓")

    st.info(
        "**Core Vision:** Secure the Global Korea Scholarship to study how South Korea leverages data and AI for socio-economic growth, "
        "and then apply these learnings to build stronger data-driven systems between India and Korea."
    )

    st.subheader("📍 Phase 1: Foundation (Current)")
    st.write("- Strengthening fundamentals in Python, statistics, and data science.")
    st.write("- Building small but meaningful, deployable projects (like this portfolio) to practice end-to-end execution.")
    st.write("- Actively documenting my work so it can support my future Personal Statement and Study Plan.")

    st.subheader("⚙️ Phase 2: Specialization (Next 12–18 Months)")
    st.write("- Focusing on advanced ML, SQL, and domain-specific applications (tourism, public policy, education).")
    st.write("- Researching professors and target universities in Korea whose work aligns with data-driven socio-economic analysis.")
    st.write("- Starting drafts of my GKS Personal Statement and Study Plan, aligned with my projects and academic profile.")

    st.subheader("🎓 Phase 3: Application (2027–2028)")
    st.write("- Finalizing a coherent narrative that connects my background, projects, and Korea-focused goals.")
    st.write("- Maintaining 9+ SGPA and strengthening my recommendation portfolio.")
    st.write("- Submitting a strong GKS application that shows consistent effort from 3rd year until the application year.")

# --- CONTACT ---
elif choice == "Contact":
    st.header("Get In Touch 📬")
    st.write(
        "I am open to collaborations, data science internships, and research opportunities related to AI, data analytics, "
        "and Korea-focused socio-economic studies."
    )

    st.subheader("Email")
    st.write("📧 You can reach me at: **shrutijadon1306@gmail.com**")

    st.subheader("Quick Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Thank you for reaching out! I will get back to you as soon as possible.")
        else:
            st.error("Please fill in all the fields before submitting.")
