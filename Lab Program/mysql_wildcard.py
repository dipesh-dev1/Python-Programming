import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM students WHERE name LIKE 'J%'")

for row in cursor.fetchall():
    print(row)

db.close()