import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, connections

# Check if a GPU is available and set PyTorch to use it
device = "cuda" if torch.cuda.is_available() else "cpu"

print(device)

# Initialize tokenizer and model for embeddings, and move the model to the selected device
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

# Connect to Milvus and define the collection schema with metadata fields
connections.connect("default", host='localhost', port='19530')

collection_name = "resumes"
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024),  # Adjusted dimension for BERT-Large
    FieldSchema(name="resumeid", dtype=DataType.INT64),
    FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=128),
    FieldSchema(name="resume_str", dtype=DataType.VARCHAR, max_length=49152)
]
schema = CollectionSchema(fields, description="Document Embeddings with Metadata using BERT")
collection = Collection(name=collection_name, schema=schema)

# Define batch size
batch_size = 100
count = 0

# Load and process data from CSV in batches
for batch_df in pd.read_csv('./resume/Resume/Resume.csv', chunksize=batch_size):
    print(count)
    count += 1
    
    # Combine title and content for embedding
    batch_df['text_for_embedding'] = batch_df['Resume_str']
    
    # Generate embeddings for each document in the batch
    batch_df['embeddings'] = batch_df['text_for_embedding'].apply(lambda x: get_embeddings([x])[0] if get_embeddings([x]) is not None else None).tolist()
    # batch_df['Value'] = batch_df['Value'].apply(lambda x: float(x.replace('$', '').replace(',', '')) if isinstance(x, str) else x)

    # Remove rows with None embeddings
    batch_df = batch_df[batch_df['embeddings'].notna()]
    
    # Extract entities for insertion
    entities = [
        batch_df['embeddings'].tolist(),
        batch_df['ID'].tolist(),
        batch_df['Category'].tolist(),
        batch_df['Resume_str'].tolist()
    ]
    
    # Insert data into Milvus
    insert_response = collection.insert(entities)

# Define index parameters for the "embedding" field
index_params = {
    "metric_type": "COSINE",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 100},
}

# Create the index
collection.create_index(field_name="embedding", index_params=index_params)
print("Index on the 'embedding' field has been created.")

print("Documents and embeddings with metadata have been successfully ingested into Milvus.")
