from langchain_community.document_loaders import WebBaseLoader 
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

url='https://www.amazon.in/Apple-2025-MacBook-Laptop-10%E2%80%91core/dp/B0FWD8YR67/ref=sr_1_7?crid=26MX1EY6ID6BQ&dib=eyJ2IjoiMSJ9.asb3l5WT-2IvI1DgvMjmGm4serspOXRbI-N_Bc1Rp_LwiTEXFUfYKkt9CVGflHBBelp4c5GZzkUTNTCR7RLN3FCvGIBT825kY6NDE0HJdbQw4geQWTppvJlR4gh9uGW6QUl-lvyaIR_jx51YmO8BXAngCyadQdFOmcuu0LIWr4_iRhGOiqo9532qe2kc0TYpOl58BL8sMKijLIXXEsvX4JhDHaktFlZc0-AlN1ktOOk.8ibF7Wz076KCFah37z8ae7wdTRhLkFY2b8pIcpGGSZU&dib_tag=se&keywords=macbook+m4&qid=1771439623&sprefix=mac%2Caps%2C372&sr=8-7'

loader=WebBaseLoader(url)
docs=loader.load()

# print(len(docs))
# print(docs[0].page_content)

prompt=PromptTemplate(
    template='Answer the following questions \n {question} from the text \n {text}',
    input_variables=['question','text']
)

parser=StrOutputParser()

chain=prompt | model | parser

print(chain.invoke({'question':'What is the product we are talking about','text':docs[0].page_content}))