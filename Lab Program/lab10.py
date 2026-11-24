# Public, Protected, and Private Members

class MyClass:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

obj = MyClass()

print(obj.public_var)
print(obj._protected_var)
print(obj._MyClass__private_var)