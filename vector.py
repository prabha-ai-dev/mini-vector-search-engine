import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

embedding_function = embedding_functions.DefaultEmbeddingFunction()

collection = client.create_collection(
    name="my_sentences",
    embedding_function=embedding_function
)

sentences = [
    "I love dogs",
    "Cats are cute animals",
    "I enjoy playing cricket",
    "Football is a popular sport",
    "Machine learning is interesting",
    "AI is the future",
    "I like eating pizza",
    "Healthy food is important",
    "I love programming",
    "Coding is fun"
]

collection.add(
    documents=sentences,
    ids=[str(i) for i in range(len(sentences))]
)

print(" Stored 10 sentences!")

query = "burger is my favourite"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\n Query:", query)
print("\nTop matches:")
for doc in results["documents"][0]:
    print("-", doc)