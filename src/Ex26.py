#p = player, 1 or 2
#b = board
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
    if is_winner(b, 1):
        return '1'
    elif is_winner(b, 2):
        return '2'
    else:
        return '0'
    
board0 = [[2, 2, 0],
          [2, 1, 0],
          [2, 1, 1]]

board1 = [[1, 2, 0],
	      [2, 1, 0],
	      [2, 1, 2]]

board2 = [[0, 1, 0],
	      [2, 1, 0],
	      [2, 1, 1]]

print(board0)
print("Winner is " + any_winner(board0))
print(board1)
print("Winner is " + any_winner(board1))
print(board2)
print("Winner is " + any_winner(board2))
