from langchain_community.document_loaders import WebBaseLoader
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
    template='ANswer the following question {question} from the following text {text} ',
    input_variables=['question','text']
)
parser=StrOutputParser()
url='https://en.wikipedia.org/wiki/Success'
loader=WebBaseLoader(url)
docs=loader.load()
chain=prompt|model|parser
res=chain.invoke({'question':'what is the definition of success','text':docs[0].page_content})
print(res)