from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)
prompt1=PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a linkedin post {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkedin':RunnableSequence(prompt2,model,parser)
    }
)
print(parallel_chain.invoke({'topic':'AI'}))