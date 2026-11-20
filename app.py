
import streamlit as st
from rag_engine import ask_rag

st.set_page_config(
    page_title="Programming AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

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
    background-color: white;
    color: #7626a8;
    border: 1px solid #c9a7f5;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🤖 Programming AI")
st.sidebar.caption("Your Personal Coding Assistant")

# Pipeline in sidebar
with st.sidebar.expander("🔄 Pipeline"):
    st.markdown("""
    **About the Project**

    Programming AI Chatbot helps students learn C, Java and Python.

    **How it works**

    1. Select a programming language.
    2. Enter your question.
    3. Search the knowledge file.
    4. Retrieve relevant information.
    5. Display the answer.

    **Knowledge files**
    - c.txt
    - java.txt
    - python.txt
    """)

# Info in sidebar
with st.sidebar.expander("ℹ️ Info"):
    st.markdown("""
    **Programming AI Chatbot**

    Educational programming assistant.

    **Team Members**
    - Jyothi
    - Aishwarya
    - Chaithra B H
    - Madava

    **Languages**
    - C
    - Java
    - Python

    **Technology**
    - Python
    - Streamlit
    - GitHub
    """)

# MAIN CHATBOT - ALWAYS VISIBLE
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
    placeholder="Explain loops in detail..."
)

if st.button("✨ Ask Chatbot", use_container_width=True):

    if question.strip():

        with st.spinner("🤖 Searching programming knowledge..."):
            answer = ask_rag(question, language)

        st.markdown("### 🤖 Answer")
        st.write(answer)

    else:
        st.warning("Please enter your question.")
