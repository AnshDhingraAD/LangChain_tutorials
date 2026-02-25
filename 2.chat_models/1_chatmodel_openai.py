from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_tokens=100)

result=model.invoke("Write a 5 line poem on cricket")

print(result.content)

# temperature here refers to creativity of the model here , if set to 0 , the llm provides same resultfor the same prompt each time but if set close to 1-1.5 , the output changes each time and becomes more creative

