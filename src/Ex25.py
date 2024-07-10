counter = 0
high = 100
low = 0
pool = high - low
guess = int(pool/2 + low)
print("I guess " + str(guess))
guesses = 1
while True:
    user = input("Enter h if your number is higher than the guess, l if it's lower than the guess, and c if the guess is correct: ")
    if user == "h":
       low = guess
       pool = high - low
       guess = int(low + (pool/2)) 
       print("I guess " + str(guess))
       guesses += 1 
    elif user == "l":
        high = guess
        pool = high - low
        guess = int(low + (pool/2))
        print("I guess " + str(guess))
        guesses += 1
    elif user == "c":
        print("It took " + str(guesses) + " guesses to guess your number.")
        break
    else:
        print("That was not h, l, or c. Try again.")

