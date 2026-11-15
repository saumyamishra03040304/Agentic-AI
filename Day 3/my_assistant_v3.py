#  WITH SYSTEM PROMPT - PROMPT WHICH TELLS ASSISTANCE IT'S ROLE

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
print("="*40)
print("My Assistant")
print("="*40)

Messages = [
    {
        "role":"system",
        "content":"You are a friendly AI teacher. Explain every concept in a simple language with real life examples"
    }
]
while True:
    user_input = input("\nYou: ")
    Messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )
    if user_input.lower()=="quit":
        print("\nAI: Bye")
        break
    else:
        response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = Messages
)
     # display response
    ai_reply = response.choices[0].message.content
    print("AI: "+ai_reply)
    Messages.append(
        {
            "role":"assistant",
            "content":ai_reply
        }
    )

