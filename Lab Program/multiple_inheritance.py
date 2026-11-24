class Father:
    def skills(self):
        print("Father: Cooking")

class Mother:
    def hobbies(self):
        print("Mother: Singing")

class Child(Father, Mother):
    pass

child = Child()

child.skills()
child.hobbies()