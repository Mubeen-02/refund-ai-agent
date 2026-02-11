
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from refund_graph import build_refund_graph

app = FastAPI(title="Refund AI Agent")

#  Load model once at startup
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

#  Load policies file
with open("refund_policies.txt") as f:
    policies = [line.strip() for line in f]

#  Create FAISS index
embeddings = embedding_model.encode(policies).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Build graph
refund_graph = build_refund_graph()

@app.post("/refund")
def process_refund(request: dict):

    state = {
        "user_input": request["user_input"],
        "embedding_model": embedding_model,
        "index": index,
        "policies": policies
    }

    result = refund_graph.invoke(state)

    return {
        "decision": result["decision"],
        "response": result["response"]
    }
