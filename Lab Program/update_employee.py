import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)

cursor = db.cursor()

# Update Jane Doe's city
sql = "UPDATE employees SET city = %s WHERE name = %s"
values = ("New York", "Jane Doe")

cursor.execute(sql, values)
db.commit()

# Show only updated employee
cursor.execute("SELECT * FROM employees WHERE name = 'Jane Doe'")

for row in cursor.fetchall():
    print(row)

db.close()