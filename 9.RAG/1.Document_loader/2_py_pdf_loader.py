# converts a 25 page pdf into a list of 25 documents , each page is represented by a document , each having its own meta data and page content

from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('RAG/Document_loader/sample pdf.pdf')

docs=loader.load()

print(len(docs))

print(docs[0].page_content)

# py pdf loader is good for only those pdfs which have only texy in them , for other types of pdf , use other pdf loaders