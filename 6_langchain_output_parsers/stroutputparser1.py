from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
parser=StrOutputParser()
chain=temp1 | model | parser | temp2 | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)