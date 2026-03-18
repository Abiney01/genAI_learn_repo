import os 
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
SYSTEM_PROMPT = """
You are a CLI assistant.

Your job:
- Convert user requests into SAFE shell commands.
- Focus on development tasks (files, folders, running scripts, project setup).
- NEVER delete anything.
- NEVER run destructive commands.
- Prefer safe, reversible operations.
- for your reference i'm using windows command prompt

You MUST respond with EXACTLY ONE JSON object.

Format:
{
  "tool": "execute_command",
  "arguments": {
    "command": "<shell command>"
  }
}
"""
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def generate_command(user_input:str):
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    content = response.choices[0].message.content
    try:
        parsed = json.loads(content)
        return parsed
    except:
        return {
            "tool": "none",
            "arguments": {
                "command": "echo 'Invalid response from LLM'"
            },
            "raw": content
        }