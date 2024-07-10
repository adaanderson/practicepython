birthday_dictionary = {"Ada Anderson": "7/9/2011", "Benjamin Franklin": "1/17/1706"}
print("We know the birthdays of Ada Anderson and Benjamin Franklin.")
user = input("Whose birthday do you want to look up? ")
if user == "Ada Anderson":
    print(birthday_dictionary["Ada Anderson"])
elif user == "Benjamin Franklin":
    print(birthday_dictionary["Benjamin Franklin"])