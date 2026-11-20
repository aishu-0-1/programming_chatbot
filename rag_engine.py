
def load_data():
    with open("data.txt", "r", encoding="utf-8") as file:
        return file.read()


def retrieve(question, background):
    question = question.lower()

    if "c" in question or "pointer" in question:
        return background[:500]

    if "java" in question:
        start = background.find("JAVA PROGRAMMING")
        end = background.find("PYTHON PROGRAMMING")
        return background[start:end]

    if "python" in question:
        start = background.find("PYTHON PROGRAMMING")
        return background[start:]

    if "compare" in question:
        return background

    return background


def ask_rag(question):
    background = load_data()
    answer = retrieve(question, background)
    return answer
