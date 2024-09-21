from flask import Flask, request, jsonify, send_from_directory, abort
from pymilvus import Collection, connections
from transformers import BertTokenizer, BertModel
import torch
import os


# Check if a GPU is available and set PyTorch to use it
device = "cuda" if torch.cuda.is_available() else "cpu"

# Connect to Milvus
connections.connect("default", host='localhost', port='19530')

# Specify the collection name and ensure it's loaded
collection_name = "resumes"
collection = Collection(name=collection_name)
collection.load()

# Load the model
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
model = BertModel.from_pretrained('bert-large-uncased').to(device)

def get_embeddings(texts):
    try:
        inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
        with torch.no_grad():
            outputs = model(**inputs)
        # Move output tensors back to CPU for compatibility with other operations that expect NumPy arrays
        return outputs.last_hidden_state.mean(dim=1).cpu().numpy()
    except Exception as e:
        print("Error occurred while generating embeddings:", e)
        return None
        
def answer_question(question, resume, client, deployment_name):
    # Tokenize the text to get an accurate token count
   
    completion = client.chat.completions.create(
        model=deployment_name,  # e.g. gpt-35-instant
        messages=[
            {
                "role": "system",
                "content": "You are a search assistant. The user will submit just one resume per request. Use that one resume to answer this question: " + question,
            },
            {
                "role": "user",
                "content": resume,
            },
        ],
    )
    
    answer = completion.choices[0].message.content
    
    print(answer)

                       
    return answer




def ragsearch(request, client, deployment_name):
    # Extract query from request
    data = request.json
    query_text = data.get('query')
    if not query_text:
        return jsonify({"error": "Please provide a 'query' field."}), 400
        
    # context = get_context(query_text, client, deployment_name)

    # Generate query embedding
    query_embedding = get_embeddings([query_text])
    query_embeddings_list = query_embedding.tolist()
    
    # Search parameters
    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
   
    # Perform the search
    results = collection.search(
        data=query_embeddings_list,
        anns_field="embedding",
        param=search_params,
        limit=5,
        output_fields=["id", "embedding", "resumeid", "category", "resume_str"]
    )
    
    search_results = []
    for hits in results:
        for hit in hits:
            

            answer = answer_question(query_text, hit.entity.get('resume_str'), client, deployment_name)
    
    
            search_results.append({
                "distance": hit.distance,
                "id": hit.entity.get('resumeid'),
                "category": hit.entity.get('category'),
                "answer": answer
            })    
    
    return jsonify(search_results)
    
def getresume(request):
    # Extracting 'id' and 'category' from the query string
    category = request.args.get('category')
    resume_id = request.args.get('id')

    if not category or not resume_id:
        return abort(400, description="Missing 'id' or 'category' in query string")

    # Define the directory where files are stored
    directory = os.path.join('./data/docs', category)
    
    print(directory)
    
    # Filename for the PDF
    filename = f"{resume_id}.pdf"

    # Check if the file exists
    if not os.path.exists(os.path.join(directory, filename)):
        return abort(404, description="File not found")

    # Sending the file from the directory
    return send_from_directory(directory, filename)