from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
parser=JsonOutputParser()
model=ChatHuggingFace(llm=llm)
template=PromptTemplate(
    template='Give me the name,age and city of a fictional person {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template | model | parser
result=chain.invoke({})
print(result)

