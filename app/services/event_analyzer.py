def analyze_event(event_description: str):
    words = event_description.split()

    topics = []

    for word in words:
        if len(word) > 3:
            topics.append(word)

    return topics