import csv

with open("8_vazifa/employees.csv","r",encoding="UTF-8") as f,open(
    "8_vazifa/IT_bonuses.csv","w",newline="",encoding="UTF-8"
) as new_f:
    data=csv.DictReader(f)
    malumot=csv.writer(new_f)\

    malumot.writerow(['name','department','salary','bonus_salary'])

    for i in data:
        if i['department']=="IT":
            malumot.writerow([i['name'],i['department'],i['salary'],round(int(i['salary'])*1.1)])

print("Muvaffaqiyatli!")
