import random


def game_board(input_char, placement, previous_movement):
    spaces = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    for i in range(0, 3):
        for x in range(0, 3):
            if spaces[x][i] == placement:
                spaces[x][i] = input_char

    for i in range(0, 3):
        for x in range(0, 3):
            if previous_movement[x][i] == 'x':
                spaces[x][i] = 'X'
            if previous_movement[x][i] == 'o':
                spaces[x][i] = 'O'

    print("        |       |          ")
    print("  ", spaces[0][0], "   |  ", spaces[0][1], "  |   ", spaces[0][2], "    ")
    print("        |       |          ")
    print("---------------------------")
    print("        |       |          ")
    print("  ", spaces[1][0], "   |  ", spaces[1][1], "  |   ", spaces[1][2], "    ")
    print("        |       |          ")
    print("---------------------------")
    print("        |       |          ")
    print("  ", spaces[2][0], "   |  ", spaces[2][1], "  |   ", spaces[2][2], "    ")
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
    # Returns True if a winner is detected, and the symbol of the winner
    if game_board[1][1] != "":
        if game_board[0][0] == game_board[1][1] == game_board[2][2]:
            return True, game_board[0][0]
        if game_board[0][2] == game_board[1][1] == game_board[2][0]:
            return True, game_board[0][0]

    for i in range(0, 3):
        if (game_board[i][0] != "") and (game_board[i][0] == game_board[i][1] == game_board[i][2]):
            return True, game_board[i][0]

    for j in range(0, 3):
        if (game_board[0][j] != "") and (game_board[0][j] == game_board[1][j] == game_board[2][j]):
            return True, game_board[0][j]

    # Returns False if a winner is not detected, and the symbol in spot (0, 0) of the board as a placeholder
    return False, game_board[0][0]


if __name__ == "__main__":
    # Create game board as 2D array filled with empty strings
    board_array = [["", "", "", ],
                   ["", "", "", ],
                   ["", "", ""]]

    game_board(1, 1, board_array)
    # Get player symbol ('x' or 'o') and set computer symbol to opposite
    player_symbol = input('Welcome, please choose your symbol for this game of TicTacToe (x or o)\n')
    cpu_symbol = ""
    if player_symbol == 'x':
        cpu_symbol = 'o'
    elif player_symbol == 'o':
        cpu_symbol = 'x'
    elif player_symbol != 'x' and player_symbol != 'o':
        # While loop until user enters valid symbol
        while player_symbol != 'x' and player_symbol != 'o':
            player_symbol = input('Please enter a valid symbol (x or o)\n')
            if player_symbol == 'x':
                cpu_symbol = 'o'
            elif player_symbol == 'o':
                cpu_symbol = 'x'

    # Get player move (1 - 9)
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
    # Get computer move
    game_board(cpu_symbol, (generate_move(board_array, cpu_symbol)) + 1, board_array)
    # Check board
    # If winner is detected, end game and display appropriate message
    # Else if the board is full and there is no winner, end game and display appropriate message
    # Else, continue the game
    while check_board_for_winner(board_array)[0] is not True:
        try:
            player_move = int(input('Choose your next move.\n'))
            if 1 <= player_move <= 3:
                if board_array[0][player_move - 1] == "":
                    board_array[0][player_move - 1] = player_symbol
                    if check_board_for_winner(board_array)[0] is True:
                        game_board(1, 1, board_array)
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
                        game_board(1, 1, board_array)
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
