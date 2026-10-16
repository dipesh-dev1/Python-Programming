# class Student:
#     def __init__(self):
#         print("Object created")

#     def __del__(self):
#         print("Object being Destroyed")

# s = Student()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

s = Student("Ram", 20)
s.show()