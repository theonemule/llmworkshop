# Objective: Demonstrate how LLMs can generate executable code from natural language prompting.

Note: If the queries don't work, try again or try tweaking your prompt. LLMs are not deterministic, so you may get different results even with the same prompt.

#
![Image](images/Slide24.JPG)
#
![Image](images/Slide25.JPG)

# The System Prompt

These exercises use a **system prompt** that instructs the LLM what to do. Your questions are passed in as the **user prompt**. The two are combined to create a prompt to generate the SQL.

System prompt:

```
"Generate just a SQL query from the following table called QuestionsAnswers with columns for a SQLLite database

ShowNumber,
AirDate,
Round -- Possible Values "Jeopardy!", "Double Jeopardy!", "Final Jeopardy!"
Category,
Value,
Question,
Answer

Return just the SQL. No Commentary! Include all the fields. Limit the results to 500
```


# **1. Create a simple filter.** 

**Prompt:** "Show all QuestionsAnswers  questions in the 'Science' category."


**Possible Output** (Executed Automatically):
   ```sql
   SELECT *
   FROM QuestionsAnswers 
   WHERE Category = 'Science';
   ```

# **2. Use natural language to create queries with multiple conditions.**

**Prompt:** "Find all questions from 'Double Jeopardy!' that have a value greater than $1000."

**Possible Output**
   ```sql
   SELECT *
   FROM QuestionsAnswers 
   WHERE Round = 'Double Jeopardy!' AND Value > 1000;
   ```

# **3. Use a natural language prompt to retrieve QuestionsAnswers  questions based on their air date.**

**Prompt:** "Show all questions from episodes that aired after January 1, 2010."

**Possible Output** (Executed Automatically):
   ```sql
   SELECT *
   FROM QuestionsAnswers 
   WHERE AirDate > '2020-01-01';
   ```

# **4. Use natural language to perform an aggregate query, such as counting questions or summarizing values.**

**Prompt:** "How many QuestionsAnswers  questions were asked in 'Final Jeopardy!'?"

**Possible Output** (Executed Automatically):
   ```sql
   SELECT COUNT(*) AS TotalQuestions
   FROM QuestionsAnswers 
   WHERE Round = 'Final Jeopardy!';
   ```

# **5. Retrieve questions based on a combination of conditions, such as date and round, using natural language prompts.**

**Prompt:** "Show all 'Jeopardy!' round questions from episodes aired in 2019."

**Possible Output** (Executed Automatically):
   ```sql
   SELECT *
   FROM QuestionsAnswers 
   WHERE Round = 'Jeopardy!' AND AirDate BETWEEN '2019-01-01' AND '2019-12-31';
   ```

# **6. Use natural language to group results by a specific field, like category, and perform an aggregate function.**

**Prompt:** "Group the number of questions by category in the 'Double Jeopardy!' round."

2. **Possible Output** (Executed Automatically):
   ```sql
   SELECT Category, COUNT(*) AS TotalQuestions
   FROM QuestionsAnswers 
   WHERE Round = 'Double Jeopardy!'
   GROUP BY Category;
   ```

# **7. Create a query that filters results based on multiple fields, such as value and category, using natural language.**

**Prompt** "Find all questions in the 'History' category with a value of $500 or less."

**Possible Output** (Executed Automatically):
   ```sql
   SELECT Question, Answer, Value, Category
   FROM QuestionsAnswers 
   WHERE Category = 'History' AND Value <= 500;
   ```
