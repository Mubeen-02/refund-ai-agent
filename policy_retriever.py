
def retrieve_policy(query, embedding_model, index, policies, top_k=3):
    query_embedding = embedding_model.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, top_k)
    return [policies[i] for i in indices[0]]
