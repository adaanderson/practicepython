number = input("Give me a number: ")
print("Your number is: " + number)
number = int(number)
n = int((number / 2) + 1)
divisors = range(2, n)
for element in divisors:
    if number % element == 0:
        print(element)