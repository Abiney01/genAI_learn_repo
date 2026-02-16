# 🤖 Agentic AI Repository

A comprehensive collection of AI agent projects demonstrating various prompt engineering techniques, LLM integrations, and advanced AI applications using Google Gemini and OpenAI APIs.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Projects](#projects)
  - [Hello AI](#hello-ai)
  - [Prompts](#prompts)
  - [Agent CLI](#agent-cli)
  - [LangGraph Learn](#langgraph-learn)
  - [Weather Project](#weather-project)
  - [Image Analysis](#image-analysis)
  - [RAG System](#rag-system)
  - [RAG Queue](#rag-queue)
  - [Tokenization](#tokenization)
  - [Agent Project](#agent-project)
- [Technologies](#technologies)
- [Quick Start Guide](#quick-start-guide)
- [Environment Setup](#environment-setup)
- [Contributing](#contributing)

---

## 🎯 Overview

A comprehensive collection of AI agent projects with:
- LLM integrations (Gemini, OpenAI)
- Prompt engineering techniques
- Tool-calling agents & RAG systems
- Async queue processing
- Vision capabilities & CLI tools

---

## 📁 Project Structure

```
agentic_ai_repo/
├── hello_ai/                  # Basic LLM integration examples
├── prompts/                   # Prompt engineering techniques showcase
├── agent_cli/                 # CLI-based AI agent
├── langraph_learn/            # LangGraph state management & workflow patterns
├── weather_project/           # Tool-calling weather agent
├── image/                     # Image analysis using vision models
├── rag/                       # RAG system with Qdrant vector database
├── rag_queue/                 # Async RAG with Redis queue
├── tokenization/              # Token encoding/decoding utilities
├── agent_project/             # Web-based agent project
├── requirements.txt           # Global dependencies
└── README.md                  # This file
```

---

## 📦 Prerequisites

- Python 3.9+
- pip package manager
- API Keys: GEMINI_API_KEY (required), OPENAI_API_KEY (optional)
- Docker & Docker Compose (for RAG projects)

---

## 🚀 Installation

```bash
# 1. Clone repo
git clone <repository-url> && cd agentic_ai_repo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup .env
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Start Docker services (for RAG)
docker-compose -f rag/docker-compose.yml up -d
docker-compose -f rag_queue/docker-compose.yml up -d
```

---

## 🎮 Projects

| Project | Location | Description | Command |
|---------|----------|-------------|---------|
| **Hello AI** | [hello_ai/](hello_ai/) | Basic Gemini API integration | `cd hello_ai && python main.py` |
| **Prompts** | [prompts/](prompts/) | Zero-shot, Few-shot, CoT, Persona | `python prompts/zero_shot.py` |
| **Agent CLI** | [agent_cli/](agent_cli/) | CLI agent for file/folder creation | `cd agent_cli && python vibe_code.py` |
| **LangGraph Learn** | [langraph_learn/](langraph_learn/) | State management & workflow orchestration with LangGraph | `cd langraph_learn && python sample_chat.py` |
| **Weather** | [weather_project/](weather_project/) | Tool-calling weather agent | `cd weather_project && python agent.py` |
| **Image Analysis** | [image/](image/) | Vision model for image description | `cd image && python main.py` |
| **RAG System** | [rag/](rag/) | Semantic search on PDF documents | `docker-compose -f rag/docker-compose.yml up -d && python rag/index.py && python rag/chat.py` |
| **RAG Queue** | [rag_queue/](rag_queue/) | Async RAG with Redis queue | `docker-compose -f rag_queue/docker-compose.yml up -d && python rag_queue/main.py` |
| **Tokenization** | [tokenization/](tokenization/) | Token encoding/decoding | `cd tokenization && python main.py` |
| **Web Project** | [agent_project/](agent_project/) | HTML/CSS/JS web interface | Open `index.html` in browser |

---

## 🛠 Technologies

| Category | Technologies |
|----------|--------------|
| **Languages** | Python 3.9+ |
| **LLM APIs** | Google Gemini, OpenAI, LangChain |
| **Graph Framework** | LangGraph |
| **Web Framework** | FastAPI, Uvicorn |
| **Data & Validation** | Pydantic, Marshmallow |
| **Vector Database** | Qdrant |
| **Task Queue** | Redis, RQ |
| **Embeddings** | Google GenerativeAI Embeddings |
| **Tokenization** | Tiktoken |
| **Frontend** | HTML5, CSS3, JavaScript |

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup .env with API keys
echo "GEMINI_API_KEY=your_key" > .env

# 3. Run a quick project
cd hello_ai && python main.py

# 4. Try another project
cd ../agent_cli && python vibe_code.py

# 5. Setup RAG (needs Docker)
docker-compose -f rag/docker-compose.yml up -d
```

---

## 🔐 Environment Variables

Create `.env` file in root:
```
GEMINI_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key (optional)
QDRANT_URL=http://localhost:6333
REDIS_URL=redis://localhost:6379
```

Get keys from:
- Google Gemini: https://aistudio.google.com/app/apikey
- OpenAI: https://platform.openai.com/api-keys

---

## 📚 Prompt Engineering Techniques

| Technique | Use Case | Complexity |
|-----------|----------|-----------|
| Zero-Shot | Simple direct tasks | Easy |
| Few-Shot | Example-based tasks | Medium |
| Chain-of-Thought | Complex reasoning | Hard |
| Persona | Role-based responses | Medium |
| Tool-Calling | API integration | Hard |

---

## 🔗 API Samples

**Gemini API Call**
```python
from openai import OpenAI
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), 
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
response = client.chat.completions.create(model="gemini-3-flash-preview",
                                          messages=[{"role":"user","content":"Hi"}])
```

**Vector Store Query**
```python
from langchain_qdrant import QdrantVectorStore
vector_db = QdrantVectorStore.from_documents(documents=chunks, embedding=embedding_model,
                                             url="http://localhost:6333", collection_name="rag")
```

**FastAPI RAG Endpoint**
```python
@app.post("/chat")
def chat(query: str = Query(...)):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}
```

---

## � Contributing

1. Fork the repo
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

**Code Standards**: Follow PEP 8, add comments, include docstrings.

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `GEMINI_API_KEY not found` | Check `.env` file exists in root directory |
| `Connection refused for Qdrant` | Run `docker-compose -f rag/docker-compose.yml up -d` |
| `Redis connection error` | Run `docker-compose -f rag_queue/docker-compose.yml up -d` |
| `Module not found` | Run `pip install -r requirements.txt` |

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🌟 Features

✅ Multiple LLM integrations | ✅ 5+ prompt techniques | ✅ Tool-calling agents
✅ RAG with vector DB | ✅ Async processing | ✅ Vision models | ✅ Production-ready

**Last Updated**: February 2026 | **Version**: 1.0.0
