from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader=DirectoryLoader(
    path=r'C:\Users\DELL\OneDrive\Desktop\LangChain\9.RAG\1.Document_loader\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()   #use lazy_load at place of load here to see the difference

print(len(docs))  #each page of each pdf is 1 document , therefore the length of docs is equal to sum of number of pages in all pdfs

print(docs[0].page_content)
print(docs[0].metadata)

# problem of this loader is that it is time consuming and also it loads every pdf present inside the directory.

# therefore instead of using load we use lazy load which returns a generator of document objects and documents are not all loaded at once , they are fetched one at a time as needed, meanwhile the load returns a list of document objects and loads all documents immediately into the memory.

for document in docs:
    print(document.metadata)