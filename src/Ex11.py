user = int(input("Give me a number: "))

x = int((user/2) + 1)

divisors = list(range(2, x))

c = [element for element in divisors if user % element == 0]
if len(c) == 0:
    print("Your number is a prime number.")
else:
    print("Your number is not a prime number.")
