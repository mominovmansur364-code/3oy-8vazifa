import csv

with open("8_vazifa/orders.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    eng_qimmat=next(data)
    jami=int(eng_qimmat['total_amount'])
    soni=1
    toshkent_jami=0
    toshkent_soni=0

    for i in data:
        jami+=int(i['total_amount'])
        soni+=1
        if i['city']=="Toshkent":
            toshkent_jami+=int(i["total_amount"])
            toshkent_soni+=1

        if int(i["total_amount"])>int(eng_qimmat["total_amount"]):
            eng_qimmat=i

ortacha=jami/soni

print(f"O'rtacha summa: {round(ortacha)}")
print(f"Toshkent buyurtmalar soni: {toshkent_soni}")
print(f"Toshkent buyurtmalar narxi: {toshkent_jami}")
print(f"Eng qimmat buyurtma qilgan mijoz ismi: {eng_qimmat['customer']} xarid summasi: {eng_qimmat['total_amount']}")
