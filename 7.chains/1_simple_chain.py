from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Generate 5 interesting facts about the {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

chain = prompt | model | parser

result=chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()