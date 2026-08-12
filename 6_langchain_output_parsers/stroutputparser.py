from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)
temp1=PromptTemplate(
    template='tell me about the {topic}',
    input_variables=['topic']
)

temp2=PromptTemplate(
    template='Write a 5 line summary on the following text {text}',
    input_variables=['text']
)
prompt1=temp1.invoke({'topic':'black hole'})
result=model.invoke(prompt1)
prompt2=temp2.invoke({'text':result.content})
result1=model.invoke(prompt2)
print(result1.content)
