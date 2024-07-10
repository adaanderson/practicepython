
def fib(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2: 
        return 2
    a = fib(n-1)
    b = fib(n-2)
    return a + b 

n = int(input("Enter the number of fibonnaci numbers you want generated: "))
x = list(range(0, n))
z = [fib(element) for element in x]
print(z)