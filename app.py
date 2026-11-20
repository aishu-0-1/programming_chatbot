
import streamlit as st
from rag_engine import ask_rag

st.set_page_config(
    page_title="Programming AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ============================
# DESIGN
# ============================

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
    background-color: #ffffff;
    color: #7626a8;
    border: 1px solid #c9a7f5;
    height: 45px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #e8d5ff;
    color: #5e218a;
}

</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR
# ============================

st.sidebar.title("🤖 Programming AI")
st.sidebar.caption("Your Personal Coding Assistant")
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Menu")

if "page" not in st.session_state:
    st.session_state.page = "Chatbot"

if st.sidebar.button("🔄 Pipeline", use_container_width=True):
    st.session_state.page = "Pipeline"

if st.sidebar.button("ℹ️ Info", use_container_width=True):
    st.session_state.page = "Info"

if st.sidebar.button("💬 Back to Chatbot", use_container_width=True):
    st.session_state.page = "Chatbot"

page = st.session_state.page

# ============================
# MAIN CHATBOT
# ============================

if page == "Chatbot":

    st.title("🌈 Programming AI Chatbot")

    st.markdown(
        "<h3 style='text-align:center;'>💻 Your Personal Coding Assistant</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Ask questions and learn programming step by step.</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    language = st.selectbox(
        "📚 Choose Programming Language",
        ["C", "Java", "Python"]
    )

    question = st.text_input(
        "💬 Ask your question",
        placeholder="For example: Explain loops in Python..."
    )

    if st.button("✨ Ask Chatbot", use_container_width=True):

        if question.strip():

            with st.spinner("🤖 Searching knowledge..."):
                answer = ask_rag(question, language)

            st.markdown("### 🤖 Answer")
            st.write(answer)

        else:
            st.warning("Please enter your question.")

# ============================
# PIPELINE
# ============================

elif page == "Pipeline":

    st.title("🔄 Project Pipeline")

    st.header("📖 About the Project")

    st.write("""
    Programming AI Chatbot is an educational project designed
    to help students learn C, Java and Python programming.

    Users select a programming language, enter their questions,
    and receive answers based on programming knowledge.
    """)

    st.markdown("---")

    st.subheader("⚙️ How It Works")

    st.markdown("""
    **Step 1 — Select Language**

    Select C, Java or Python.

    **Step 2 — Enter Question**

    Enter a programming question into the chatbot.

    **Step 3 — Knowledge Search**

    The chatbot reads the selected programming knowledge file.

    **Step 4 — Retrieve Information**

    Relevant information is selected based on the question.

    **Step 5 — Display Answer**

    The chatbot displays the retrieved answer.
    """)

    st.subheader("📂 Knowledge Files")

    st.markdown("""
    - 🧡 C — `c.txt`
    - 💙 Java — `java.txt`
    - 💚 Python — `python.txt`
    """)

    st.subheader("🛠️ Technologies Used")

    st.markdown("""
    - Python
    - Streamlit
    - GitHub
    - Knowledge retrieval
    """)

# ============================
# INFO
# ============================

elif page == "Info":

    st.title("ℹ️ Project Information")

    st.header("🤖 Programming AI Chatbot")

    st.write("""
    An educational programming assistant that helps users
    understand coding concepts, syntax, programs and examples
    in C, Java and Python.
    """)

    st.markdown("---")

    st.subheader("🎯 Project Objective")

    st.write("""
    To make programming easier for beginners by providing
    a simple chatbot that answers programming questions
    and supports learning.
    """)

    st.subheader("👩‍💻 Team Members")

    st.markdown("""
    💜 Jyothi

    💙 Aishwarya

    💚 Chaithra B H

    🧡 Madava
    """)

    st.subheader("💻 Programming Languages")

    st.markdown("""
    - C Programming
    - Java Programming
    - Python Programming
    """)
