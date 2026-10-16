class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Enter your age:"))
    if age<0:
        raise NegativeAgeError ("Age can't be negative")

except NegativeAgeError as e:
    print(e)

except ValueError:
    print("Please enter a valid number")

else:
    print("Age :", age)

finally:
    print("Program finished")