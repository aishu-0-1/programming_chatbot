
import streamlit as st
from rag_engine import ask_rag

st.set_page_config(
    page_title="Programming AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# DESIGN
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

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🤖 Programming AI")
st.sidebar.caption("Your Coding Assistant")

page = st.sidebar.radio(
    "Navigation",
    ["💬 Chatbot", "🔄 Pipeline", "ℹ️ Info"]
)

# =========================
# CHATBOT PAGE
# =========================
if page == "💬 Chatbot":

    st.title("🌈 Programming AI Chatbot")
    st.markdown(
        "<h3 style='text-align:center;'>💻 Your Personal Coding Assistant</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Ask questions and learn programming step by step.</p>",
        unsafe_allow_html=True
    )

    language = st.selectbox(
        "Choose Programming Language",
        ["C", "Java", "Python"]
    )

    question = st.text_input(
        "Ask your question",
        placeholder="Explain programming in detail..."
    )

    if st.button("✨ Ask Chatbot", use_container_width=True):

        if question.strip():

            with st.spinner("Searching programming knowledge..."):
                answer = ask_rag(question, language)

            st.markdown("## 🤖 Chatbot Answer")
            st.write(answer)

        else:
            st.warning("Please enter your question.")

# =========================
# PIPELINE PAGE
# =========================
elif page == "🔄 Pipeline":

    st.title("🔄 Project Pipeline")

    st.markdown("""
    <h3 style="text-align:center;">About the Project</h3>
    """, unsafe_allow_html=True)

    st.write("""
    Programming AI Chatbot is an educational project developed
    to help students learn C, Java and Python programming.

    It provides programming information, explanations and
    knowledge-based answers to users.
    """)

    st.subheader("⚙️ How the Project Works")

    st.markdown("""
    **Step 1 — Select Language**  
    Select C, Java or Python.

    **Step 2 — Enter Question**  
    Enter any programming question.

    **Step 3 — Search Knowledge**  
    The system reads the selected language knowledge file.

    **Step 4 — Retrieve Information**  
    Relevant programming information is selected.

    **Step 5 — Display Answer**  
    The chatbot displays the answer on the screen.
    """)

    st.subheader("📚 Knowledge Files")

    st.markdown("""
    - C Programming — `c.txt`
    - Java Programming — `java.txt`
    - Python Programming — `python.txt`
    """)

    st.subheader("🛠️ Technologies")

    st.markdown("""
    - Python
    - Streamlit
    - GitHub
    - Text-based knowledge retrieval
    """)

# =========================
# INFO PAGE
# =========================
elif page == "ℹ️ Info":

    st.title("ℹ️ Project Information")

    st.subheader("Programming AI Chatbot")

    st.write("""
    An educational chatbot designed to help users understand
    programming concepts, learn syntax, explore code examples
    and improve their programming knowledge.
    """)

    st.subheader("🎯 Objective")

    st.write("""
    The main objective is to make programming easier for beginners
    by providing a simple interactive platform for learning
    C, Java and Python.
    """)

    st.subheader("👩‍💻 Team Members")

    st.markdown("""
    - Jyothi
    - Aishwarya
    - Chaithra B H
    - Madava
    """)

    st.subheader("💻 Programming Languages")

    st.markdown("""
    🧡 C Programming

    💙 Java Programming

    💚 Python Programming
    """)
