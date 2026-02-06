import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages= [
        # here the first prompt is called as system prompt and we have given the instructions directly -> this is known as zero shot prompting 
        {
            "role" : "system",
            "content" : "you're a expert in solving technical questions related to coding, but if someone ask other than that say 'sorry google it bro'"
        },
        {
            "role": "user",
            "content" : "who is the father of our nation"
        }
    ]
)
print(response.choices[0].message.content)