from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-4.1-mini')

result=llm.invoke("What is capital of India?")

print(result.content)


# llm models are not used much now , instead we use chat models 