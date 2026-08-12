from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
     huggingfacehub_api_token="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"
)
model=ChatHuggingFace(llm=llm)
chatHistory=[
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input=input('You: ')
    chatHistory.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break
    result=model.invoke(chatHistory)
    chatHistory.append(AIMessage(result.content))
    print("AI: ",result.content)