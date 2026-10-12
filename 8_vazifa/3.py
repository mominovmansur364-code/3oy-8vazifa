import csv

with open("8_vazifa/books_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    count=0
    for i in data:
        if int(i['year'])>2021:
            count+=1

print(f"2021 yildan keyin nashr etilgan kitoblar soni: {count} ta")