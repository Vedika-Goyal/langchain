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
    template='Generate five interesting facts about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
chain=prompt | model | parser
result=chain.invoke({'topic':'India'})
print(result)
chain.get_graph().print_ascii()
