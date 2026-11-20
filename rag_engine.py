
import os

def load_knowledge(language):
    files = {
        "C": "c.txt",
        "Java": "java.txt",
        "Python": "python.txt"
    }

    filename = files.get(language)

    if not filename or not os.path.exists(filename):
        return "Knowledge file not found."

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def ask_rag(question, language):
    knowledge = load_knowledge(language)

    if knowledge == "Knowledge file not found.":
        return knowledge

    question_words = question.lower().split()

    sections = knowledge.split("\n\n")

    best_section = ""
    best_score = 0

    for section in sections:
        score = sum(
            1 for word in question_words
            if len(word) > 2 and word in section.lower()
        )

        if score > best_score:
            best_score = score
            best_section = section

    if best_score == 0:
        return knowledge

    return best_section
