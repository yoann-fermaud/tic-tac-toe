import random


def ia(board, sign):
    while True:
        x = random.randrange(1, 10)
        x -= 1
        if 0 <= x < 9:
            if x in board:
                continue
            board.append(x)
            board[x] = sign
            return board
