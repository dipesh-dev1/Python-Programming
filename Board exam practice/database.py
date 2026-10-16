import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER,
name TEXT,
age INTEGER)""" 
)

cur.execute("INSERT INTO students VALUES(1, 'Hari', 20)")
cur.execute("INSERT INTO students VALUES(2,'Ram',23)")
cur.execute("INSERT INTO students VALUES(3,'Sita',21)")

con.commit()

cur.execute("DELETE FROM students WHERE id =2")
con.commit()

cur.execute("SELECT * FROM students")
print("After delete:",cur.fetchall())

cur.execute("UPDATE students SET name='Rakesh' WHERE id = 1")
con.commit()

cur.execute("SELECT*FROM students")
print("After update :",cur.fetchall())

con.close()