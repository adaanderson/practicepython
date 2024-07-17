import json

#birthday_dictionary = {
#    "Ada Lovelace" : "12/10/1815"
#}

#with open("birthdays.json", "w") as f:
#    json.dump(birthday_dictionary, f)


with open("birthdays.json", "r") as f:
    birthdays = json.load(f)
user = input("Enter the person whose birthday you want to know: ")
print(birthdays[user])
#print(birthdays)