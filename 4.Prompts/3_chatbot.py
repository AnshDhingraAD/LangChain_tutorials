from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input=input('YOU: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        print(chat_history)
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: " ,result.content)