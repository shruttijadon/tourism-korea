import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    .card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = ["Home", "About Me", "Projects", "Contact"]
choice = st.sidebar.radio("Go to", menu)

# Home Section
if choice == "Home":
    st.title("Welcome to My Portfolio! 🌟")
    st.write("### Hi, I'm a passionate developer!")
    st.write("Yahan aap mere work aur skills explore kar sakte hain.")
    st.image("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800", use_column_width=True)

# About Me Section
elif choice == "About Me":
    st.header("About Me")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Main ek tech enthusiast hoon jo creative solutions banana pasand karta hai.")
    with col2:
        st.write("Skills: Python, Streamlit, Machine Learning, Web Dev.")

# Projects Section
elif choice == "Projects":
    st.header("My Projects")
    st.markdown('<div class="card"><h3>Project 1: Data Dashboard</h3><p>Streamlit based dashboard.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Project 2: AI Bot</h3><p>ChatGPT powered chatbot.</p></div>', unsafe_allow_html=True)

# Contact Section
elif choice == "Contact":
    st.header("Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"Thanks {name}, I will get back to you soon!")
```eof

### Isse run kaise karein:
1. Apne computer mein Python install karein.
2. Terminal ya Command Prompt mein likhein: `pip install streamlit`
3. Upar diye gaye code ko `app.py` file mein save karein.
4. Terminal mein run karein: `streamlit run app.py`

Aapki website browser mein khul jayegi! Agar aapko design mein kuch aur change karwana ho (jaise colours ya naye sections), toh mujhe zaroor batayein.
