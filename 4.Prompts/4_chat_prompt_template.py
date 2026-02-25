# the chat prompt template class is used for dynamic list of messages to be sent to llm. 
# we used  prompt template class but that was for single dynamic message , whereas chat prompt template is for dynamic list of messages that we use for chatbot application
# and here we do not need SystemMessage , HumanMessage classes

from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Tell me about {topic} in simple terms')
])

prompt=chat_template.invoke({'domain':'cricket','topic':'wicket'})

print(prompt)
