from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)
prompt=PromptTemplate(
    template='Write a summary for the following poem {poem}',
    input_variables=['poem']
)
parser=StrOutputParser()
from langchain_community.document_loaders import TextLoader
loader=TextLoader('cricket.txt',encoding='utf-8')
docs=loader.load()
print(docs)
print(type(docs))
chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))
