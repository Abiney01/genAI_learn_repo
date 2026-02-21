from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

# Connect to local Qdrant
client = QdrantClient(host="localhost", port=6333)

collection_name = "mem0_gemini"

# Delete existing collection (if exists)
if client.collection_exists(collection_name):
    client.delete_collection(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Recreate collection with correct Gemini embedding dimension
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=768,  # Gemini embedding dimension
        distance=Distance.COSINE,
    ),
)

print(f"Collection '{collection_name}' created with 768 dimensions.")

# Verify
info = client.get_collection(collection_name)
print("Collection info:")
print(info)