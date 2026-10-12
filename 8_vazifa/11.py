import csv

with open("8_vazifa/products.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    eng_qimmat=next(data)
    jami=int(eng_qimmat['price'])*int(eng_qimmat['stock'])

    for i in data:
        jami+=int(i['price'])*int(i['stock'])
        
        if int(i['stock'])>100:
            print(f"{i['product_name']},{i['price']}")

        if int(i['price'])>int(eng_qimmat['price']):
            eng_qimmat=i

print(f"Jami summa: {jami}")
print(f"Eng qimmat maxsulot: {eng_qimmat['product_name']}")