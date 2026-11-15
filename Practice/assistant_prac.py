from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior coder. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced traveller. Recommend places, food, transportation and travel tips.",

    "4": "You are a doctor. Prescribe medicines for various diseases.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)


print("\nChoose Your Assistant\n")
print("1. Teacher")
print("2. Coder")
print("3. Travellere")
print("4. Doctor")
print("5. Interviewer")

choice = input("\nEnter your choice:")

Messages = [
    {
        "role":"system",
        "content":roles.get(choice, "You are a helpful assistant")
    }
]
while True:
    query = input("\nUser:")
    Messages.append(
        {
            "role":"user",
            "content":query
        }
    )
    if query.lower() == "quit":
        print("\nAI: Bye")
        break
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages=Messages
    )
    ai_reply = response.choices[0].message.content
    Messages.append(
        {
            "role":"assistant",
            "content":ai_reply
        }
    )
    print("\nAI: "+ai_reply)

