from flask import Flask, request, jsonify
from pymilvus import Collection, connections
from transformers import DistilBertTokenizer, DistilBertModel
import torch

# Connect to Milvus
connections.connect("default", host='localhost', port='19530')

# Specify the collection name and ensure it's loaded
collection_name = "document_embeddings_with_metadata"
collection = Collection(name=collection_name)
collection.load()

# Load the model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

def get_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def search(request):
    # Extract query from request
    data = request.json
    query_text = data.get('query')
    if not query_text:
        return jsonify({"error": "Please provide a 'query' field."}), 400
    
    # Generate query embedding
    query_embedding = get_embeddings([query_text])
    query_embeddings_list = query_embedding.tolist()
    
    # Search parameters
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    
    # Perform the search
    results = collection.search(
        data=query_embeddings_list,
        anns_field="embedding",
        param=search_params,
        limit=10,
        output_fields=["id", "embedding", "ShowNumber", "AirDate", "Round", "Category", "Value", "Question", "Answer"]
    )
    
    # Process and return search results
    search_results = []
    for hits in results:
        for hit in hits:
            search_results.append({
                "id": hit.id,
                "distance": hit.distance,
                "ShowNumber": hit.entity.get('ShowNumber'),
                "AirDate": hit.entity.get('title'),
                "Round": hit.entity.get('Round'),
                "Category": hit.entity.get('Category'),
                "Question": hit.entity.get('Question'),
                "Answer": hit.entity.get('Answer')
            })
    
    return jsonify(search_results)