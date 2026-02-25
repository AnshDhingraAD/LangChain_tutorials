from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template='Give me name , place and age of a fictional character. \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template | model | parser

result=chain.invoke({})
print(result)

# the problem with json output parser is that it has a fixed schema , we can not define our own schema to it. It does not enforce a schema , we use structured_output_parser for this which gives us structured json output