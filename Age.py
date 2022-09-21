import datetime

print("Welcome! This program computes the year you reach 100 when you input your current age!")
age = int(input("Current age:"))
date = datetime.date.today()

hundredyear = (100 - age) + date.year
print("You will reach one hundred on %d!" %hundredyear)

