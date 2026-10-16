import csv

with open("students.csv","w" ,newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","name","age"])
    w.writerow([1,"Ram",20])
    w.writerow([2,"Haari",23])
    w.writerow([3,"Shyam",24])
    w.writerow([4,"Sita",21])
    w.writerow([5,"Sima",19])

with open ("students.csv","r") as f:
    r = csv.reader(f)
    for row in r:
        print(row)