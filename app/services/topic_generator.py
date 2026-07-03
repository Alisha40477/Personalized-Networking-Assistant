def generate_topics(topics):
    questions = []

    for topic in topics:
        questions.append(
            f"What are your thoughts on {topic}?"
        )

    return questions