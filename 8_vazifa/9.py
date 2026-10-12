import csv

with open("8_vazifa/expenses_homework.csv","r",encoding="UTF-8") as f,open(
    "8_vazifa/large_expenses.csv","w",newline="",encoding="UTF-8"
) as new_f:
    data=csv.DictReader(f)
    malumot=csv.writer(new_f)

    malumot.writerow(["category","amount"])

    for i in data:
        if int(i['amount'])>200:
            malumot.writerow([i['category'],i['amount']])
print("Muvaffaqiyatli!")