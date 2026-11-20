
import streamlit as st
from rag_engine import ask_rag

st.set_page_config(
    page_title="Programming AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ==============================
# DESIGN
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ead5ff, #d6e9ff, #d5ffe6);
}

[data-testid="stSidebar"] {
    background-color: #f1e5ff;
}

.block-container {
    max-width: 1000px;
    margin: auto;
    padding-top: 2rem;
}

h1 {
    text-align: center;
    color: #7626a8;
}

.stButton > button {
    border-radius: 12px;
    border: 1px solid #c9a7f5;
    background-color: #ffffff;
    color: #7626a8;
    height: 45px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #e8d5ff;
    border-color: #9b59d0;
    color: #5e218a;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR NAVIGATION
# ==============================

st.sidebar.title("🤖 Programming AI")
st.sidebar.caption("Your Personal Coding Assistant")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Navigation")

if "page" not in st.session_state:
    st.session_state.page = "Chatbot"

if st.sidebar.button("💬 Chatbot", use_container_width=True):
    st.session_state.page = "Chatbot"

if st.sidebar.button("🔄 Pipeline", use_container_width=True):
    st.session_state.page = "Pipeline"

if st.sidebar.button("ℹ️ Info", use_container_width=True):
    st.session_state.page = "Info"

page = st.session_state.page

# ==============================
# CHATBOT
# ==============================

if page == "Chatbot":

    st.title("🌈 Programming AI Chatbot")

    st.markdown(
        "<h3 style='text-align:center;'>💻 Your Personal Coding Assistant</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Learn C, Java and Python step by step.</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    language = st.selectbox(
        "📚 Choose Programming Language",
        ["C", "Java", "Python"]
    )

    question = st.text_input(
        "💬 Ask your Question",
        placeholder="Explain loops in detail..."
    )

    if st.button("✨ Ask Chatbot", use_container_width=True):

        if question.strip():

            with st.spinner("🤖 Searching knowledge..."):
                answer = ask_rag(question, language)

            st.markdown("## 🤖 Chatbot Answer")
            st.markdown(answer)

        else:
            st.warning("Please enter your question.")

# ==============================
# PIPELINE
# ==============================

elif page == "Pipeline":

    st.title("🔄 Project Pipeline")

    st.markdown(
        "<h3 style='text-align:center;'>About the Project</h3>",
        unsafe_allow_html=True
    )

    st.write("""
    Programming AI Chatbot is an educational project designed
    to help students learn C, Java and Python programming.

    It provides programming knowledge, detailed explanations,
    coding examples and answers to programming questions.
    """)

    st.markdown("---")

    st.header("⚙️ How the Project Works")

    st.markdown("""
    **Step 1 — Select Language**

    Select C, Java or Python from the language menu.

    **Step 2 — Enter Question**

    Enter a programming question into the chatbot.

    **Step 3 — Knowledge Search**

    The system opens the selected language knowledge file.

    **Step 4 — Information Retrieval**

    The system searches for relevant programming information.

    **Step 5 — Answer Display**

    The retrieved information is displayed to the user.
    """)

    st.markdown("---")

    st.header("📂 Knowledge Files")

    st.markdown("""
    - 🧡 C Programming — `c.txt`
    - 💙 Java Programming — `java.txt`
    - 💚 Python Programming — `python.txt`
    """)

    st.header("🛠️ Technologies Used")

    st.markdown("""
    - Python
    - Streamlit
    - GitHub
    - Text-based knowledge retrieval
    """)

# ==============================
# INFO
# ==============================

elif page == "Info":

    st.title("ℹ️ Project Information")

    st.header("Programming AI Chatbot")

    st.write("""
    Programming AI Chatbot is a learning platform that helps
    users understand programming concepts and learn coding
    through questions and explanations.

    It supports C, Java and Python programming languages.
    """)

    st.markdown("---")

    st.header("🎯 Project Objective")

    st.write("""
    The main objective of this project is to make programming
    easier for beginners by providing a simple chatbot that
    offers programming explanations, knowledge and examples.
    """)

    st.header("👩‍💻 Team Members")

    st.markdown("""
    💜 Jyothi

    💙 Aishwarya

    💚 Chaithra B H

    🧡 Madava
    """)

    st.markdown("---")

    st.header("💻 Programming Languages")

    st.markdown("""
    🧡 C Programming

    💙 Java Programming

    💚 Python Programming
    """)

    st.header("🌟 Project Type")

    st.write("Educational AI Programming Assistant")
