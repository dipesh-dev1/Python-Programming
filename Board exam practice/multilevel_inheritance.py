class A():
    def show(self):
        print("Grandparent")

class B(A):
    pass

class C(A):
    pass

c = C()
c.show()