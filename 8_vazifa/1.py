import csv

with open("8_vazifa/employees_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    for xodim in data:
        print(f"{xodim['name']},{xodim['department']}")
