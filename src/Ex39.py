import datetime

name = input("Give me your name: ")
print("Your name is " + name)
now = datetime.datetime.now()
age = input("Give me your age: ")
age = int(age)
years = str((99 - age) + now.year)

print(name + " will be 100 when the year is " + years)