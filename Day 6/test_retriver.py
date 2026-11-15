from retriver import load_documents,retrive

# documents = load_documents()

# for name,text in documents.items():
#     print(name)
#     print(text)
#     print("-"*40)

filename, content = retrive("weather")
print(filename)
print()
print(content)