from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-Coder-Next',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model=ChatHuggingFace(llm=llm)
result=model.invoke('what is the capital of india?')

print(result.content)

# by running this code , the model is downloaded locally on pc and then output is generated
