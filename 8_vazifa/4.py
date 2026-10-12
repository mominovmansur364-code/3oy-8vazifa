import csv
umumiy=0
with open("8_vazifa/products_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    for i in data:
        jami=int(i['price'])*int(i['quantity'])
        print(f"{i['name']} ni jami narxi: {jami}")
        umumiy+=jami

print(f"Umumiy summa: {umumiy}")