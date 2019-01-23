from square import *
from pieces import *

HEIGHT = 20
SPAWN = 4
HEIGHT += SPAWN
WIDTH = 10
squares = []

def populate():
    global HEIGHT, WIDTH, squares
    squares = []
    for i in range(HEIGHT):
        squares.append([])

    # fill board with transparent squares
    for row in range(len(squares)):
        for col in range(WIDTH):
            squares[row].append(Square(False, "none", row, col))

    # set first SPAWN rows to spawn area
    for i in range(SPAWN):
        for j in range(WIDTH):
            squares[i][j].spawn = True

"""
apply_to_board: calls function() for
every square with a square in p on the
corresponding squares in board
"""
def apply_to_board(p, function, args=[]):
    global squares
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                function(args, squares[p.squares[i][j].row][p.squares[i][j].col])
