#Job 4.2
def board_cr(n):
    board = [['O' for _ in range(n)] for _ in range(n)]

    for line in range(n):
        for column in range(n):
            if (line + column) % 2 == 1:
                board[line][column] = 'X'

    return board

def display_board(board):
    for row in board:
        print(' '.join(row))

def main():
    n = int(input("Enter the size of the board: "))
    checkers_board = board_cr(n)
    display_board(checkers_board)

    
main()
