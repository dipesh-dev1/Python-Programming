import csv

with open ("doc.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Dipesh", 20])

with open ("doc.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)