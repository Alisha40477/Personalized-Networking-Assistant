import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Smart Connect AI",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title(" Smart Connect AI")

st.sidebar.write(
    "Your AI companion for conferences, seminars, workshops and networking events."
)

st.sidebar.markdown("---")

name = st.sidebar.text_input(
    "Your Name"
)

profession = st.sidebar.selectbox(
    "Your Profession",
    [
        "Student",
        "Software Engineer",
        "Data Scientist",
        "Researcher",
        "Entrepreneur",
        "Other"
    ]
)

goal = st.sidebar.selectbox(
    "Networking Goal",
    [
        "Find Internship Opportunities",
        "Meet Professionals",
        "Find Collaborators",
        "Explore Research Topics",
        "Build Connections"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Powered by FastAPI + Streamlit + NLP"
)


st.title(" SmartConnect AI")

st.write(
    "Generate meaningful conversation starters for networking events."
)


event = st.text_area(
    "Event Description",
    placeholder="Example: AI for Sustainable Cities Conference"
)


if st.button(" Generate Smart Starters"):

    if event:

        response = requests.get(
            f"{API_URL}/generate",
            params={"event": event}
        )

        data = response.json()

        st.subheader(" Suggested Conversation Starters")

        for starter in data["conversation_starters"]:

            st.info(
                f"""
{name if name else 'You'} ({profession}) can ask:

{starter}

Goal: {goal}
                """
            )

    else:
        st.warning(
            "Please enter an event description."
        )


st.markdown("---")

st.subheader("🔍 Knowledge Assistant")

topic = st.text_input(
    "Enter a topic to verify",
    placeholder="Example: Blockchain"
)

if st.button(" Verify Topic"):

    if topic:

        response = requests.get(
            f"{API_URL}/factcheck",
            params={"topic": topic}
        )

        data = response.json()

        st.success(
            data["fact"]
        )


st.markdown("---")

if st.button(" Save Session"):

    if event:

        requests.get(
            f"{API_URL}/save-history",
            params={"event": event}
        )

        st.success(
            "Session saved successfully."
        )


st.markdown("---")

feedback = st.text_area(
    "Share your feedback"
)

if st.button(" Submit Feedback"):

    if feedback:

        requests.get(
            f"{API_URL}/feedback",
            params={"feedback": feedback}
        )

        st.success(
            "Thank you for your feedback."
        )


st.markdown("---")

st.caption(
    "Smart Connect AI | Developed using FastAPI, Streamlit and NLP"
)