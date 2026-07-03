import json
import os

def save_feedback(feedback):
    if os.path.exists("feedback.json"):
        with open("feedback.json", "r") as file:
            try:
                feedback_data = json.load(file)
            except:
                feedback_data = []
    else:
        feedback_data = []

    feedback_data.append({"feedback": feedback})

    with open("feedback.json", "w") as file:
        json.dump(feedback_data, file, indent=4)