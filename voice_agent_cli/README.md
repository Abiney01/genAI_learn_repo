# 🎙️ Voice Agent CLI 

A voice-controlled CLI assistant built using **Speech Recognition**, **LangGraph**, and **Python**, designed to execute commands through natural voice input.

---

## 🚀 Project Overview

This project aims to build a **voice-driven AI agent** that:

* 🎤 Captures voice input
* 🔤 Converts speech → text (Google Speech Recognition)
* 🧠 Processes commands using LangGraph (node-based workflow)
* 🤖 Generates safe shell commands using LLM (OpenAI/Gemini)
* ⚙️ Executes actions with built-in safety checks
* 💾 Maintains persistent state via MongoDB
* 🔄 Runs continuously as an interactive CLI tool

---

## 🧱 Current Architecture

```
Voice Input → Speech-to-Text → LangGraph Flow → LLM Command Generation → Safe Execution → MongoDB Persistence
```

---

## 📁 Project Structure

```
voice_agent_cli/
│
├── speech_to_text.py   # Handles microphone input & speech recognition
├── langgraph_flow.py   # Defines LangGraph nodes & workflow
├── llm_client.py       # Generates shell commands using LLM (OpenAI/Gemini)
├── executor.py         # Executes commands with safety checks
├── main.py             # Entry point (connects voice + graph)
├── test_mic.py         # Microphone testing utility
├── test_mongo.py       # MongoDB checkpoint testing
└── .env                # Environment variables (API keys)
```

---

## ⚙️ Tech Stack

| Component        | Technology Used             |
| ---------------- | --------------------------- |
| Speech Input     | SpeechRecognition + PyAudio |
| AI Workflow      | LangGraph                   |
| LLM Provider     | OpenAI/Google Gemini API    |
| Backend Language | Python                      |
| Database         | MongoDB (checkpointing)     |

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

### ✅ 3. LLM-Powered Command Generation

- Uses OpenAI/Gemini API to convert natural language to shell commands
- System prompt ensures safe, reversible operations
- Windows command prompt compatible
- Returns structured JSON responses

---

### ✅ 4. LangGraph Workflow

* Node-based architecture
* Current nodes:

  * **Input Node** → receives text
  * **Parser Node** → detects intent (basic fallback)
  * **Router Node** → generates & executes commands via LLM

---

### ✅ 5. MongoDB Checkpointing

- Persistent state management
- Thread-based session tracking
- Enables conversation continuity across runs

---

### ✅ 6. Modular Code Structure

* Clean separation of concerns:

  * Voice handling (speech_to_text.py)
  * LLM integration (llm_client.py)
  * Command execution (executor.py)
  * Workflow logic (langgraph_flow.py)
  * Main execution loop (main.py)

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
pip install SpeechRecognition pyaudio langgraph langchain pymongo python-dotenv openai
```

> ⚠️ If PyAudio fails on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Or use OpenAI:

```env
GEMINI_API_KEY=your_openai_api_key_here
```

---

### 5. Start MongoDB (Optional for checkpointing)

```bash
# Using Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

---

### 6. Run the Project

```bash
python main.py
```

---

## 🧪 Example Usage

```
🎤 Listening...
You: "create a new file called hello.py"

📥 Input received: "create a new file called hello.py"
🤖 Gemini Structured Output:
{
  "tool": "execute_command",
  "arguments": {
    "command": "echo. > hello.py"
  }
}
⚡ Executing...
✅ Done

You: "list files in current directory"
🤖 Gemini Structured Output:
{
  "tool": "execute_command",
  "arguments": {
    "command": "dir"
  }
}
⚡ Executing...
✅ Done

You: "exit"
Exiting CLI...
```

---

## ⚠️ Known Limitations

* Limited built-in safety measures (rely on LLM's system prompt and blocked keywords)
* Microphone input requires audio device
* MongoDB checkpoint requires local MongoDB instance (optional)
* Blocked keywords list is not fully comprehensive

---

## 🔴 Upcoming Features

* �️ Text-to-speech responses (voice feedback)
* 🧠 Enhanced intent parsing with conversation memory
* 🔐 Improved safety mechanisms (sandboxed execution mode)
* 📦 CLI packaging (installable tool via pip)
* 🎯 Task automation workflows (multi-step operations)
* 🔗 Integration with external APIs (GitHub, cloud services)

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

� **Phase 3 (Current) — LLM-Powered Execution**
- ✅ Voice input → Text conversion
- ✅ LLM-based command generation (OpenAI/Gemini)
- ✅ Safe command execution with keyword blocking
- ✅ MongoDB checkpointing & persistence
- ✅ LangGraph workflow integration

🔜 Next: Text-to-speech responses & enhanced safety