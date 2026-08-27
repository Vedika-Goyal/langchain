from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""In Rígsþula, Rig wanders through the world and fathers the progenitors of the three classes of human beings as conceived by the poet. The youngest of these sons, Jarl ('earl, nobleman'), inherits the name or title "Ríg" and so in turn does his youngest son, Kon the Young or Kon ungr (Old Norse: konungr, king). This third Ríg was the first true king and the ultimate founder of the state of royalty as appears in the Rígsþula and in two other associated works. In all three sources he is connected with two primordial Danish rulers named Dan and Danþír."""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)
