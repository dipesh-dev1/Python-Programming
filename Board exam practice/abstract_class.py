# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sound()

from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print(4*4)

class  Circle(Shape):
    def area(self):
        print(3.14*2*2)

s = Square()
c = Circle()

s.area()
c.area()