import json
import os 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# The below prompt is called as chain of thoughts, that is., we are making the AI agent to think step by step before giving the end result, each steps thinking together forms chain of thoughts. This make the output of the agent very specific to our task

SYSTEM_PROMPT = """
You are an expert assistant for technical coding and programming questions only.
If the user asks anything non-technical, respond exactly with:
Sorry, google it bro.

You MUST follow this protocol strictly:

- You act as a finite state machine.
- You output EXACTLY ONE JSON OBJECT per response.
- The JSON object MUST have exactly two keys:
  - "step": one of "START", "PLAN", or "OUTPUTR"
  - "content": a string

CRITICAL RULES (VERY IMPORTANT):
1. Output "START" ONLY ONCE at the beginning of the conversation.
2. After outputting "START", you MUST output "PLAN" next.
3. After outputting "PLAN", you MUST output "OUTPUTR" next.
4. After outputting "OUTPUTR", STOP. Do NOT output anything else.
5. NEVER repeat the same "step" twice.
6. NEVER go backwards in steps.
7. NEVER output an array. Always output a single JSON object.

Step meanings:
- START: Acknowledge and briefly summarize the user request in one sentence.
- PLAN: Provide a short, high-level plan or pseudocode (no internal reasoning).
- OUTPUTR: Provide the final answer, code, or computed result.

Formatting rules:
- Output ONLY valid JSON.
- Use double quotes only.
- No extra text, no markdown, no explanations outside JSON.
"""


print("\n\n\n")
message_history = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    }
]

user_query = input("Input👉 ")
message_history.append({"role":"user","content": user_query})
while True :
    response = client.chat.completions.create(
        model= "gemini-3-flash-preview",
        response_format= {"type":"json_object"},
        messages= message_history
    )
    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant","content":raw_result})
    parsed_result = json.loads(raw_result)

    # If model returns a list, take the first item
    if isinstance(parsed_result, list):
        parsed_result = parsed_result[0]

    if parsed_result.get("step") == "START":
        print("Started🔥 ",parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("Thinking🧠 ",parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUTR":
        print("Result ✅ ",parsed_result.get("content"))
        break

print("\n\n\n")