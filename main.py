board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def print_board(board):
    print("-------------")
    for x in board:
        print("| " + x[0] + " | " + x[1] + " | " + x[2] + " |")
        print("-------------")


def next_turn(board, item, x, y):
    board[x][y] = item


print('Hello in tic-tac-toe')
board[0][0] = "X"
print_board(board)
