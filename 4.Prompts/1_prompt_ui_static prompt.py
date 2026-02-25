from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

st.header('AI Research Tool')

user_input=st.text_input("Enter your prompt here")

if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)

# Prompts are of 2 types:
# Static Prompt:
# A fixed instruction sent to an LLM that does not change at runtime.

# Dynamic Prompt:
# A prompt template that injects variables, user input, or context dynamically before sending to the LLM.

# we do not use static prompts now , instead we use dynamic prompts.
