import random

def generate_move(game_board, cpu_symbol):
    cpu_move = randint(0, 8)
    if game_board[cpu_move // 3][cpu_move % 3] == "":
        game_board[cpu_move // 3][cpu_move % 3] = cpu_symbol
    else:
        generate_move(game_board, cpu_symbol)

def check_board_for_winner(game_board):
    #Returns True if a winner is detected, and the symbol of the winner
    if game_board[1][1] != "":
        if game_board[0][0] == game_board[1][1] == game_board[2][2]: return True, game_board[0][0]
        if game_board[0][2] == game_board[1][1] == game_board[2][0]: return True, game_board[0][0]

    for i in range(0, 3):
        if (game_board[i][0] != "") and (game_board[i][0] == game_board[i][1] == game_board[i][2]): return True, game_board[i][0]
       
    for j in range(0, 3):
        if (game_board[0][j] != "") and (game_board[0][j] == game_board[1][j] == game_board[2][j]): return True, game_board[0][j]

    #Returns False if a winner is not detected, and the symbol in spot (0, 0) of the board as a placeholder
    return False, game_board[0][0]

if __name__ == "main":
    #Create game board as 2D array filled with empty strings
    #Get player symbol ('x' or 'o') and set computer symbol to opposite
    #Get player move (1 - 9)
    #Get computer move
    #Check board
    #If winner is detected, end game and display appropriate message
    #Else if the board is full and there is no winner, end game and display appropriate message
    #Else, continue the game
