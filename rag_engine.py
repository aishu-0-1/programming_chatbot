
import os
import re

# ------------------------------------------
# 1. LOAD KNOWLEDGE FILES
# ------------------------------------------

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


# ------------------------------------------
# 2. SPLIT FILE INTO TOPICS
# ------------------------------------------

def get_sections(knowledge):

    sections = re.split(
        r"(?m)(?=^\d+\.\s)",
        knowledge
    )

    result = []

    for section in sections:

        section = section.strip()

        if re.match(r"^\d+\.\s", section):
            result.append(section)

    return result


# ------------------------------------------
# 3. DETAILED FUNCTION EXPLANATIONS
# ------------------------------------------

def explain_functions(language):

    explanations = {

        "C": """
## FUNCTIONS IN C

A function is a block of code that performs a particular task.
Functions help divide a large program into smaller and reusable parts.

### Types of functions
1. Library functions
2. User-defined functions

### Function syntax

return_type function_name(parameters)
{
    // statements
    return value;
}

### Example program

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
- a, b: parameters
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

A function is a reusable block of code used to perform a specific task.
Python functions are created using the def keyword.

### Syntax

def function_name(parameters):
    statements
    return value

### Example program

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum =", result)

### Output
Sum = 30

### Explanation
- def: creates a function
- add: function name
- a, b: parameters
- return: sends a result back
- add(10, 20): function call

### Types of functions
1. Built-in functions
2. User-defined functions
3. Lambda functions
4. Recursive functions

### Advantages
- Reusable code
- Less repetition
- Easy maintenance
- Improved readability
""",

        "Java": """
## METHODS IN JAVA

In Java, a function inside a class is generally called a method.
A method is used to perform a particular operation.

### Syntax

returnType methodName(parameters)
{
    // statements
    return value;
}

### Example program

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
- a, b: parameters
- return: sends the result back
- main(): starting point of the program

### Types of methods
1. Predefined methods
2. User-defined methods
3. Static methods
4. Instance methods

### Advantages
- Code reusability
- Easy maintenance
- Reduces repeated code
- Improves program organization
"""
    }

    return explanations.get(language)


# ------------------------------------------
# 4. TOPIC KEYWORDS
# ------------------------------------------

def get_keywords(question):

    aliases = {
        "loop": ["loops", "iteration", "iterative"],
        "function": ["functions", "method", "methods"],
        "array": ["arrays"],
        "variable": ["variables"],
        "string": ["strings"],
        "class": ["classes"],
        "object": ["objects"],
        "inheritance": ["inherited"],
        "condition": ["conditions", "conditional", "if", "else"],
        "pointer": ["pointers"],
        "operator": ["operators"],
        "exception": ["exceptions", "error handling"],
        "file": ["files", "file handling"],
        "datatype": ["data type", "data types"],
        "dictionary": ["dict", "dictionaries"],
        "list": ["lists"],
        "tuple": ["tuples"],
        "set": ["sets"],
        "constructor": ["constructors"],
        "recursion": ["recursive"],
        "polymorphism": ["poly"],
        "encapsulation": ["encapsulate"],
        "abstraction": ["abstract"],
    }

    question = question.lower()

    for main_word, related_words in aliases.items():

        for word in related_words:

            question = question.replace(word, main_word)

    stop_words = {
        "what", "is", "are", "was", "were",
        "the", "a", "an", "in", "of", "to",
        "how", "explain", "tell", "me", "about",
        "with", "for", "and", "please", "give",
        "write", "show", "describe", "can", "you",
        "program", "programming", "language", "detail",
        "details", "detailed", "example", "examples"
    }

    words = re.findall(r"[a-zA-Z]+", question)

    keywords = [
        word for word in words
        if word not in stop_words and len(word) > 1
    ]

    return keywords


# ------------------------------------------
# 5. FIND BEST TOPIC
# ------------------------------------------

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

            # Heading match is more important
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


# ------------------------------------------
# 6. MAIN CHATBOT
# ------------------------------------------

def ask_rag(question, language):

    question = question.strip()

    if not question:
        return "Please enter a programming question."

    knowledge = load_knowledge(language)

    if knowledge is None:
        return "Knowledge file not found. Check your files."

    sections = get_sections(knowledge)

    if not sections:
        return "No programming topics found in the knowledge file."

    question_lower = question.lower()

    # Introduction questions
    intro_words = [
        "what is",
        "define",
        "introduction",
        "tell me about"
    ]

    if any(word in question_lower for word in intro_words):

        if language.lower() in question_lower or question_lower.strip() in [
            "what is c",
            "what is java",
            "what is python"
        ]:

            for section in sections:

                if "introduction" in section.lower():
                    return section

    # Special detailed function answers
    function_words = [
        "function",
        "functions",
        "method",
        "methods"
    ]

    if any(word in question_lower for word in function_words):

        detailed_answer = explain_functions(language)

        if detailed_answer:
            return detailed_answer

    # Retrieve matching topic
    answer = find_best_section(question, sections)

    if answer:
        return answer

    return (
        "I couldn't find this topic in the "
        + language
        + " knowledge file. Try asking about variables, loops, "
        "functions, arrays, classes or operators."
    )
