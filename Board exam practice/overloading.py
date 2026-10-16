# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# a = Number(10)
# b = Number(20)

# print(a+b)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(self.x, self.y)

p1 = Point(2,3)
p2 = Point(4,5)

p3 = p1 + p2

p3.show()