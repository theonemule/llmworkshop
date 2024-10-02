import pandas as pd
import sqlite3

# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file_path = 'JEOPARDY.csv'
# Replace 'your_database.db' with the desired SQLite database name
sqlite_db_path = 'JEOPARDY.db'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Connect to the SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(sqlite_db_path)

# Replace 'your_table_name' with the desired table name
table_name = 'QuestionsAnswers'

# Convert the DataFrame to SQL (this will create the table if it doesn't exist)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

print(f"Data from {csv_file_path} has been successfully imported into {sqlite_db_path} in the table {table_name}.")
