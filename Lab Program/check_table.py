import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES LIKE 'students'")

if cursor.fetchone():
    print("students table exists.")
else:
    print("students table does not exist.")

db.close()