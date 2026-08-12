from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model1=ChatHuggingFace(llm=llm)
model2=ChatHuggingFace(llm=llm)
model3=ChatHuggingFace(llm=llm)
prompt1=PromptTemplate(
    template='Generate notes from the text {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate 5 short questions from the text {text}',
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document {notes} and {quiz}',
    input_variables=['notes','quiz']
)
parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        'notes':prompt1|model1|parser,
        'quiz':prompt2|model2|parser
    }
)
merge_chain=prompt3|model1|parser
chain=parallel_chain|merge_chain
result=chain.invoke({'text':'Hello tell me about india '})
print(result)

