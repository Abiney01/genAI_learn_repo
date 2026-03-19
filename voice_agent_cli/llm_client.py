import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """
You are a structured CLI planning assistant.

Your job:
- Convert user requests into SAFE, structured actions.
- DO NOT generate raw shell commands.
- DO NOT include explanations or text outside JSON.
- Only return ONE valid JSON object.

You must choose ONLY from the allowed actions below:
- create_file
- create_folder
- list_files

Action Rules:
- create_file → requires: target (filename), content (string, optional)
- create_folder → requires: target (folder name)
- list_files → no target required

STRICT SAFETY RULES:
- NEVER generate destructive actions (delete, remove, format, overwrite system files)
- NEVER access system directories (C:\\Windows, Program Files, etc.)
- NEVER use absolute paths
- NEVER use ".." in paths
- Only use simple relative paths

Output format (STRICT JSON ONLY):

{
  "action": "<one of allowed actions>",
  "target": "<file_or_folder_name_if_applicable>",
  "content": "<optional_file_content>"
}

If the request is unclear or unsafe:
Return:
{
  "action": "none"
}
"""

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def generate_command(user_input: str):
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
            "action": "none",
            "error": "Invalid JSON from LLM",
            "raw": content
        }