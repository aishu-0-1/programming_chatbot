
import os
import re

# Load the selected programming language file
def load_knowledge(language):

    files = {
        "C": "c.txt",
        "Java": "java.txt",
        "Python": "python.txt"
    }

    filename = files.get(language)

    if filename is None or not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# Divide knowledge into topics
def get_sections(knowledge):

    sections = re.split(r"(?m)(?=^\d+\.\s)", knowledge)

    result = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        # Ignore the main file title
        if not re.match(r"^\d+\.\s", section):
            continue

        result.append(section)

    return result


# Find the best answer
def ask_rag(question, language):

    knowledge = load_knowledge(language)

    if knowledge is None:
        return "Knowledge file not found. Please check your GitHub files."

    sections = get_sections(knowledge)

    if not sections:
        return "No programming information found in the knowledge file."

    question_lower = question.lower().strip()

    # Return the introduction for basic language questions
    basic_questions = [
        "what is",
        "define",
        "introduction to",
        "tell me about"
    ]

    if any(q in question_lower for q in basic_questions):

        if sections:
            return sections[0]

    # Remove common words from the question
    stop_words = {
        "what", "is", "are", "was", "were",
        "the", "a", "an", "in", "of", "to",
        "how", "explain", "tell", "me", "about",
        "with", "for", "and", "please", "give",
        "write", "show", "describe"
    }

    words = re.findall(r"[a-zA-Z]+", question_lower)

    keywords = [
        word for word in words
        if word not in stop_words and len(word) > 1
    ]

    # Search for the most relevant section
    best_section = None
    best_score = 0

    for section in sections:

        section_lower = section.lower()
        score = 0

        for word in keywords:

            if word in section_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_section = section

    # Return the full topic, including its explanation
    if best_section is not None and best_score > 0:
        return best_section

    return (
        "I couldn't find this topic in my "
        + language
        + " knowledge file. Please try asking about another programming topic."
    )
