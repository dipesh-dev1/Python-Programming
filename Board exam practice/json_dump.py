import json
student = {
    "name":"Dipesh",
    "age":20
}
with open("student.json","w") as file:
    json.dump(student, file)