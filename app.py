
import streamlit as st
from rag_engine import ask_rag

st.set_page_config(
    page_title="Programming Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Programming Languages Chatbot")
st.caption("Learn C, Java and Python")

question = st.text_input(
    "Ask a programming question:",
    placeholder="What is Python?"
)

if st.button("Ask"):
    if question:
        answer = ask_rag(question)
        st.write("### Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
