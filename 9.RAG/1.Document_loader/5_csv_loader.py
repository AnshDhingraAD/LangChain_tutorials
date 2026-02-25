# it creates a document object of each row , here too we can use lazy_loader
from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path=r'C:\Users\DELL\OneDrive\Desktop\LangChain\9.RAG\1.Document_loader\sample_dataset.csv')

docs=loader.load()

print(docs[0])
print(len(docs))