import pandas as pd
from transformers import DistilBertTokenizer, DistilBertModel
import torch
from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, connections

# Check if GPU is available and select the device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Initialize tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
# Load the model to the specified device
model = DistilBertModel.from_pretrained('distilbert-base-uncased').to(device)

def get_embeddings(texts):
    try:
        # Encode the inputs using the tokenizer
        inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}  # Move input tensors to the device
        with torch.no_grad():
            outputs = model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).cpu().numpy()  # Move output tensors back to CPU for numpy conversion
    except Exception as e:
        print("Error occurred while generating embeddings:", e)
        return None

# Connect to Milvus and define the collection schema with metadata fields
connections.connect("default", host='localhost', port='19530')

collection_name = "document_embeddings_with_metadata"
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
    FieldSchema(name="ShowNumber", dtype=DataType.INT64),
    FieldSchema(name="AirDate", dtype=DataType.VARCHAR, max_length=64),
    FieldSchema(name="Round", dtype=DataType.VARCHAR, max_length=64),
    FieldSchema(name="Category", dtype=DataType.VARCHAR, max_length=256),
    FieldSchema(name="Value", dtype=DataType.FLOAT),
    FieldSchema(name="Question", dtype=DataType.VARCHAR, max_length=1024),
    FieldSchema(name="Answer", dtype=DataType.VARCHAR, max_length=1024),
]
schema = CollectionSchema(fields, description="Document Embeddings with Metadata")
collection = Collection(name=collection_name, schema=schema)

# Define batch size and start processing
batch_size = 100
count = 0

# Load and process data from CSV in batches
for batch_df in pd.read_csv('JEOPARDY.csv', chunksize=batch_size):
    print(count)
    count += 1
    
    # Combine relevant fields for embedding
    batch_df['text_for_embedding'] = batch_df['Category'] + " " + batch_df['Question'] + " " + batch_df['Answer']

    # Generate embeddings for each document in the batch
    batch_df['embeddings'] = batch_df['text_for_embedding'].apply(lambda x: get_embeddings([x])[0] if get_embeddings([x]) is not None else None).tolist()
    batch_df['Value'] = batch_df['Value'].apply(lambda x: float(x.replace('$', '').replace(',', '')) if isinstance(x, str) else x)

    # Filter out rows without embeddings
    batch_df = batch_df[batch_df['embeddings'].notna()]
    
    # Prepare data for insertion into Milvus
    entities = [
        batch_df['embeddings'].tolist(),
        batch_df['ShowNumber'].tolist(),
        batch_df['AirDate'].tolist(),
        batch_df['Round'].tolist(),
        batch_df['Category'].tolist(),
        batch_df['Value'].tolist(),
        batch_df['Question'].tolist(),
        batch_df['Answer'].tolist(),
    ]
    
    # Insert data into Milvus
    insert_response = collection.insert(entities)

# Define index parameters for the "embedding" field
index_params = {
    "metric_type": "L2",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 100},
}

# Create the index
collection.create_index(field_name="embedding", index_params=index_params)
print("Index on the 'embedding' field has been created.")

print("Documents and embeddings with metadata have been successfully ingested into Milvus.")