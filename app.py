import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="Shruti's Portfolio",
    page_icon="🎓",
    layout="wide"
)

# --- Session State ---
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None
if "selected_certificate" not in st.session_state:
    st.session_state.selected_certificate = None

# --- Data ---
projects = {
    "Tourism in Korea Analysis": {
        "emoji": "🌍",
        "detail": "### What I did\n- Collected and studied tourism trend data.\n- Identified recovery patterns.\n### Tools Used\n- Python, Pandas, Streamlit"
    },
    "Tata Forge: GenAI Analytics": {
        "emoji": "💻",
        "detail": "### What I did\n- Risk profiling and predictive modeling.\n- Focused on data storytelling."
    }
}

certificates = {
    "Research Paper": {
        "emoji": "📊",
        "detail": "### Research\n- Traffic Incident Analysis for Seoul Expressways.\n- Used Python for data visualization and cleaning."
    }
}

# --- CSS ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #1a1a1a 0%, #2d242e 100%); color: #e0e0e0; }
h1, h2, h3 { color: #ffb6c1 !important; }
div.stButton > button { background: linear-gradient(90deg, #ffb6c1, #ff9aa2); color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- Main App Display ---
st.title("🎓 Shruti's Portfolio")

tab1, tab2 = st.tabs(["Projects", "Certificates"])

with tab1:
    st.subheader("My Projects")
    for name, info in projects.items():
        if st.button(f"{info['emoji']} {name}", key=name):
            st.session_state.selected_project = name
    
    if st.session_state.selected_project:
        st.markdown("---")
        st.subheader(st.session_state.selected_project)
        st.markdown(projects[st.session_state.selected_project]['detail'])

with tab2:
    st.subheader("My Certificates")
    for name, info in certificates.items():
        if st.button(f"{info['emoji']} {name}", key=f"cert_{name}"):
            st.session_state.selected_certificate = name
            
    if st.session_state.selected_certificate:
        st.markdown("---")
        st.subheader(st.session_state.selected_certificate)
        st.markdown(certificates[st.session_state.selected_certificate]['detail'])
