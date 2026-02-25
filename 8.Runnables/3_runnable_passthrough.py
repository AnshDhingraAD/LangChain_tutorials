# no change or processing on output , this runnable gives input as output as it is.

# we can see in op of 1_runnable_sequence.py where we used sequential runnable , we see only explanation of joke as output , but not the joke

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-Next",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Explain me this joke {joke}',
    input_variables=['joke']
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt , model , parser)

parallel_joke_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2 , model , parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_joke_chain)
result=final_chain.invoke({'topic':'AI'})
print(result)