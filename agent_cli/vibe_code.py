# This is a simple agent cli project which performs small task like creating files or directories you can think it like a vibe code simulation 

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def execute_command(command: str):
    return os.system(command)

SYSTEM_PROMPT = """
You are a CLI assistant.

Your job:
- Convert user requests into SAFE shell commands.
- Only create folders or files.
- NEVER delete anything.
- NEVER run destructive commands.

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

def run_cli():
    print("🧠 Simple CLI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        assistant_msg = response.choices[0].message.content
        print("\n🤖:", assistant_msg)

        try:
            data = json.loads(assistant_msg)
            command = data["arguments"]["command"]

            print(f"\n🛠 Executing: {command}")
            result = execute_command(command)

            print("✅ Done\n")

        except Exception as e:
            print("❌ Failed to execute command:", e)

if __name__ == "__main__":
    run_cli()


