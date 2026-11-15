from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

def choose_tool(user_request):
    planner_prompt = f"""
You are an AI planner.
Available tools:
1. get_current_time
   Use when the user sks for the current date or time.
2. roll_dice:
   Use when user asks to roll a dice.
3. generate_password:
   Use when user wants a secure password.
If no tool i required, return:
None
Reuturn ONLY the tool name.
user request:{user_request}
"""
    response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages=[
        {
            "role":"system",
            "content":"you are an AI planner"
        },
        {
            "role":"user",
            "content":planner_prompt
        }
    ]
)
    return response.choices[0].message.content.strip()

