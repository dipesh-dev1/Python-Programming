import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="school_db"
)

print("Connected successfully!")

db.close()