# MessagesPlaceholder is used inside ChatPromptTemplate to dynamically insert chat history or a list of messaes at runtime.

from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]
with open('3.Prompts/5.1_chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt=chat_template.invoke({'chat_history':chat_history , 'query':'Where is my refund'})

print(prompt)