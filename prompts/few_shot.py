import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = '''
                       you're a expert in solving technical questions related to coding, but if someone ask other than that say 'sorry google it bro' 
                       Q. Who is the founder of python
                       A. Guido Van Rossum (since it is related to coding you can answer)
                       Q. Who is the father of economics
                       A. Sorry google it bro!
                    '''

# the above system prompt is called as few shot prompting since we have given with examples it makes it different from zero shot
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages= [
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content" : "who is the father rust"
        }
    ]
)
print(response.choices[0].message.content)