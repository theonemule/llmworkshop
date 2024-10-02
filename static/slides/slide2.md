Objective: The lab that explores different kinds of prompting while summarizing a Wikipedia article.

# **1. Choose a Wikipedia Article**

1. Select any Wikipedia article (e.g., “Machine Learning”).
2. Copy the the URL and paste it into the box for the URL

# **2. Few-Shot Learning Pattern**

Provide examples before the task to show the model how to summarize.

- **Prompt**: 
  - "Here’s how to summarize an article:  
    Example 1: [Summary of Article 1]  
    Example 2: [Summary of Article 2]"

Change the number of examples to see how it affects the model’s output.


# **3. Chain of Thought Pattern**

Encourage the model to break down its reasoning step-by-step before giving the final answer.

- **Prompt**: "First, identify the key topics in the article. Then, list the main points. Finally, summarize the article.  


Observe how the intermediate steps improve or affect the final summary.

# **4. Persona Pattern**

Instruct the model to act as a specific persona or take on a certain role when summarizing.

- **Prompt**:
  - "You are a history professor. Summarize the following article for your students.  

  - "You are a technical expert. Summarize the following article for a general audience."

Compare how different personas affect the tone, style, and depth of the summary.


# **5. Template Pattern**

Use a predefined template or format to structure the response.

- **Prompt**:
  - "Summarize the article in three sentences:  
    - The main topic is…  
    - The most important detail is…  
    - In conclusion…  

See how the template enforces structure in the summaries.

# **6. Safety and Guardrails Pattern**

Provide instructions to avoid certain types of responses or content.

**Prompt**: "Summarize the article without including any opinions, speculation, or offensive content."

Note how the model remains neutral and avoids potentially problematic content.

# **7. Controlled Text Generation Pattern**

Guide the model to produce text within specific constraints, such as word limits.

**Prompt**: "Summarize this article in exactly 50 words:  
  
**Variation**: "Summarize in a maximum of two sentences."

Observe how constraints like length influence the precision and conciseness of the summary.