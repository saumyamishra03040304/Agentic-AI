from openai import OpenAI
import os
from dotenv import load_dotenv
from similarity import cosine_simlarity

load_dotenv()
client = OpenAI(
    base_url= os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

response = client.embeddings.create(
    model = "nomic-embed-text",
    input = "Python is a programming language"
)
embedding = response.data[0].embedding
# print(type(embedding))
# print(len(embedding))

text1 = "Python is a programming language"
text2 = "Python is used for software development"

embedding1 = client.embeddings.create(
    model= "nomic-embed-text",
    input = text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model="nomic-embed-text",
    input = text2
).data[0].embedding
# print(len(embedding1))
# print(len(embedding2))

sentence1 = "python is a programming language"
sentence2 = "python is used for software development"
sentence3 = "Pizza is delicious"

emb1 = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence1
).data[0].embedding

emb2 = client.embeddings.create(
    model="nomic-embed-text",
    input = sentence2
).data[0].embedding

emb3 = client.embeddings.create(
    model = "nomic-embed-text",
    input = sentence3
).data[0].embedding
score1 = cosine_simlarity(emb1,emb2)
score2 = cosine_simlarity(emb1,emb3)
# print(score1)
# print(score2)

def create_embeddings(content):
    Embedding = client.embeddings.create(
        model = "nomic-embed-text",
        input = content
    ).data[0].embedding 
    return Embedding