# 🤝 Personalized Networking Assistant (Smart Connect AI)

## 📌 Project Overview

The Personalized Networking Assistant, also known as **Smart Connect AI**, is an AI-powered web application developed to help students, professionals, researchers, and entrepreneurs prepare for networking events.

The application analyzes event descriptions, generates personalized conversation starters, verifies information using Wikipedia, stores networking history, and collects user feedback.

---

# 🎯 Problem Statement

People attending conferences, workshops, seminars, and networking events often struggle to start meaningful conversations and build professional connections. Lack of preparation reduces networking opportunities.

This project provides AI-generated conversation starters and verified information to help users communicate confidently.

---

# 💡 Proposed Solution

The system accepts an event description from the user and analyzes important topics. Based on these topics, personalized conversation starters are generated. Users can also verify topics using the Wikipedia API, save networking sessions, and submit feedback.

---

# 🚀 Features

- AI-based Event Analysis
- Personalized Conversation Starters
- Knowledge Assistant
- Wikipedia API Integration
- Save Networking Sessions
- Feedback Collection
- User-Friendly Streamlit Interface
- FastAPI Backend
- JSON Data Storage

---

# 🛠 Technology Stack

## Frontend
- Streamlit
- HTML
- CSS

## Backend
- FastAPI
- Python

## APIs
- Wikipedia API

## Database
- JSON Files
  - history.json
  - feedback.json

---

# 📂 Project Structure

```
personalized-networking-assistant/

│
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── event_analyzer.py
│   │   ├── topic_generator.py
│   │   ├── fact_checker.py
│   │   ├── history_logger.py
│   │   └── feedback_logger.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── images/
│
├── history.json
├── feedback.json
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/personalized-networking-assistant.git
```

## Move into the Project Folder

```bash
cd personalized-networking-assistant
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Application URL

```
http://localhost:8501
```

---

# 📊 Workflow

1. User enters an event description.
2. FastAPI analyzes the event.
3. Important topics are extracted.
4. AI generates conversation starters.
5. User verifies topics using Wikipedia.
6. Session is stored in history.json.
7. Feedback is stored in feedback.json.

---

# 📷 Application Modules

- Home Page
- Sidebar
- Event Description
- AI Conversation Starters
- Knowledge Assistant
- Save Networking Session
- Feedback Form
- Project Summary
- Swagger API Documentation

---

# 📁 JSON Storage

## history.json

Stores:

- Event Name
- Extracted Topics

## feedback.json

Stores:

- User Feedback

---

# 📌 Future Enhancements

- OpenAI API Integration
- User Authentication
- Cloud Database Support
- Voice Assistant
- Mobile Application
- Multi-language Support
- Resume-based Networking Suggestions

---

# 🎯 Advantages

- Easy to use
- Improves networking confidence
- Generates personalized conversation starters
- Provides verified information
- Stores networking history
- Lightweight and fast
- Responsive user interface

---

# 📚 Applications

- Conferences
- Career Fairs
- Technical Workshops
- Seminars
- Professional Networking Events
- Research Meetings
- College Placement Events

---

# 👨‍💻 Developed By

**Mohammed Mahaboob Alisha Shaik**

B.Tech – Computer Science and Engineering (AI & ML)

Aditya College of Engineering and Technology

APSCHE Internship Project – 2026

---

# 📄 License

This project is developed for educational purposes as part of the APSCHE Internship Program.
