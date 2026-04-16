from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ["LANGCHAIN_PROJECT"] ="Chatbot -1"


prompt=ChatPromptTemplate.from_messages([
    ('system','You are a helpful assistant. Please respond to the user queries'),
    ('user' , 'Question :{Question}')
])

st.title('Chatbot')
input_text=st.text_input("Give me any question...")

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain=prompt | model | parser

if input_text:
    st.write(chain.invoke({'Question':input_text}))
