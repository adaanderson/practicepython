
def maxus(a, b, c):
    if a > b:
        winner1 = a
    else:
        winner1 = b
    if winner1 > c:
        return winner1
    else:
        return c
    
a = input("Enter the first thing: ")
b = input("Enter the second thing: ")
c = input("Enter the third thing: ")
print(maxus(a, b, c))