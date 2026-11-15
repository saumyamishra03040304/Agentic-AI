# USING TOOLS - remove the if statements and used tool_manager.py instead. Lot of if statements make code longer (suppose there are 100 tools)

from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool
# load configuration from the .env file
load_dotenv()

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}


#create a client that communicates with ollama
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)
print("="*40)
print("  My Assistant")
print("="*40)

print("\nChoose Your Assistant\n")
print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice:")
Messages = [
    {
        "role":"system",
         "content":roles.get(choice, "You are a helpful AI assistant") 
        # 2nd argument tab use hoga agar user koi galat choice karle joki present hi na ho like 99 tab AI normal assistant ki tarah behave karega
    }
]
while True:
    user_input = input("\nYou: ")
    tool_result = execute_tool(user_input)
    if tool_result:
        print("\nAI: ",tool_result)
        continue
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

