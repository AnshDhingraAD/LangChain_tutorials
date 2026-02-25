# Your password encrypts your private keys using AES-256-GCM encryption. This password is required to access your wallet and cannot be recovered if lost. Please store it securely.

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(r'C:\Users\DELL\OneDrive\Desktop\LangChain\9.RAG\1.Document_loader\books\sample1.pdf')

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,  #it refers to the comman characters between 2 chunks ,helps to retain context , but increases the number of chunks
    separator=''
)

result=splitter.split_documents(docs)

# print(result)

print(result[0].page_content)

#for a RAG nased application , it is observed that performance is good when chunk overlap is 10% to 20% of chunk size