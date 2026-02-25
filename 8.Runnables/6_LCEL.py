# since runnable sequence is used everywhere , langchain thought that the defining runnable sequence like this->
# chain=RunnableSequence(prompt , model , parser , prompt2 , model , parser)  
# it can be defined by chain=prompt | model | parser | prompt2 | model | parser

# this pipe operator (|) in langchain is called as lcel

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda , RunnableBranch
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables={'topic'}
)

prompt2=PromptTemplate(
    template='summarize the following text {text}',
    input_variables=['text']
)

parser=StrOutputParser()

report_gen_chain=prompt1 | model | parser
branch_chain=RunnableBranch(
    (lambda x : len(x.split())>500 , prompt2 | model | parser ),
    (RunnablePassthrough())   
)
final_chain=report_gen_chain | branch_chain
result=final_chain.invoke({'topic':'AI'})
print(result)