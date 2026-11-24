import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)

cursor = db.cursor()

sql = "SELECT * FROM employees WHERE address LIKE %s"
value = ("%Main%",)

cursor.execute(sql, value)

for row in cursor.fetchall():
    print(row)

db.close()