from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)
class Person(BaseModel):
    name: str=Field(description='Name of the person')
    age: int=Field(gt=18,description='Age of a person')
    city:str=Field(description='city')
parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Generate the name,city and age of a fictional {place}perosn \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)    
prompt=template.invoke({'place':'indian'})
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)