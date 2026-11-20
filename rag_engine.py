
import os
import re

# Load programming knowledge
def load_knowledge(language):

    files = {
        "C": "c.txt",
        "Java": "java.txt",
        "Python": "python.txt"
    }

    filename = files.get(language)

    if filename is None:
        return None

    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    if not os.path.exists(filepath):
        return None

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


# Split knowledge into numbered topics
def get_sections(knowledge):

    sections = re.split(r"(?m)(?=^\d+\.\s)", knowledge)

    result = []

    for section in sections:

        section = section.strip()

        if not section:
            continue

        if re.match(r"^\d+\.\s", section):
            result.append(section)

    return result


# Search for the correct programming topic
def ask_rag(question, language):

    knowledge = load_knowledge(language)

    if knowledge is None:
        return "Knowledge file not found. Please check c.txt, java.txt and python.txt."

    sections = get_sections(knowledge)

    if not sections:
        return "No topics found in the knowledge file."

    question_lower = question.lower().strip()

    # Remove common words
    stop_words = {
        "what", "is", "are", "was", "were",
        "the", "a", "an", "in", "of", "to",
        "how", "explain", "tell", "me", "about",
        "with", "for", "and", "please", "give",
        "write", "show", "describe", "can", "you"
    }

    # Extract question keywords
    words = re.findall(r"[a-zA-Z]+", question_lower)

    keywords = [
        word for word in words
        if word not in stop_words and len(word) > 1
    ]

    # Handle language introduction questions
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

    # Find the best matching topic
    best_section = None
    best_score = 0

    for section in sections:

        section_lower = section.lower()
        score = 0

        for word in keywords:

            if word in section_lower:
                score += 1

        # Give extra importance to topic headings
        heading = section.split("\n")[0].lower()

        for word in keywords:

            if word in heading:
                score += 3

        if score > best_score:
            best_score = score
            best_section = section

    # Return the full topic
    if best_section is not None and best_score > 0:
        return best_section

    return (
        "Sorry, I couldn't find a matching topic in the "
        + language
        + " knowledge file. Please try another programming question."
    )
