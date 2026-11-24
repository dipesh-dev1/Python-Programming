# Explicit Typecasting
string = "10" 
number = 9
string_number = int(string) # error occurs if the string is not valid integer
sum = number + string_number
print("sum is : ", sum)

# Implicit Typecasting
# Python Automatically converts
a = 7
print(type(a))

b = 3.8
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))