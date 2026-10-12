import csv
name=input("Ism: ").capitalize()
age=input("Yoshi: ")
score=int(input("Bali: ")
)
if score<0 or score>100:
    print("Bunday ball mavjud emas!")
    
elif score>=70:
    with open("8_vazifa/new_students_homewrork.csv","a",encoding="UTF-8") as f:
        data=csv.writer(f)
        data.writerow([name,age,score])
        print("Muvaffaqiyatli qo'shildi")

else:
    print("Xatolik! Faylga qoshilmadi")


    
    