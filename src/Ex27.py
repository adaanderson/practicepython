
def game_format(start_game):
        for row in start_game:
            print(row)

start_game = [['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0']]

game_format(start_game)

while True:
    player1 = input("Player 1: Enter your move in the format (row,col): ")
    player2 = input("Player 2: Enter your move in the format (row,col): ")

    list1 = player1.split(',')
    list2 = player2.split(',')
    first = list(map(int, list1))
    second = list(map(int, list2))
    
    start_game[first[0]][first[1]] = 'X'   
    start_game[second[0]][second[1]] = 'O'   
    def game_format(start_game):
        for row in start_game:
            print(row)
    game_format(start_game)    
      
   
    