#fix recursion
from random import randint

def get_player_moves(game_board):
    #get horizontal moves
    for i in range(3):
        if (game_board[i][0] == "X" and game_board[i][1] == "X") and game_board[i][2] == " ":
            return [i, 2]
        elif (game_board[i][1] == "X") and (game_board[i][2] == "X") and game_board[i][0] == " ":
            return [i, 0]
        elif (game_board[i][0] == "X" and game_board[i][2] == "X") and game_board[i][1] == " ":
            return [i, 1]
        #horizontal blocks
        elif (game_board[0][i] == "X") and (game_board[1][i] == "X") and game_board[2][i] == " ":
            return [2, i]
        elif (game_board[1][i] == "X") and (game_board[2][i] == "X") and game_board[0][i] == " ":
            return [0, i]
        elif (game_board[0][i] == "X") and (game_board[2][i] == "X") and game_board[1][i] == " ":
            return [1, i]
        #vertical blocks
    if (game_board[0][0] == "X") and (game_board[1][1] == "X") and game_board[2][2] == " ":
        return [2, 2]
    elif (game_board[2][2] == "X") and (game_board[1][1] == "X") and game_board[0][0] == " ":
        return [0, 0]
    elif (game_board[0][0] == "X") and (game_board[2][2] == "X") and game_board[1][1] == " ":
        return [1, 1]
    #diagonal blocks
    else:
        for i in range(3):
            for x in range(3):
                if game_board[i][x] == " ":
                    row, column = [i, x]
        return [row, column]
    #no forseeable moves
    
    return [row, column]

def make_move(game_board):
    row, column = get_player_moves(game_board)
    return [row, column]
