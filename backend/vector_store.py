from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.client = chromadb.Client()
        self.collection = self.client.create_collection(
            "qa_agent_collection",
            metadata={"hnsw:space": "cosine"}
        )

    def embed(self, text):
        return self.model.encode(text).tolist()

    def add_documents(self, docs):
        ids = []
        texts = []
        metadatas = []

        for idx, doc in enumerate(docs):
            ids.append(str(idx))
            texts.append(doc["content"])
            metadatas.append({"source": doc["filename"]})

        embeddings = self.model.encode(texts).tolist()

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

    def query(self, query_text, k=5):
        query_emb = self.embed(query_text)
        return self.collection.query(
            query_embeddings=[query_emb],
            n_results=k
        )
