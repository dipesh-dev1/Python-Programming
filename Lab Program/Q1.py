
# Student Marks Management Program

names = []
marks = []

n = int(input("Enter number of students: "))

# Accept student names and marks
for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

# Calculate average
average = sum(marks) / n

print("\n----- Student Result -----")

# Display Pass or Fail
for i in range(n):
    if marks[i] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(names[i], ":", marks[i], "-", result)

# Display highest and lowest marks
print("\nAverage Marks:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
