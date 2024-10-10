# These lab exercises use prompt patterns for searching and analyzing obfuscated resumes in a vector database (Milvus) with a RAG app. Each exercise will first involve searching the resumes, followed by analyzing the matched results.

#
![Image](images/Slide33.JPG)
#
![Image](images/Slide34.JPG)
#
![Image](images/Slide35.JPG)

# # About the RAG underpinnings.

The example here uses BERT as an embedding model, but uses GPT 3.5 to analyze the results according to what you instruct the model to do.

GPT 3.5 uses the follwing system prompt:

```
You are a search assistant. The user will submit just one resume per request. Use that one resume to answer this question: [Your Analysis Prompt Here]
```

# **1. Perform a simple search using zero-shot prompting to find resumes with specific skills.**

 **Search Prompt**:  
"Find resumes of candidates with experience in management and Python."

 **Analysis Prompt**:  
"Analyze each resume for years of experience in management and provide a summary of relevant projects."

# **2. Break down the thought process to search for specific expertise (Chain of Thought Pattern).**

 **Search Prompt**:  
"First, find resumes with C# Experience with management skills."

 **Analysis Prompt**:  
"For the resume found, summarize the managment skills, and 2. provide a detailed breakdown of the candidate's development experience."

# **3. Use a persona-based search to find resumes that fit a specific role (Persona Pattern).**

 **Search Prompt**:  
"Find candidates who can lead a software engineering team and has experience in .NET and Javascript."

 **Analysis Prompt**:  
"You are a hiring manager. Analyze the resume for leadership experience and assess project management skills based on the candidate's previous roles."


# **4. Search resumes that follow a specific template for qualifications (Template Pattern).**

 **Search Prompt**:  
"Find candidates who can lead a software engineering team and has experience in .NET and Javascript."

 **Analysis Prompt**:  
"Summarize the resume of in the following format:  
- Skills:  
- Experience:  
- Education:  
- Certifications:"

# **5. Ensure the search follows safety and guardrails, avoiding specific content (Safety and Guardrails Pattern).**

 **Search Prompt**:  
"Find candidates who can lead a software engineering team and has experience in .NET and Javascript."

 **Analysis Prompt**:  
"Summarize the resume of for skills and experience, but avoid using bulleted lists of skills."