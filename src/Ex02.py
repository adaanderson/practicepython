number = input("Give me a random number: ")
print("Your number is: " + number)
number = int(number)
divide = str(number % 2)
number1 = str(number)
if divide == 0:
    print("The number " + number1 + " is even!")
else:
    print("The number " + number1 + " is odd!") 

