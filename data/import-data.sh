#!/bin/bash
# Start milvus-server in the background
milvus-server &

sleep 30

# Execute the Python scripts
python3 import-milvus.py
python3 import-sqlite.py
python3 import-resumes-bert.py

