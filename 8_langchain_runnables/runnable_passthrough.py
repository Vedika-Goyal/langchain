from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
passthrough=RunnablePassthrough()
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
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'explanation':RunnableSequence(prompt2,model,parser)
    }
)
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'AI'}))