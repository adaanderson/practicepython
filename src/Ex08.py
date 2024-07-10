player1 = str()
player2 = str()
while player1 == player2:
    player1 = input ("Type in rock, paper or scissors: ")
    
    player2 = input ("Type in rock, paper or scissors: ")
    
    win1 = str("Player 1 wins!")
    win2 = str("Player 2 wins!")
    if player1 == "rock" and player2 == "paper":
        print(win2)
    elif player1 == "rock" and player2 == "scissors":
        print(win1)
    elif player1 == "paper" and player2 == "scissors":
        print(win2)
    elif player1 == "paper" and player2 == "rock":
        print(win1)
    elif player1 == "scissors" and player2 == "rock":
        print(win2)
    elif player1 == "scissors" and player2 == "paper":
        print(win1)
    elif player1 == player2:
        print("Tie, nobody wins. Play again.")
    

