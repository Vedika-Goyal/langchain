from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Write a joke abput {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Explain the joke {text}',
    input_variables=['text']
)
parser=StrOutputParser()
chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(chain.invoke({'topic':'AI'}))