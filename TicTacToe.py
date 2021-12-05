import random

def game_board(input_char, placement, previous_movement):
    top_left = 1
    top_mid = 2
    top_right = 3
    mid_left = 4
    mid_mid = 5
    mid_right = 6
    bot_left = 7
    bot_mid = 8
    bot_right = 9

    if top_left == placement:
        top_left = input_char
    if top_mid == placement:
        top_mid = input_char
    if top_right == placement:
        top_right = input_char
    if mid_left == placement:
        mid_left = input_char
    if mid_mid == placement:
        mid_mid = input_char
    if mid_right == placement:
        mid_right = input_char
    if bot_left == placement:
        bot_left = input_char
    if bot_mid == placement:
        bot_mid = input_char
    if bot_right == placement:
        bot_right = input_char

    if previous_movement[0][0] == 'x':
        top_left = 'x'
    if previous_movement[0][1] == 'x':
        top_mid = 'x'
    if previous_movement[0][2] == 'x':
        top_right = 'x'
    if previous_movement[1][0] == 'x':
        mid_left = 'x'
    if previous_movement[1][1] == 'x':
        mid_mid = 'x'
    if previous_movement[1][2] == 'x':
        mid_right = 'x'
    if previous_movement[2][0] == 'x':
        bot_left = 'x'
    if previous_movement[2][1] == 'x':
        bot_mid = 'x'
    if previous_movement[2][2] == 'x':
        bot_right = 'x'
    if previous_movement[0][0] == 'o':
        top_left = 'o'
    if previous_movement[0][1] == 'o':
        top_mid = 'o'
    if previous_movement[0][2] == 'o':
        top_right = 'o'
    if previous_movement[1][0] == 'o':
        mid_left = 'o'
    if previous_movement[1][1] == 'o':
        mid_mid = 'o'
    if previous_movement[1][2] == 'o':
        mid_right = 'o'
    if previous_movement[2][0] == 'o':
        bot_left = 'o'
    if previous_movement[2][1] == 'o':
        bot_mid = 'o'
    if previous_movement[2][2] == 'o':
        bot_right = 'o'
    
    print("        |       |          ")
    print("  ", top_left, "   |  ", top_mid, "  |   ", top_right, "    ")
    print("        |       |          ")
    print("---------------------------")
    print("        |       |          ")
    print("  ", mid_left, "   |  ", mid_mid, "  |   ", mid_right, "    ")
    print("        |       |          ")
    print("---------------------------")
    print("        |       |          ")
    print("  ", bot_left, "   |  ", bot_mid, "  |   ", bot_right, "    ")
    print("        |       |          ")
    print()

def generate_move(game_board, cpu_symbol):
    cpu_move = random.randint(0, 8)
    if game_board[cpu_move // 3][cpu_move % 3] == "":
        game_board[cpu_move // 3][cpu_move % 3] = cpu_symbol
    else:
        generate_move(game_board, cpu_symbol)
    return cpu_move
        
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

if __name__ == "__main__":
    #Create game board as 2D array filled with empty strings
    board_array = [["", "", "",],
                  ["", "", "",],
                  ["", "", ""]]
    
    game_board(1, 1, board_array)
    #Get player symbol ('x' or 'o') and set computer symbol to opposite
    player_symbol = input('Welcome, please choose your symbol for this game of TicTacToe (x or o)\n')
    if player_symbol == 'x':
        cpu_symbol = 'o'
    elif player_symbol == 'o':
        cpu_symbol = 'x'
    elif player_symbol != 'x' and player_symbol != 'o':
        #While loop until user enters valid symbol
        while player_symbol != 'x' and player_symbol != 'o':
            player_symbol = input('Please enter a valid symbol (x or o)\n')
            if player_symbol == 'x':
                cpu_symbol = 'o'
            elif player_symbol == 'o':
                cpu_symbol = 'x'
                
    #Get player move (1 - 9)
    player_move = 0
    while (player_move < 1) or (player_move > 9):
        try:
            player_move = int(input('Choose where you would like to make your first play (1-9).\n'))
            if 1 <= player_move <= 3:
                board_array[0][player_move - 1] = player_symbol
            elif 4 <= player_move <= 6:
                board_array[1][player_move - 4] = player_symbol
            elif 7 <= player_move <= 9:
                board_array[2][player_move - 7] = player_symbol
            else:
                print('Invalid position')
                continue
        except:
            print('Invalid position')
            continue
    #Get computer move
    game_board(cpu_symbol, (generate_move(board_array, cpu_symbol)) + 1, board_array)
    #Check board
    #If winner is detected, end game and display appropriate message
    #Else if the board is full and there is no winner, end game and display appropriate message
    #Else, continue the game
    while check_board_for_winner(board_array)[0] is not True:
        try:
            player_move = int(input('Choose your next move.\n'))
            if 1 <= player_move <= 3:
                if board_array[0][player_move - 1] == "":
                    board_array[0][player_move - 1] = player_symbol
                    if check_board_for_winner(board_array)[0] is True:
                        print('Congratulations, you win!')
                        break
                else:
                    print('That position is already taken.')
                    continue
            elif 4 <= player_move <= 6:
                if board_array[1][player_move - 4] == "":
                    board_array[1][player_move - 4] = player_symbol
                    if check_board_for_winner(board_array)[0] is True:
                        game_board(1, 1, board_array)
                        print('Congratulations, you win!')
                        break
                else:
                    print('That position is already taken.')
                    continue
            elif 7 <= player_move <= 9:
                if board_array[2][player_move - 7] == "":
                    board_array[2][player_move - 7] = player_symbol
                    if check_board_for_winner(board_array)[0] is True:
                        print('Congratulations, you win!')
                        break
                else:
                    print('That position is already taken.')
                    continue
            else:
                print('That is an invalid position.')
                continue
            game_board(cpu_symbol, (generate_move(board_array, cpu_symbol)) + 1, board_array)
        except:
            game_board(1, 1, board_array)
            print("It's a tie!")
            break

    if (check_board_for_winner(board_array)[0] is True) and (check_board_for_winner(board_array)[1] == cpu_symbol):
        print('Better luck next time!')
