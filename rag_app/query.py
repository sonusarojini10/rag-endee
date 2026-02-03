from endee import Endee
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Endee()

try:
    index = client.get_index("rag_index")
except Exception as e:
    print("⚠️ Endee server not running or index unavailable.")
    print("Details:", e)
    exit(0)

query = input("Enter your question: ")
query_vector = model.encode(query).tolist()

results = index.search(
    vector=query_vector,
    top_k=2
)

print("\n🔎 Retrieved Context:\n")
for i, r in enumerate(results, 1):
    print(f"{i}. {r['document']}\n")
