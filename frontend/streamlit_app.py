import streamlit as st
import requests

st.title("🤝 Personalized Networking Assistant")

event = st.text_input(
    "Enter Event Description",
    placeholder="Example: AI for Sustainable Cities"
)

if st.button("Generate Conversation Starters"):
    if event:
        response = requests.get(
            "http://127.0.0.1:8000/generate",
            params={"event": event}
        )

        data = response.json()

        st.subheader("Conversation Starters")

        for starter in data["conversation_starters"]:
            st.subheader("Fact Checker")

topic = st.text_input(
    "Enter topic to verify",
    placeholder="Example: blockchain"
)

if st.button("Check Fact"):
    if topic:
        response = requests.get(
            "http://127.0.0.1:8000/factcheck",
            params={"topic": topic}
        )

        data = response.json()

        st.write(data["fact"])
