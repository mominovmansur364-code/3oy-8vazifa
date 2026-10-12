import csv

with open("8_vazifa/books.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    eng_qalin=next(data)
    jami=int(eng_qalin['pages'])
    count=1
    count2=0

    for i in data:
        count+=1
        jami+=int(i['pages'])

        if float(i['rating'])>=4.5:
            count2+=1
            print(f"{i['title']},{i['author']},{i['pages']},{i['rating']}")

        if int(i['pages'])>int(eng_qalin['pages']):
            eng_qalin=i
ortacha=jami/count
print(f"O'rtacha sahifalar soni: {ortacha}")
print(f"4.5 va undan yuqori bolgan kitoblar soni: {count2}")
print(f"Eng ko'p sahifali kitob nomi: {eng_qalin['title']} sahifalar soni: {eng_qalin['pages']}")