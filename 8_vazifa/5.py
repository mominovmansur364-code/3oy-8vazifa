import csv

jami=0
soni=0

with open("8_vazifa/orders_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    for i in data:
        soni+=1
        jami+=int(i['amount'])

ortacha=jami/soni

print(f"Buyurtmalar summasi: {jami}")
print(f"O'rtacha buyurtma summasi: {ortacha}")