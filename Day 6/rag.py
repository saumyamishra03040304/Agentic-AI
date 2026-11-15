from retriver import load_documents
from create_embeddings import create_embeddings
from openai import OpenAI
from dotenv import load_dotenv
import os
from similarity import cosine_simlarity

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


documents = load_documents()

  
document_embedding = {}

for filename, content in documents.items():
    document_embedding[filename] = create_embeddings(content)

while True:
    user_input = input("\nYou:")
    if user_input.lower()=="quit":
        print("\nAI: Bye")
        break

    question_embedding = create_embeddings(user_input)

    best_score = -1
    best_document = None
    for filename,embedding in document_embedding.items():
        score = cosine_simlarity(question_embedding,embedding)
        if score>best_score:
            best_score = score
            best_document = filename 
    context = documents[best_document]

    prompt = f"""
Answer the question only using the following information
Context:
{context}
Question:
{user_input}
"""


    response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = [
        {
            "role":"user",
            "content":prompt
        }
    ]
)
   # display response
    print(response.choices[0].message.content)

