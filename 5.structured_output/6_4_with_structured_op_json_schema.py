from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict , Annotated ,Optional , Literal
from pydantic import BaseModel , Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3-Coder-Next',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}



structured_model = model.with_structured_output(json_schema)

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

