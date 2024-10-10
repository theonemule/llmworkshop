# This set of lab exercises uses natural language to search a vector database (Milvus) containing concatenated embeddings of trivia data, utilizing different prompting patterns.

#
![Image](images/Slide29.JPG)
#
![Image](images/Slide30.JPG)
#
![Image](images/Slide31.JPG)
#
![Image](images/Slide32.JPG)
#
![Image](images/Slide38.JPG)
#
![Image](images/Slide39.JPG)
#
![Image](images/Slide40.JPG)
#
![Image](images/Slide41.JPG)
#
![Image](images/Slide42.JPG)

# About the BERT Model:

BERT (Bidirectional Encoder Representations from Transformers) is a pre-trained deep learning model that excels at understanding the context and relationships between words in a sentence by considering both the left and right context simultaneously. While it's an older model, it's still widely used for natural language processing tasks like question answering, semantic search, and text classification becuase it its relatively compact size and speed. However, when it comes to **negative prompting** where the goal is to exclude certain information or focus on results that lack specific features—it isn't inherently well-equipped for handling these scenarios in a straightforward manner.

# **1. Perform a simple search to find trivia questions related to a specific topic.**

Note: These exercises simply return results without actually analyzing the results. You'll see analysis when dealing with RAG apps.

Example Prompt: "Find trivia questions about World War II."

# **2. Perform a search to find trivia questions that contain similar words or phrases.**

Example Prompt: "Find trivia questions with similar words to 'election' and 'government.'"

# **3. Search for trivia questions that are contextually similar to a specific question.**

Example Prompt: "Find trivia questions similar to 'Who was the first president of the United States?'"

# **4. Find trivia questions based on a broad category and compare semantic similarity.**

Example Prompt: "Show trivia questions related to the category 'Science,' and more specifically space exploration."

# **5. Perform a search for trivia questions by combining multiple related topics.**

Example Prompt: "Find trivia questions about both ancient civilizations and famous wars."

# **6. Search for trivia questions that mention historical figures but not by name.**

Example Prompt: "Find trivia questions about a famous U.S. president who helped abolish slavery."

