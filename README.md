🧠 LangGraph Agents With Memory

This project demonstrates how to build intelligent conversational agents using LangGraph and LangChain memory.

🚀 Overview

The app creates a simple AI agent that:
- Understands user input through LangGraph workflow.
- Keeps track of previous conversations using ConversationBufferMemory.
- Interacts through a FastAPI backend and a simple web interface (HTML + CSS).



🏗️ Project Structure

LangGraph-Agents-With-Memory/
│
├── app.py # FastAPI app to run the server
├── Agents.py # Agent definition and memory logic
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend page
├── static/
│ └── style.css # Styling for the page
└── .gitignore # Ignored files (like pycache)

yaml
Copy code



⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Janaelpardisi/LangGraph-Agents-With-Memory.git
   cd LangGraph-Agents-With-Memory
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Run the App
Start the FastAPI server:

bash
Copy code
uvicorn app:app --reload
Then open your browser and visit:

cpp
Copy code
http://127.0.0.1:8000
You’ll see the web interface to chat with your LangGraph Agent.

🧩 Technologies Used
Python

LangGraph

LangChain

FastAPI

HTML / CSS
