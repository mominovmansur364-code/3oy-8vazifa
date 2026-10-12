import csv

with open("8_vazifa/students.csv","r",encoding="UTF-8") as f,open(
    "8_vazifa/scholarship_students.csv","w",newline="",encoding="UTF-8"
) as new_f:
    data=csv.DictReader(f)
    malumot=csv.writer(new_f)

    malumot.writerow(['name','faculty','gpa','status'])

    for i in data:
        if i['faculty'] == "Informatika" and i['status'] == "Aktiv" and float(i['gpa']) >= 4.2:
            malumot.writerow([i['name'],i['faculty'],i["gpa"],i['status']])

print("Muvaffaqiyatli!")