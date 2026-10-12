import csv

with open("8_vazifa/exam_results_homework.csv","r",encoding="UTF-8") as f:
    data=csv.DictReader(f)

    eng_baland=next(data)
    eng_past=eng_baland
    jami=int(eng_baland['score'])
    soni=1

    for i in data:
        soni+=1
        jami+=int(i['score'])
        if int(i['score'])>=70:
            print(f"{i['name']} {i['score']}")


        if int(i['score'])>int(eng_baland['score']):
            eng_baland=i


        if int(i['score'])<int(eng_past['score']):
            eng_past=i

ortacha=jami/soni

print(f"Eng baland ball olgan student: {eng_baland['name']} bali: {eng_baland['score']}")
print(f"Eng past ball olgan student: {eng_past['name']} bali: {eng_past['score']}")
print(f"O'rtacha ball: {ortacha}")
      