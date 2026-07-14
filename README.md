# Personalized Networking Assistant

## Overview
The Personalized Networking Assistant is an AI-powered application that helps users create meaningful conversation starters based on an event description. It also provides Wikipedia-based fact verification and stores user history and feedback.

## Features
- Event topic analysis
- AI conversation starter generation
- Wikipedia fact checking
- History logging
- Feedback collection
- FastAPI backend
- Streamlit frontend

## Technologies Used
- Python
- FastAPI
- Streamlit
- Wikipedia API
- JSON
- Uvicorn

## Project Structure

```
app/
    main.py
    services/
frontend/
    streamlit_app.py
tests/
requirements.txt
README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

## Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

## Author

Mohammed Mahaboob Alisha Shaik