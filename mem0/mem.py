# This project we will save the user chat and try to map relevant answer by retrieving it
# For this we are using mem0
# With this we can make llm to remember few things
from dotenv import load_dotenv
from mem0 import Memory
from google import genai
import os
import json
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# setting up config for our mem
config = {
    "version" : "v1.1",
    "embedder" : {
        "provider" : "gemini",
        "config" : {
            "model":"gemini-embedding-001"
            }
    },
    "llm":{
        "provider" : "gemini",
        "config" : {"model":"gemini-3-flash-preview"}
        },
    "vector_store" : {
        "provider" : "qdrant",
        "config" : {
            "host" : "localhost",
            "port" : 6333,
            "collection_name" : "mem0_gemini"
        }
    }
}

# creating mem memory
mem_client = Memory.from_config(config)

# initializing client 
client = genai.Client()
while True:
    user_input = input("> ")

    # searching relevant chunks
    search_memory = mem_client.search(query=user_input,user_id="user1")
    memories = [
        f"ID:{mem.get('id')}\nMemory: {mem.get('memory')}" 
        for mem in search_memory.get("results")
    ]
    
    # getting memories
    print("Found memories",memories)
    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """
    # passing system prompt with memories and user_input
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role": "system",
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    ]
)
    ai_response = response.text
    print("AI:", ai_response)

    # storing user input and ai response
    mem_client.add(
        user_id = "user1",
        messages=[
            {"role":"user","content":user_input},
            {"role":"assistant","content":ai_response}
        ]
    )

    print("Memory has been saved...")