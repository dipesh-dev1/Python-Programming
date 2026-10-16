from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

current_year = datetime.now().year
age = current_year - birth_year

print("Hello", name + "! You are approximately", age, "years old.")