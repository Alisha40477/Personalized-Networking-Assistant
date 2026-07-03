import wikipedia

def check_fact(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except:
        return "No information found."