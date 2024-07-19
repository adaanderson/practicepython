import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        
        if guess < 1 or guess > 9:
            print("Guess again. Your number was not between 1 and 9.")
        else:
            number_of_guesses += 1
            if guess < number:
                print("You guessed too low.")
            elif guess > number:
                print("You guessed too high.")
            elif guess == number:
                break                
    except ValueError:
        print("ValueError is thrown")

print(f"You needed {number_of_guesses} guesses to guess the number {number}")