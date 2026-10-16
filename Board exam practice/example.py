# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     result = a/b
#     print("result:",result)

# except ZeroDivisionError:
#     print("Can't divide by zero")

# def add(*args):
#     total = 0

#     for n in args:
#         total +=n

#     return total

# print(add(10,20,30))

# def student(**kwargs):
#     print(kwargs)

# student(name="Dipesh", age=20)

# import json

# data = {"name":"Dipesh", "age":20, "roll": 16}

# with open ("hello.json", "w") as file:
#     json.dump(data, file)

# print("Data saved")


# import json

# data = {"name":"Dipesh", "age":20}

# result = json.dumps(data)

# print(result)


# with open ("hii.txt", "r") as file:
#     for line in file:
#      print(line , end="")

# class Bank():
#     def __init__(self):
#         self.__balance = 1000

#     def show_balance(self):
#         print(self.__balance)

# b = Bank()
# b.show_balance()

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# num = int(input("Enter num:"))
# print(fact(num))

# class Student():
#     def __init__(self):
#         self.name = "Ram"
#         self._roll = 17
#         self.__age = 29

# s = Student()
# print(s.name)
# print(s._roll)
# print(s._Student__age)


# import sqlite3

# con = sqlite3.connect("college.db")
# cur = con.cursor()

# cur.execute(""" CREATE TABLE IF NOT EXISTS students(
# id INTEGER,
# name TEXT,
# age INTEGER)"""
#             )
# id = int(input("Enter id:"))
# name = input("Enter name:")
# age = int(input("Enter age:"))

# cur.execute("INSERT INTO students VALUES(?,?,?)",(id,name,age))
# con.commit()

# cur.execute("SELECT * FROM students")
# print(cur.fetchall())
# con.close()

# cube = lambda x:x**3
# print(cube(3))

# class A:
#     def show(self):
#         print("Parent")
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# d = D()
# d.show()

class Student:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)
s=Student("Ram")