from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import Optional, Literal
from pydantic import BaseModel, Field

# 1. Added strict parameters back to the LLM to force clean JSON
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="YOUR_NEW_TOKEN", # Stay safe!
    temperature=0.1,
    return_full_text=False,
    max_new_tokens=512
)
model = ChatHuggingFace(llm=llm)

# 2. Fixed the Literal values to match the description exactly
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="Return sentiment of the review: positive, negative, or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)

# 3. Removed the contradictory instructions from the prompt
result = structured_model.invoke("""Output ONLY a valid JSON object. Do not add any extra text, markdown formatting, or explanation.

Review:
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Vedika Goyal""")

# 4. Safely print the result
if result:
    print(result.name)
else:
    print("Parsing failed. The model did not return valid JSON.")