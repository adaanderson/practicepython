height = int(input("Enter the height of the game board: "))
width = int(input("Enter the width of the game board: "))

def columns(height, width):
    bar = "|   "
    dash = " ---"
    for numbers in range (0, height):
        print (width*dash + "\n" + (width + 1)*bar)
    print(width*dash)

columns(height, width)

