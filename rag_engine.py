
import os
import re


# ==========================================
# 1. LOAD KNOWLEDGE FILE
# ==========================================

def load_knowledge(language):

    files = {
        "C": "c.txt",
        "Python": "python.txt",
        "Java": "java.txt"
    }

    filename = files.get(language)

    if filename is None:
        return None

    folder = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(folder, filename)

    if not os.path.exists(filepath):
        return None

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


# ==========================================
# 2. DIVIDE KNOWLEDGE INTO TOPICS
# ==========================================

def get_sections(knowledge):

    sections = re.split(
        r"(?m)(?=^\d+\.\s)",
        knowledge
    )

    result = []

    for section in sections:

        section = section.strip()

        if section and re.match(r"^\d+\.\s", section):
            result.append(section)

    return result


# ==========================================
# 3. DETAILED FUNCTION EXPLANATIONS
# ==========================================

def explain_functions(language):

    explanations = {

        "C": """
## FUNCTIONS IN C

A function is a block of code that performs a specific task.
It helps divide a program into smaller reusable parts.

### Types of functions
1. Library functions
2. User-defined functions

### Syntax

return_type function_name(parameters)
{
    statements;
    return value;
}

### Example

#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main()
{
    int result = add(10, 20);
    printf("Sum = %d", result);
    return 0;
}

### Output
Sum = 30

### Explanation
- int: return type
- add: function name
- a and b: parameters
- return a + b: returns the sum
- add(10, 20): function call

### Advantages
- Code reusability
- Easy debugging
- Reduces repetition
- Improves readability
""",

        "Python": """
## FUNCTIONS IN PYTHON

A function is a reusable block of code that performs a specific task.
Functions are created using the def keyword.

### Syntax

def function_name(parameters):
    statements
    return value

### Example

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

### Output
Sum = 30

### Explanation
- def: defines a function
- add: function name
- a and b: parameters
- return: returns the result
- add(10, 20): function call

### Types of functions
1. Built-in functions
2. User-defined functions
3. Lambda functions
4. Recursive functions

### Advantages
- Reusable code
- Easy maintenance
- Less repetition
- Improved readability
""",

        "Java": """
## METHODS IN JAVA

A method is a block of code inside a class that performs a specific task.
Methods help organize and reuse code.

### Syntax

returnType methodName(parameters)
{
    statements;
    return value;
}

### Example

class Main {

    static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = add(10, 20);
        System.out.println("Sum = " + result);
    }
}

### Output
Sum = 30

### Explanation
- static: method can be called without creating an object in this example
- int: return type
- add: method name
- a and b: parameters
- return: returns the result
- main(): starting point of Java program

### Types of methods
1. Predefined methods
2. User-defined methods
3. Static methods
4. Instance methods

### Advantages
- Code reusability
- Easy maintenance
- Reduces repeated code
- Better program organization
"""
    }

    return explanations.get(language)


# ==========================================
# 4. EXTRACT KEYWORDS
# ==========================================

def get_keywords(question):

    question = question.lower()

    aliases = {
        "loop": ["loops", "iteration", "iterative"],
        "function": ["functions", "method", "methods"],
        "array": ["arrays"],
        "variable": ["variables"],
        "string": ["strings"],
        "class": ["classes"],
        "object": ["objects"],
        "inheritance": ["inherited"],
        "condition": ["conditions", "conditional"],
        "pointer": ["pointers"],
        "operator": ["operators"],
        "exception": ["exceptions"],
        "file": ["files"],
        "datatype": ["data type", "data types"],
        "dictionary": ["dictionaries"],
        "list": ["lists"],
        "tuple": ["tuples"],
        "set": ["sets"],
        "constructor": ["constructors"],
        "recursion": ["recursive"],
        "polymorphism": [],
        "encapsulation": [],
        "abstraction": []
    }

    for main_word, related_words in aliases.items():

        for word in related_words:
            question = question.replace(word, main_word)

    stop_words = {
        "what", "is", "are", "was", "were",
        "the", "a", "an", "in", "of", "to",
        "how", "explain", "tell", "me", "about",
        "with", "for", "and", "please", "give",
        "write", "show", "describe", "can", "you",
        "program", "programming", "language",
        "detail", "details", "detailed", "example", "examples"
    }

    words = re.findall(r"[a-zA-Z]+", question)

    keywords = [
        word for word in words
        if word not in stop_words and len(word) > 1
    ]

    return keywords


# ==========================================
# 5. FIND THE BEST MATCHING TOPIC
# ==========================================

def find_best_section(question, sections):

    keywords = get_keywords(question)

    best_section = None
    best_score = 0

    for section in sections:

        lines = section.splitlines()

        heading = lines[0].lower() if lines else ""
        content = section.lower()

        score = 0

        for word in keywords:

            # Heading match
            if word in heading:
                score += 5

            # Content match
            if word in content:
                score += 1

        if score > best_score:

            best_score = score
            best_section = section

    if best_score > 0:
        return best_section

    return None


# ==========================================
# 6. MAIN CHATBOT FUNCTION
# ==========================================

def ask_rag(question, language):

    question = question.strip()

    if not question:
        return "Please enter a question."

    knowledge = load_knowledge(language)

    if knowledge is None:
        return (
            "Knowledge file not found. "
            "Please check c.txt, python.txt and java.txt."
        )

    sections = get_sections(knowledge)

    if not sections:
        return "No topics found in the knowledge file."

    question_lower = question.lower()

    # Introduction questions
    intro_patterns = [
        "what is c",
        "what is java",
        "what is python",
        "define c",
        "define java",
        "define python",
        "introduction to c",
        "introduction to java",
        "introduction to python"
    ]

    if any(pattern in question_lower for pattern in intro_patterns):

        for section in sections:

            if "introduction" in section.lower():
                return section

    # Detailed function explanations
    function_words = [
        "function", "functions",
        "method", "methods"
    ]

    if any(word in question_lower for word in function_words):

        answer = explain_functions(language)

        if answer:
            return answer

    # Retrieve matching knowledge topic
    answer = find_best_section(question, sections)

    if answer:
        return answer

    return (
        "Sorry, I couldn't find this topic in the "
        + language
        + " knowledge file. Try asking about variables, "
        "loops, functions, arrays, classes or operators."
    )
