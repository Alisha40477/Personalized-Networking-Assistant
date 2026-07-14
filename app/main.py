from fastapi import FastAPI
from app.services.event_analyzer import analyze_event
from app.services.topic_generator import generate_topics
from app.services.fact_checker import check_fact
from app.services.history_logger import save_history
from app.services.feedback_logger import save_feedback

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant for generating conversation starters",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Personalized Networking Assistant"
    }


@app.get("/analyze")
def analyze(event: str):
    topics = analyze_event(event)

    return {
        "topics": topics
    }


@app.get("/generate")
def generate(event: str):
    topics = analyze_event(event)

    return {
        "conversation_starters": generate_topics(topics)
    }


@app.get("/factcheck")
def factcheck(topic: str):
    return {
        "fact": check_fact(topic)
    }


@app.post("/save-history")
def history(event: str):
    topics = analyze_event(event)
    save_history(event, topics)

    return {
        "message": "History saved successfully"
    }


@app.post("/feedback")
def feedback(feedback: str):
    save_feedback(feedback)

    return {
        "message": "Feedback saved successfully"
    }