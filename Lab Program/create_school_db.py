import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")

cursor.execute("USE school_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
)
""")

# show all data
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)
    
print("Database and table created successfully.")

db.close()