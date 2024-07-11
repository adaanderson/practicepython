a = [1, 3, 5, 30, 42, 43, 500]
def main():
    user = int(input("Give me a number: "))
    if user in a:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()