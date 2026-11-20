
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
</style>
""", unsafe_allow_html=True

# SIDEBAR
st.sidebar.title("🤖 Programming AI")
st.sidebar.caption("Your Coding Assistant")

page = st.sidebar.radio(
    "Navigation",
    ["💬 Chatbot", "🔄 Pipeline", "ℹ️ Info"]
)

# CHATBOT PAGE
if page == "💬 Chatbot":

    st.title("🌈 Programming AI Chatbot")
    st.subheader("💻 Your Personal Coding Assistant")
    st.write("Learn C, Java and Python step by step.")

    language = st.selectbox(
        "Choose Programming Language",
        ["C", "Java", "Python"]
    )

    question = st.text_input(
        "Ask your programming question",
        placeholder="Explain loops in detail..."
    )

    if st.button("✨ Ask Chatbot"):

        if question.strip():
            with st.spinner("Searching programming knowledge..."):
                answer = ask_rag(question, language)

            st.markdown("### 🤖 Answer")
            st.markdown(answer)
        else:
            st.warning("Please enter your question.")

# PIPELINE PAGE
elif page == "🔄 Pipeline":

    st.title("🔄 Project Pipeline")

    st.header("About the Project")

    st.write("""
    Programming AI Chatbot is an educational assistant designed
    to help students learn three programming languages:
    C, Java and Python.

    Users can select a programming language and ask questions.
    The chatbot searches its programming knowledge files
    and displays relevant information.
    """)

    st.header("⚙️ How It Works")

    st.markdown("""
    **Step 1 — Language Selection**  
    The user selects C, Java or Python.

    **Step 2 — Question Input**  
    The user enters a programming question.

    **Step 3 — Knowledge Retrieval**  
    The chatbot searches the selected language's knowledge file.

    **Step 4 — Answer Generation**  
    Relevant information is retrieved from the knowledge.

    **Step 5 — Display Answer**  
    The answer is shown to the user on the chatbot page.
    """)

    st.header("📚 Knowledge Files")

    st.markdown("""
    - `c.txt` — C programming concepts
    - `java.txt` — Java programming concepts
    - `python.txt` — Python programming concepts
    """)

    st.header("🛠️ Technologies Used")

    st.markdown("""
    - Python
    - Streamlit
    - Text-based knowledge retrieval
    - GitHub
    """)

# INFO PAGE
elif page == "ℹ️ Info":

    st.title("ℹ️ Project Information")

    st.header("Programming AI Chatbot")

    st.write("""
    An educational programming chatbot that helps users understand
    programming concepts, learn syntax, explore examples and
    improve coding knowledge in C, Java and Python.
    """)

    st.header("👩‍💻 Team Members")

    members = [
        "Jyothi",
        "Aishwarya",
        "Chaithra B H",
        "Madava"
    ]

    for member in members:
        st.markdown(f"👤 {member}")

    st.header("🎯 Project Objective")

    st.write("""
    To make programming easier for students by providing a simple
    interactive platform for learning programming concepts and
    exploring coding examples.
    """)

    st.header("💡 Languages Covered")

    st.markdown("""
    🧡 C Programming

    💙 Java Programming

    💚 Python Programming
    """)
