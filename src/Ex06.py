string = input("Give me a string: ")

x = string[-1::-1]
if x == string:
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome...")
