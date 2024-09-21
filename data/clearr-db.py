from pymilvus import Collection, utility, connections

# Step 1: Connect to the Milvus server
# Replace 'default' with your connection name if different.
# Adjust the host and port accordingly if your Milvus instance is not running with the default settings.

name = "resumes1"

connections.connect("default", host='localhost', port='19530')

utility.drop_collection(name)

connections.disconnect("default")

print(name + " has been deleted.")