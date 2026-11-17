from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field
class MultiplyInput(BaseModel):
    a:int=Field(...,description="the first number")
    b:int=Field(...,description="the second number")
def multiply_func(a:int,b:int)->int:
    return a*b 
multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two num",
    args_schema=MultiplyInput
)   
result=multiply_tool.invoke({"a":3,"b":5})
print(result)
