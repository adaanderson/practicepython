NoOne = 'no one'

# who won
def is_winner(b, p):
    for row in b:
        if [p, p, p] == row:
            return True
    for c in range(0, 3):
        if b[0][c] == p and b[1][c] == p and b[2][c] == p:
            return True
    diag = (p == b[0][0] and p == b[1][1] and p == b[2][2] or
            p == b[0][2] and p == b[1][1] and p == b[2][0])
    return diag

# return who won, player 1 or 2 (or 0 if nobody).
def any_winner(b):
    if is_winner(b, 'X'):
        return 'X'
    elif is_winner(b, 'O'):
        return 'O'
    else:
        return NoOne

# player move
def is_any_move(game_board):
    return any(' ' in sub for sub in game_board)

def output(game_board):
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            print(game_board[row_index][column_index], end='')
            if (column_index < 2):
                print("|", end='')
        print()
        if (row_index < 2):   
            print("-+-+-")   

def move(game_board, player):
    coords_str = input(f"Player {player}: Enter your move in the format (row,col): ")
    
    list = coords_str.split(',')
    coords = list(map(int, list))
    
    game_board[coords[0]][coords[1]] = player

    if is_any_move(game_board) == False or any_winner(game_board) != NoOne:
        print("The winner is " + any_winner(game_board) + '.')
        return False
    return True

def play(game_board):
    output(game_board)
    while any_winner(game_board) == NoOne and move(game_board, 'X') and move(game_board, 'O'):
        pass

start_game = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

play(start_game)