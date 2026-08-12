from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict,Annotated



llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="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", 
    
)
model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    key_themes:Annotated[list[str],"Write all the key theme discussed in the review"]
    summary: Annotated[str,"A brief Summary of the review"]
    sentiment: Annotated[str,"Return sentiment of the review negative positive or neutral"]
    pros:Annotated[list[str],"write down all the pros inside a list"]
    cons:Annotated[list[str],"write down all the cons inside a list"]
    
structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""Output ONLY a valid JSON object with the keys 'summary' and 'sentiment'. Do not add any extra text or explanation.

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

print(result)