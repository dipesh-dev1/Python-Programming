
import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cur = con.cursor()

# Create database
cur.execute("CREATE DATABASE IF NOT EXISTS CollegeDB")
cur.execute("USE CollegeDB")

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Student (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Marks FLOAT
)
""")

print("Database and table created successfully!")

# CRUD Menu
while True:

    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Insert Student")
    print("2. Display All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # INSERT
    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        sql = "INSERT INTO Student VALUES (%s, %s, %s)"
        val = (roll, name, marks)

        cur.execute(sql, val)
        con.commit()

        print("Student inserted successfully!")

    # DISPLAY
    elif choice == 2:
        cur.execute("SELECT * FROM Student")

        records = cur.fetchall()

        print("\nRollNo\tName\tMarks")

        for row in records:
            print(row[0], "\t", row[1], "\t", row[2])

    # UPDATE
    elif choice == 3:
        roll = int(input("Enter Roll Number: "))
        marks = float(input("Enter new Marks: "))

        sql = "UPDATE Student SET Marks=%s WHERE RollNo=%s"
        val = (marks, roll)

        cur.execute(sql, val)
        con.commit()

        if cur.rowcount > 0:
            print("Student marks updated successfully!")
        else:
            print("Student not found!")

    # DELETE
    elif choice == 4:
        roll = int(input("Enter Roll Number: "))

        sql = "DELETE FROM Student WHERE RollNo=%s"
        val = (roll,)

        cur.execute(sql, val)
        con.commit()

        if cur.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # EXIT
    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")

# Close connection
cur.close()
con.close()
