def turn():
    while True:
        column = int(input("where do you want to drop it? [1,2,3,4,5,6,7] "))
        while column not in [1,2,3,4,5,6,7]:
            column = int(input("invalid input. where do you want to drop it? [1,2,3,4,5,6,7] "))
        break
    return column

def check_win(board, row, col):
    # doesnt work right now
    max_rows = 6
    max_cols = 7
    connect = 0
    i = row
    win = False

    print(board[row][col])
    # check vertically
    while True:
        # check down
        while i in range(max_rows-1):
            if board[i][col] == board[i+1][col]:
                # print(board[i][col])
                # print(board[i+1][col])
                connect += 1
                i += 1 # go to next row down
            else:
                break
            if connect == 4:
                win = True
                break
        # check up
        while i in range(max_rows+1):
            if board[i][col] == board[i-1][col]:
                # print(board[i][col])
                # print(board[i-1][col])
                connect += 1
                i -= 1  # go to next row up
            else:
                break
            if connect == 4:
                win = True
                break
        break
    return win

def empty_board():
    board = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]

    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], '|', end="")
        print("\b ")
    return board

def play_game():
    rows = 6

    # display empty board
    board = empty_board()

    # start with player 1 by default
    player_turn = 1
        
    # tempory row indicator that gets reset per turn
    r = len(board)-1

    while True:

        # display whose turn it is
        if player_turn == 1:
            print ("player 1's turn:")
        elif player_turn == 2:
            print ("player 2's turn:")

        # ask the player which column they want to drop and return the input
        col = turn()
        col = col - 1 # because the range is from 0 to 6

        # check if the bottom-most row is 'empty' meaning it contains only a space
        # note: if there is a space in that row, record that row in 'r'
        # otherwise, decrement r to go to the above row
        while r >= 0:
            if board[r][col] == " ":
                break
            else:
                r -= 1

        # if it is player 1's turn, put X
        # if it is player 2's turn, put O
        if player_turn == 1:
            board[r][col] = "X"
        elif player_turn == 2:
            board[r][col] = "O"

        # prints out updated board
        for row in range(len(board)):
            for col in range(len(board[row])):
                print(board[row][col], '|', end="")
            print("\b ")

        # switch players
        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1

        # reset the row indicator
        r = len(board)-1


def main():

    play_game()

main()
