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
    board[x][y] = item

# todo 
def input_turn(chart):
    temp = -1
    while (temp > 1 & temp < 9):
        temp = input("Choose a position from 1-9: ")
        temp = int(temp) - 1

    print(temp)
    # if(temp == 1):
        


def game_loop():
    while(game_in_progress):
        print("Player1 [x] on the turn")
        
        print_board(board)

    

print('Hello in tic-tac-toe\n')
input_turn("X")
# game_loop()


