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
        print('\x1b[6;30;42m' +
              'Invalid move, field already taken' + '\x1b[0m')
        input_turn(chart)

    return temp


def game_loop():
    print_board(board)
    turns = 0

    while(True):
        # Player 1 on the turn
        print("Player1 [X] on the turn")
        input_turn('X')
        print_board(board)
        turns += 1
        if(check_game_over(board)):
            break

        # board is full
        if(turns == 9):
            break
            
        #  Player 2 on the turn
        print("Player2 [O] on the turn")
        input_turn('O')
        print_board(board)
        turns += 1

        if(check_game_over(board)):
            break
    

def check_game_over(board):
    if(check_game_over_horizontal(board) | check_game_over_vertical(board)):
        print('\x1b[7;32;40m' + 'Game over'  + '\x1b[0m')
        return True

def check_game_over_horizontal(board):
    for x in board:
        if(x[0] == x[1] == x[2]):
            return True

    return False

def check_game_over_vertical(board):
    for i in range(0, 3):
        if(board[0][i] == board[1][i] == board[2][i]):
            return True
    
    return False

print('\x1b[2;30;44m' + 'Hello in tic-tac-toe'  + '\x1b[0m')
game_loop()
# game_loop()


