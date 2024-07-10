import random

def main():
    numbers = [chr(e) for e in range (ord('0'), ord('9') + 1)]
    generate = random.sample(numbers, k=4)
    
    guesses = 0
    while True:
        user = list(input("Enter a 4-digit number: "))
        guesses += 1
        bulls = 0
        cows = 0
        for index in range(0, len(user)):
            if generate[index] == user[index]:
                cows += 1
            elif user[index] in generate:
                bulls += 1
        if cows == 4:
            print("You won in " + str(guesses) + " guesses!")
            break
         
        print(str(bulls) + " bull(s) and " + str(cows) + " cow(s)")

if __name__=="__main__":
    main()