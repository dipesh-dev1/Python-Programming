import json

student = [
    {"id":1,"name":"Hari","age":23},
    {"id":2,"name":"Shyam","age":22}
]

with open("students.json","w") as f:
    json.dump(student,f)

with open("students.json", "r") as f:
    data = json.load(f)
    for student in data:
        print(student)