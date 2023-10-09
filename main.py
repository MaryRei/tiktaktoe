

from checkwin import *
from opponent import *

def winner(winner):
    print_board(game_board)
    print(f"Game over! {winner} wins!")
    
turns = 0

game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

print("Welcome to tik-tak-toe! input the coordinates of the square you would like to claim")



while turns < 6:
    turns += 1    
    print_board(game_board)    
    print(f"Turn: {turns}")
    print()
    
    x, y = turn(game_board)
    
    game_board[x][y] = "X"
    
  
    if check_win(game_board, x, y):
        winner("Player")
        break
    opponent_row, opponent_column = make_move(game_board)
    game_board[opponent_row][opponent_column] = "O"
    
    
    if check_win(game_board, opponent_row, opponent_column):
        winner("Computer")        
        break 
        
    print()