import csv

with open("8_vazifa/cities_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    for i in data:
        if int(i['population'])>=500000:
            print(f"{i['city']}")