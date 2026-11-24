class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lets_fly(obj):
    obj.fly()

bird = Bird()
airplane = Airplane()

lets_fly(bird)
lets_fly(airplane)