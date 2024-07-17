
dimension = int(input("Enter the width/height of the game board: "))

def columns(dimension):
    bar = "|   "
    dash = " ---"
    for numbers in range (0, dimension):
        print (dimension*dash + "\n" + (dimension + 1)*bar)
    print(dimension*dash)

columns(dimension)