# 🎙️ Voice Agent CLI 

A voice-controlled CLI assistant built using **Speech Recognition**, **LangGraph**, and **Python**, designed to execute commands through natural voice input.

---

## 🚀 Project Overview

This project aims to build a **voice-driven AI agent** that:

* 🎤 Captures voice input
* 🔤 Converts speech → text (Google Speech Recognition)
* 🧠 Processes commands using LangGraph (node-based workflow)
* ⚙️ Executes actions based on detected intent
* 🔄 Runs continuously like a CLI tool

---

## 🧱 Current Architecture

```
Voice Input → Speech-to-Text → LangGraph Flow → Action Execution
```

---

## 📁 Project Structure

```
voice_agent_cli/
│
├── speech_to_text.py   # Handles microphone input & speech recognition
├── langgraph_flow.py   # Defines LangGraph nodes & workflow
└── main.py             # Entry point (connects voice + graph)
```

---

## ⚙️ Tech Stack

| Component        | Technology Used             |
| ---------------- | --------------------------- |
| Speech Input     | SpeechRecognition + PyAudio |
| AI Workflow      | LangGraph                   |
| Backend Language | Python                      |
| (Upcoming) DB    | MongoDB (for checkpointing) |

---

## 🟢 Features Implemented (Current Status)

### ✅ 1. Speech Recognition

* Captures audio from microphone
* Converts speech → text using Google API
* Handles errors like:

  * Unknown audio
  * API failures

---

### ✅ 2. Continuous Voice CLI

* Runs in a loop
* Listens for commands continuously
* Exit trigger via voice (`"exit"`)

---

### ✅ 3. LangGraph Workflow

* Node-based architecture
* Current nodes:

  * **Input Node** → receives text
  * **Parser Node** → detects intent
  * **Router Node** → decides action

---

### ✅ 4. Intent Detection (Basic NLP)

Supported commands:

| Voice Input   | Detected Intent |
| ------------- | --------------- |
| "create file" | create_file     |
| "run code"    | run_code        |
| anything else | unknown         |

---

### ✅ 5. Modular Code Structure

* Clean separation of concerns:

  * Voice handling
  * Logic processing
  * Main execution loop

---

## ▶️ How to Run

### 1. Clone / Navigate to Project

```bash
cd voice_agent_cli
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install SpeechRecognition
pip install pyaudio
pip install langgraph langchain pymongo
```

> ⚠️ If PyAudio fails on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

### 4. Run the Project

```bash
python main.py
```

---

## 🧪 Example Usage

```
🎤 Listening...
You: create file

📥 Input received: create file
🧠 Parsed intent: create_file
📁 Action: Creating file...
```

---

## ⚠️ Known Limitations

* Basic keyword-based intent detection (no advanced NLP yet)
* No real file execution yet (only simulated actions)
* No persistence (MongoDB not integrated yet)

---

## 🔴 Upcoming Features

* 🔥 MongoDB checkpointing (state persistence)
* 🧠 Advanced intent parsing (LLM / smarter NLP)
* ⚙️ Real command execution (file creation, script running)
* 🗣️ Text-to-speech responses
* 📦 CLI packaging (installable tool)

---

## 🎯 Future Vision

Transform this into a **fully autonomous developer assistant** that can:

* Understand complex voice instructions
* Modify codebases
* Execute workflows
* Maintain memory across sessions

---

## 🙌 Author

Built as part of an **Agentic AI system project**.

---

## 📌 Status

🟡 **In Progress — Phase 2 (LangGraph Integration Completed)**
🔜 Next: MongoDB Checkpointing
