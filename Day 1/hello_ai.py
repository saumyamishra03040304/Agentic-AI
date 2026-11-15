from openai import OpenAI
from dotenv import load_dotenv
import os

# load configuration from the .env file
load_dotenv()

#create a client that communicates with ollama
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)
response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = [
        {
            "role":"user",
            "content":"define AI"
        }
    ]
)

# display response
print(response.choices[0].message.content)