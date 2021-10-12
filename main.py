def board_moves(moves):
    if moves == 1:
        return 0, 0
    if moves == 2:
        return 0, 1
    if moves == 3:
        return 0, 2
    if moves == 4:
        return 1, 0
    if moves == 5:
        return 1, 1
    if moves == 6:
        return 1, 2
    if moves == 7:
        return 2, 0
    if moves == 8:
        return 2, 1
    if moves == 9:
        return 2, 2


def real_board(board):
    for el in board:
        print(el)


def moves_to_make(board, play1, play2):
    turn_counter = 1
    while True:
        choice = (int(input(f'{play1[0]} choose a free position [1-9]: ')))
        print()
        if turn_counter == 10:
            print('Draw')
            exit()
        # is choice valid
        if is_choice_valid(choice):
            row, col = board_moves(choice)
            if board[row][col] == ' ':
                board[row][col] = play1[1]
                real_board(board)
            else:
                print('Already taken. Choose another field.')
            if turn_counter >= 5:
                if win_conditions(board, play1[1]):
                    print(f'{play1[0]} has won!')
                    exit()

            play1, play2 = play2, play1
        turn_counter += 1


def win_conditions(board, sign):
    # horizontal
    for row in board:
        if all([el == sign for el in row]):
            return True
    # vertical
    size_of_board = len(board)
    for col in range(size_of_board):
        counter = 0
        for row in range(size_of_board):
            if board[row][col] == sign:
                counter += 1
        if counter == 3:
            return True

    # diagonal1
    diagonal1_counter = 0
    for row in range(size_of_board):
        if board[row][row] == sign:
            diagonal1_counter += 1
    if diagonal1_counter == 3:
        return True

    # diagonal2
    diagonal2_counter = 0
    if board[2][0] == sign:
        diagonal2_counter += 1
    if board[1][1] == sign:
        diagonal2_counter += 1
    if board[0][2] == sign:
        diagonal2_counter += 1

    if diagonal2_counter == 3:
        return True


def is_choice_valid(num):
    if 1 <= num <= 9:
        return num
    return print(f'{num} not in range')


def printing_matrix():
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')


def players():
    player_1 = input(f'Player one name: ')
    player_2 = input(f'Player two name: ')
    while True:
        allowed_signs = ('X', 'O')
        print(f'{player_1} pick your sign: X or O')
        player_1_sign = input().upper()
        if player_1_sign in allowed_signs:
            break
    player_2_sign = ('X' if player_1_sign == 'O' else '0')
    return [player_1, player_1_sign], [player_2, player_2_sign]


player_1, player_2 = players()
printing_matrix()
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
moves_to_make(board, player_1, player_2)
board_moves(board)
