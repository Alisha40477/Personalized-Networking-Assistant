import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError

def check_fact(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary

    except (PageError, DisambiguationError):
        return "No information found."