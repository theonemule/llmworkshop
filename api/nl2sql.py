from flask import Flask, request, jsonify, send_from_directory
import whisper
from io import BytesIO
import os
import openai
import sqlite3
from werkzeug.local import Local

sqlite_db_path = 'data/JEOPARDY.db'

#db_connection = sqlite3.connect(sqlite_db_path)
#db_cursor = db_connection.cursor()

def init_db():
    if not hasattr(local_storage, 'db_connection') or local_storage.db_connection is None:
        local_storage.db_connection = sqlite3.connect(sqlite_db_path)
        local_storage.db_cursor = local_storage.db_connection.cursor()

local_storage = Local()
local_storage.db_connection = None
local_storage.db_cursor = None

def askquestion(request, client, deployment_name):

    # Get the question from the request
    question = request.json.get('question')        
        
    print(question)
    
    completion = client.chat.completions.create(
        model=deployment_name,  # e.g. gpt-35-instant
        messages=[
            {"role": "system", "content": """Generate just a SQL query from the following table called QuestionsAnswers with columns for a SQLLite database

ShowNumber,
AirDate,
Round -- Possible Values "Jeopardy!", "Double Jeopardy!", "Final Jeopardy!"
Category,
Value,
Question,
Answer

Return just the SQL. No Commentary! Include all the fields. Limit the results to 500
"""},
            {"role": "user", "content": question}
        ]
    )
    

    
    init_db()


    sql_query = completion.choices[0].message.content

    print(sql_query)

    #db_cursor.execute(sql_query)
    #results = db_cursor.fetchall()
    
    local_storage.db_cursor.execute(sql_query)
    results = local_storage.db_cursor.fetchall()    
    

    # Format and return the results as JSON
    result_data = []
    
    
#    for row in results:
#        result_data.append({
#            'ShowNumber': row[0],
#            'AirDate': row[1],
#            'Round': row[2],
#            'Category': row[3],
#            'Value': row[4],
#            'Question': row[5],
#            'Answer': row[6]
#        })

    # Get column names from cursor description
    column_names = [desc[0] for desc in local_storage.db_cursor.description]

    # Format and return the results as JSON
    result_data = []
    
    for row in results:
        row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
        result_data.append(row_dict)
        
   return jsonify({'sqlQuery': sql_query, 'columns': column_names, 'results': result_data})
    
 


    
