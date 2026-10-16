import sys
name = sys.argv[1]
print("Hello", name)  # It prints name

a = int(sys.argv[2])
b = int(sys.argv[3])
print("sum =", a+b)  # It prints sum because int defined

a = sys.argv[2]
b = sys.argv[3]
print("sum =", a+b) # It prints the given number same it is because no defined datatype