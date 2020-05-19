board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

game_in_progress = True


def print_board(board):
    print("-------------")
    for x in board:
        print("| " + x[0] + " | " + x[1] + " | " + x[2] + " |")
        print("-------------")


def set_position(board, item, x, y):
    if((board[x][y] == 'X') | (board[x][y] == 'O')):
        return False

    board[x][y] = item
    return True


def input_turn(chart):
    temp = -1

    while not(1 <= temp <= 9):
        temp = input("Choose a position from 1-9: ")
        temp = int(temp)

    print(temp)

    result = False

    if (temp == 1):
        result = set_position(board, chart, 0, 0)
    elif (temp == 2):
        result = set_position(board, chart, 0, 1)
    elif (temp == 3):
        result = set_position(board, chart, 0, 2)
    elif (temp == 4):
        result = set_position(board, chart, 1, 0)
    elif (temp == 5):
        result = set_position(board, chart, 1, 1)
    elif (temp == 6):
        result = set_position(board, chart, 1, 2)
    elif (temp == 7):
        result = set_position(board, chart, 2, 0)
    elif (temp == 8):
        result = set_position(board, chart, 2, 1)
    elif (temp == 9):
        result = set_position(board, chart, 2, 2)

    if(result == False):
        print("Invalid move, field already taken")
        input_turn(chart)

    return temp


def game_loop():
    print_board(board)

    while(game_in_progress):
        print("Player1 [X] on the turn")
        input_turn('X')
        print_board(board)
        print("Player2 [O] on the turn")
        input_turn('O')
        print_board(board)
    

print('Hello in tic-tac-toe\n')


game_loop()
# game_loop()


