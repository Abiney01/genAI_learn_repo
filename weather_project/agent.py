import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

def get_weather(city):
    url = f"http://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    return "Something went wrong"

SYSTEM_PROMPT = """
    You are a tool-calling agent for weather queries.

    Rules:
    - You operate as a finite state machine.
    - You output EXACTLY one JSON object per response.
    - Valid steps: START, PLAN, TOOL, OUTPUTR

    TOOL step format:
    {
    "step": "TOOL",
    "content": {
        "name": "get_weather",
        "arguments": {
            "city": "<city-name>"
        }
    }
    }

    Never call tools yourself.
    Only request tools using TOOL step.
"""


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def run_agent(user_query):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

    next_step = "START"

    while True:
        messages.append({
            "role": "user",
            "content": f"Respond ONLY with step {next_step} as a single JSON object."
        })

        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=messages
        )

        assistant_msg = response.choices[0].message.content
        print("\n🤖:", assistant_msg)

        data = json.loads(assistant_msg)
        step = data["step"]

        messages.append({"role": "assistant", "content": assistant_msg})

        if step == "START":
            next_step = "PLAN"

        elif step == "PLAN":
            next_step = "TOOL"

        elif step == "TOOL":
            tool_name = data["content"]["name"]
            city = data["content"]["arguments"]["city"]

            tool_result = get_weather(city)

            messages.append({
                "role": "user",
                "content": f"Tool get_weather returned: {tool_result}"
            })

            next_step = "OUTPUTR"

        elif step == "OUTPUTR":
            break

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

def main():
    user_query = input("Input: ")
    run_agent(user_query)
main()
