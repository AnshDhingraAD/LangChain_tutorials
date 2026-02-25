from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict , Annotated ,Optional , Literal

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

# schema
class review(TypedDict):
    key_themes:Annotated[list[str],'write down all the key themes from the review in a list']
    summary:Annotated[str , 'A brief summary of the review']
    sentiment:Annotated[Literal['pos','neg'] , "return sentiment of the review"]
    pros:Annotated[Optional[list[str]],'write down all the pros from the review inside the list']
    cons:Annotated[Optional[list[str]],'write down all the cons from the review inside the list']

structured_model = model.with_structured_output(review)

result=structured_model.invoke("""The OnePlus 12 is a flagship smartphone focused on performance, display quality, and ultra-fast charging. Powered by the Snapdragon 8 Gen 3 chipset with up to 16 GB RAM, it handles gaming and multitasking effortlessly. Its large AMOLED display with 120 Hz refresh rate delivers vibrant visuals, while the 5,400 mAh battery ensures long usage with extremely fast wired and wireless charging.

Pros

Excellent flagship performance (Snapdragon 8 Gen 3)

Bright, high-resolution AMOLED display with 120 Hz refresh rate

Very fast charging + strong battery life

Smooth OxygenOS experience

Premium design and build quality

Cons

Camera not the absolute best vs top rivals

Software update support shorter than competitors

Limited AI features compared to some flagship phones

Premium price segment""")

print(result)
print(result['sentiment'])
