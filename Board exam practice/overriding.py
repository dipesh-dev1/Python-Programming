class A():
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
c = B()
c.show()