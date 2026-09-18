#Step 1: Setup Groq API Key
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step 2:Convert Image to required format
import base64

# image_path="acne.png"
def encode_image(image_path):
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step 3:Setup MultiModal LLM
from groq import Groq

query="Is there something wrong with my face?"
model="qwen/qwen3.8-27b"
def analyze_image_with_query(query,model,encoded_image):
    client=Groq(api_key=GROQ_API_KEY)
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}",
                        },
                    },
                ],
            }]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return (chat_completion.choices[0].message.content)