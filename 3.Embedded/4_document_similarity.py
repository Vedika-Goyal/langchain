from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
documents=[
    "Rohit sharma is known for his elegant batting and record breaking double centuries",
    "Sachin tendular also known as the 'God of Cricket' holds many batting records",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers"
]
query='tell me about rohit sharma'
doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)
scores=(cosine_similarity([query_embedding],doc_embedding)[0])
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(documents[index])
print("similarity score is: ",score)