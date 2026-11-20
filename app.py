
import streamlit as st

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
h1 {
    color: #7626a8;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🌈 Programming AI Chatbot")
st.subheader("💻 Your Personal Coding Assistant")
st.write("Ask questions and learn programming step by step.")

language = st.selectbox(
    "Choose a Programming Language",
    ["C", "Java", "Python"]
)

question = st.text_input(
    "Ask your question",
    placeholder="Explain C programming in detail..."
)

if st.button("✨ Ask Chatbot"):

    if not question:
        st.warning("Please enter your question.")

    elif language == "C":

        st.markdown("## 🤖 C Programming")

        st.write("""
        C is a general-purpose procedural programming language
        developed by Dennis Ritchie in the early 1970s.
        It is widely used for system programming and application development.

        ### Features of C
        - Simple and efficient programming language.
        - Supports pointers and memory management.
        - Provides functions for code reuse.
        - Supports arrays, structures and loops.
        - Fast execution.

        ### Applications
        - Operating systems.
        - Embedded systems.
        - Device drivers.
        - Compilers.
        - Database systems.

        ### Example Program
        """)

        st.code("""
#include <stdio.h>

int main() {
    printf("Hello World");
    return 0;
}
        """, language="c")

        st.write("""
        ### Explanation
        1. #include <stdio.h> includes the standard input/output library.
        2. main() is the starting point of the program.
        3. printf() displays text on the screen.
        4. return 0 indicates successful program execution.
        """)

    elif language == "Java":

        st.markdown("## 🤖 Java Programming")

        st.write("""
        Java is a high-level, object-oriented programming language
        developed by James Gosling at Sun Microsystems.

        Java is used to create secure, portable and reliable applications.

        ### Features of Java
        - Object-oriented programming.
        - Platform independent.
        - Secure and robust.
        - Automatic memory management.
        - Supports multithreading.

        ### Applications
        - Android applications.
        - Web applications.
        - Enterprise software.
        - Banking systems.
        - Desktop applications.

        ### Example Program
        """)

        st.code("""
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
        """, language="java")

        st.write("""
        ### Explanation
        1. class Main defines a class named Main.
        2. main() is the starting method of the program.
        3. System.out.println() displays text.
        4. Java code runs through the JVM (Java Virtual Machine).
        """)

    else:

        st.markdown("## 🤖 Python Programming")

        st.write("""
        Python is a high-level, interpreted and general-purpose
        programming language created by Guido van Rossum.

        Python is popular for its simple syntax and readability.

        ### Features of Python
        - Easy to learn and read.
        - Simple syntax.
        - Large library support.
        - Supports object-oriented programming.
        - Dynamically typed language.

        ### Applications
        - Artificial intelligence.
        - Machine learning.
        - Web development.
        - Data science.
        - Automation.

        ### Example Program
        """)

        st.code("""
print("Hello World")
        """, language="python")

        st.write("""
        ### Explanation
        1. print() is a built-in Python function.
        2. It displays text or values on the screen.
        3. Python does not require semicolons for basic statements.
        4. Python code is executed by the Python interpreter.
        """)

    st.success("Explanation generated successfully! 🎉")
