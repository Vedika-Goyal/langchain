from langchain_core.documents import Document
document=[
   Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
embedding_model=HuggingFaceEmbeddings()
vectorstores=FAISS.from_documents(
    documents=document,
    embedding=embedding_model
)
retriver=vectorstores.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":0.5}
)
query="what is langchain?"
result=retriver.invoke(query)
print(result[0].page_content)
