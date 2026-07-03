import json
import os

def save_history(event, topics):
    data = {
        "event": event,
        "topics": topics
    }

    if os.path.exists("history.json"):
        with open("history.json", "r") as file:
            try:
                history = json.load(file)
            except:
                history = []
    else:
        history = []

    history.append(data)

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)