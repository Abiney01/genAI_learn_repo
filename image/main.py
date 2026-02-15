import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role":"user",
            "content":[
                {"type":"text","text":"Describe this image beautifully in about 50 words"},
                # we can also provide image url or image to do any task for this the model must be capable of understanding image 
                {
                    "type":"image_url",
                    "image_url":{
                        "url":"https://images.pexels.com/photos/35758271/pexels-photo-35758271.jpeg"
                    }
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)