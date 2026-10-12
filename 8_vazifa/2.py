import csv

with open("8_vazifa/students_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    for i in data:
        if int(i['score'])>=85:
            print(f"{i['name']},{i['score']}")