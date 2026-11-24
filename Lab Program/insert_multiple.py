import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)

cursor = db.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"

students = [
    ("Ram", 20),
    ("Sita", 21),
    ("Haji", 22)
]

cursor.executemany(sql, students)

db.commit()

print("Records inserted successfully!")

db.close()