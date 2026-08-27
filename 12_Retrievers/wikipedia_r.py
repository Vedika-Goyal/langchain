from langchain_community.retrievers import WikipediaRetriever
retriver=WikipediaRetriever(top_k_results=2,lang="en")
query="tell me about arijit singh"
docs=retriver.invoke(query)
print(docs)