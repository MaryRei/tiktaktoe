def validity(number):
    return number >= 0 and number <= 3

def check_win(game_board, x, y):
    if ((game_board[x][y] == game_board[x][y-1] == game_board[x][y-2])  # check for horizontal win
    or (game_board[x][y] == game_board[x-1][y] == game_board[x-2][y])  # check for vertical win
    or (game_board[x][y] == game_board[x-1][y-1] == game_board[x-2][y-2])  # check for diagonal winS
    or (game_board[x][y] == game_board[x-1][y-2] == game_board[x-2][y-1])):            
        return True
    else:
        return False    
    
def print_board(game_board):
    for i in range(3):
        print(f"| {game_board[i][0]} | | {game_board[i][1]} | | {game_board[i][2]} |\n")    
    
def turn(game_board):
    while True:
        try:
            x = int(input("Please input the row number you would like to select: "))
            y = int(input("Please input the column number you would like to select: "))
        except ValueError:
            print("Not an integer, try again. ")
            continue
        if (validity(x) and validity(y)) and game_board[x][y] == " ":
            return [x, y]
        else:
            print("Spot is already taken or invalid input")
            continue