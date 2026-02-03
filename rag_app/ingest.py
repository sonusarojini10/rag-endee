from endee import Endee
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


client = Endee()

index_name = "rag_index"


try:
    if index_name not in client.list_indexes():
        client.create_index(
            name=index_name,
            dimension=384,
            metric="cosine"
        )
    index = client.get_index(index_name)
    server_available = True
except Exception as e:
    print("⚠️ Endee server not running or not accessible.")
    print("Details:", e)
    server_available = False


if not server_available:
    print("\nℹ️ Ingestion skipped. Start Endee server to enable full ingestion.")
    exit(0)


with open("rag_app/data/sample.txt", "r", encoding="utf-8") as f:
    documents = f.read().split("\n\n")


for i, doc in enumerate(documents):
    embedding = model.encode(doc).tolist()
    index.add(
        ids=[str(i)],
        vectors=[embedding],
        documents=[doc],
        metadata=[{"source": "sample.txt"}]
    )

print("✅ Documents successfully ingested into Endee vector database")
