import random
a = random.randint(1,9)
while True:
    print(a)
    user = input("Type in a number from 1 to 9: ")
    if user == "exit":
        break
    user = int(user)

    if user < a:
        print("You guessed too low.")
    elif user > a:
        print("You guessed too high.")
    
    elif user == a:
        print("You guessed correct! Game over.")
        break
