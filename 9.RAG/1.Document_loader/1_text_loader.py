from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

loader=TextLoader(r'C:\Users\DELL\OneDrive\Desktop\LangChain\RAG\Document_loader\cricket.txt',encoding='utf-8')

docs=loader.load()

print(docs)
print(type(docs)) #docs is a list of document object
print(len(docs))
print(docs[0])
print(type(docs[0]))
print(docs[0].page_content)
print(docs[0].metadata)

prompt=PromptTemplate(
    template='Generate summary about the poem {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke(docs[0].page_content)
print(result)