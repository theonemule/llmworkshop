# This set of lab exercises uses natural language to search a vector database (Milvus) containing concatenated embeddings of trivia data, utilizing different prompting patterns.

#
![Image](images/Slide29.JPG)
#
![Image](images/Slide30.JPG)
#
![Image](images/Slide31.JPG)
#
![Image](images/Slide32.JPG)

# **1. Perform a simple search using zero-shot prompting to find trivia questions related to a specific topic.**

Prompt: "Find trivia questions about World War II."

# **2. Use a few examples to guide the search for similar trivia questions (Few-Shot Learning Pattern).**

Prompt:  
"Here are two examples of questions:  
Example 1: 'Who was the president of the United States during World War II?'  
Example 2: 'What year did World War II end?'  
Now, find more trivia questions about wars."

# **3. Use a persona-based prompt to influence the search results (Persona Pattern).**

Prompt:  
"You are a history professor. Find trivia questions related to major historical events from the 20th century."

# **4. Ensure the prompt follows certain guardrails by avoiding specific content (Safety and Guardrails Pattern).**

Prompt:  
"Find trivia questions related to science, but avoid any questions related to biology."


