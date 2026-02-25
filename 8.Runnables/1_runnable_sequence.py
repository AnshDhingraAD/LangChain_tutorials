from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task='text-generation',
    max_new_tokens=200,
    temperature=0.7

)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Explain me this joke {joke}',
    input_variables=['joke']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt , model , parser , prompt2 , model , parser)

print(chain.invoke({'topic':'AI'}))