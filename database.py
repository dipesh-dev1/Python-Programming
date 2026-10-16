import sqlite3
# Connect to database
connection = sqlite3.connect("college.db")
# Create cursor
cursor = connection.cursor()
# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
# Insert data
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Sita", 19)
)
# Save changes
connection.commit()
# Retrieve data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Close connection
connection.close()
