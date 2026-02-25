from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents=[
    "Delhi is the capital of India",
    "Gurugram is in Haryana",
    "Bangalore is in south of India"
]

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
vector=embedding.embed_documents(documents)

print(str(vector))