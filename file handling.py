#write operation
file = open("dipesh.txt", "w")
file.write("Hello, This is my first file")
file.write("This is the another content.\n")

#append operation
file = open("dipesh.txt", "a")
file.write("This line is added at the end.\n")

#read operation
file = open("detail.csv", "r")
content = file.read()
print(content)
file.close()
