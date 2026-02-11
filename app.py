
from fastapi import FastAPI
from refund_graph import build_refund_graph

app = FastAPI(title="Refund Request AI Agent")

refund_graph = build_refund_graph()

@app.post("/refund")
def process_refund(request: dict):
    state = {
        "user_input": request["user_input"],
        "embedding_model": request["embedding_model"],
        "index": request["index"],
        "policies": request["policies"]
    }

    result = refund_graph.invoke(state)

    return {
        "decision": result["decision"],
        "response": result["response"],
        "policy_used": result["policies_matched"] # Changed from result.get("policy") or result.get("policies_matched")
    }
