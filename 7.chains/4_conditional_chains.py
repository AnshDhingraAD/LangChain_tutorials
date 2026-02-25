# reply on the basis of feedback -> pos or neg

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Positive' , 'Negative'] = Field(description='Give the sentiment of the given feedback')

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text in positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='You are in customer support team , Generate a response for this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='You are in customer support team ,Generate a response for this negative feedback \n {feedback}',
    input_variables=['feedback']
)


classify_chain = prompt1 | model | parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='Positive' , prompt2 | model | parser),
    (lambda x:x.sentiment=='Negative' , prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find the feedback")
)

final_chain = classify_chain | branch_chain

print(final_chain.invoke({'feedback':'this is a terrible phone'}))

final_chain.get_graph().print_ascii()