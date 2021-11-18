import random

def generate_move(game_board, cpu_symbol):
    cpu_move = randint(0, 8)
    if game_board[cpu_move // 3][cpu_move % 3] == "":
        game_board[cpu_move // 3][cpu_move % 3] = cpu_symbol
    else:
        generate_move(game_board, cpu_symbol)

def check_board(game_board):
    if game_board[0][0] == game_board[1][1] == game_board[2][2]: return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0]: return True

    for i in range(len(game_board)):
        if game_board[i][0] == game_board[i][1] == game_board[i][2]: return True
       
    for j in range(len(game_board(i))):
        if game_board[0][j] == game_board[1][j] == game_board[2][j]: return True

    return False

if __name__ == "main":
    #Create game board as 2D array filled with empty strings
    #Get player symbol ('x' or 'o') and set computer symbol to opposite
    #Get player move (1 - 9)
    #Get computer move
    #Check board
    #If winner is detected, end game and display message
    #Else, continue the game
