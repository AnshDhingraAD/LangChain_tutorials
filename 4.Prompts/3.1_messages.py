from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.messages import SystemMessage , AIMessage , HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are an AI assistant'),
    HumanMessage(content='tell me about langchain')
]

result=model.invoke(messages)         
messages.append(AIMessage(content=result.content))

print(messages)