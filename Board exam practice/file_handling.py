import os

with open ("example.txt","w") as file:
    file.write("Hello vai k xa")

with open ("example.txt", "r") as file:
    data = file.read()
    print(data)

with open ("example.txt", "a") as file:
    file.write("\nHii")

with open ("example.txt", "r") as file:
    data = file.read()
    print( data)

os.remove("example.txt")