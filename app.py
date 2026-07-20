import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="My Portfolio", 
    page_icon="🚀", 
    layout="wide"
)

# --- CSS Styling (Professional Look) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3em; 
        background-color: #007BFF; 
        color: white; 
        font-weight: bold;
    }
    .card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px; 
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("Navigation")
    menu = ["Home", "About Me", "Projects", "Contact"]
    choice = st.sidebar.radio("Go to", menu)

# --- Sections ---

# Home
if choice == "Home":
    st.title("Welcome to My Portfolio! 🌟")
    st.subheader("Building solutions with code and creativity.")
    st.write("Yahan aap mere projects, skills aur professional journey explore kar sakte hain.")
    st.image("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800", use_column_width=True)

# About
elif choice == "About Me":
    st.header("About Me")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Main ek tech enthusiast hoon, jise nayi technology seekhna aur real-world problems ke liye solutions banana pasand hai.")
    with col2:
        st.write("**Technical Skills:**")
        st.write("- Python & Streamlit")
        st.write("- Data Analysis & Visualization")
        st.write("- Web Development")

# Projects
elif choice == "Projects":
    st.header("My Projects")
    
    # Project Card 1
    st.markdown('<div class="card"><h3>Tourism Data Dashboard</h3><p>Ek interactive dashboard jo data visualization use karta hai.</p></div>', unsafe_allow_html=True)
    
    # Project Card 2
    st.markdown('<div class="card"><h3>Portfolio Website</h3><p>Personal brand showcase ke liye built website.</p></div>', unsafe_allow_html=True)

# Contact
elif choice == "Contact":
    st.header("Get In Touch")
    st.write("Mujhse connect karne ke liye niche diya gaya form bharein.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if name and email:
                st.success(f"Thanks {name}! Aapka message mil gaya hai.")
            else:
                st.warning("Please apne name aur email fill karein.")
