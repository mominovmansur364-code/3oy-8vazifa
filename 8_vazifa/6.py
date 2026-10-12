import csv

with open("8_vazifa/inventory_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    eng_kam_mahsulot=next(data)

    for i in data:
        if int(i['stock'])<int(eng_kam_mahsulot['stock']):
            eng_kam_mahsulot=i

    print(f"Eng kam maxsulot nomi: {eng_kam_mahsulot['item']} uning soni: {eng_kam_mahsulot['stock']}")