from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Generate a joke about topic {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

def word_counter(text):
    return len(text.split())

joke_gen_chain=RunnableSequence(prompt , model , parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_counter)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'AI'})
print(result)