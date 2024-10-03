# Objective: Demonstrate how LLMs can generate executable code from natural language prompting

# ![Image](slides/Slide24.JPG)
# ![Image](slides/Slide25.JPG)

# **1. Create a simple filter.** 

**Prompt:** "Show all trivia questions in the 'Science' category."**

**Possible Output** (Executed Automatically):
   ```sql
   SELECT *
   FROM trivia
   WHERE Category = 'Science';
   ```

# **2. Use natural language to create queries with multiple conditions.**

**Prompt:** "Find all questions from 'Double Jeopardy!' that have a value greater than $1000."

**Possible Output**
   ```sql
   SELECT *
   FROM trivia
   WHERE Round = 'Double Jeopardy!' AND Value > 1000;
   ```

# **3. Use a natural language prompt to retrieve trivia questions based on their air date.**

**Prompt:** "Show all questions from episodes that aired after January 1, 2010."

**Possible Output**
   ```sql
   SELECT *
   FROM trivia
   WHERE AirDate > '2020-01-01';
   ```

# **4. Use natural language to perform an aggregate query, such as counting questions or summarizing values.**

**Prompt:** "How many trivia questions were asked in 'Final Jeopardy!'?"

**Possible Output**
   ```sql
   SELECT COUNT(*) AS TotalQuestions
   FROM trivia
   WHERE Round = 'Final Jeopardy!';
   ```

# **5. Retrieve questions based on a combination of conditions, such as date and round, using natural language prompts.**

**Prompt:** "Show all 'Jeopardy!' round questions from episodes aired in 2019."

**Possible Output**
   ```sql
   SELECT *
   FROM trivia
   WHERE Round = 'Jeopardy!' AND AirDate BETWEEN '2019-01-01' AND '2019-12-31';
   ```

# **6. Use natural language to group results by a specific field, like category, and perform an aggregate function.**

**Prompt:** "Group the number of questions by category in the 'Double Jeopardy!' round."

2. **Possible Output**
   ```sql
   SELECT Category, COUNT(*) AS TotalQuestions
   FROM trivia
   WHERE Round = 'Double Jeopardy!'
   GROUP BY Category;
   ```

# **7. Create a query that filters results based on multiple fields, such as value and category, using natural language.**

**Prompt** "Find all questions in the 'History' category with a value of $500 or less."

**Possible Output**
   ```sql
   SELECT Question, Answer, Value, Category
   FROM trivia
   WHERE Category = 'History' AND Value <= 500;
   ```
