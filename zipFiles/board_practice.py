def space_check(board,position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def disply_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
test_board = ['#','X','O','X','O','X','O','X',' ','']
disply_board(test_board)

# 🚨 Don't change the code below 👇
import random
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? :")

column = int(position[0])
row = int(position[1])

map[r-1][c-1] = "x"
print(f"{row1}\n{row2}\n{row3}")