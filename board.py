from square import *
from pieces import *

HEIGHT = 20
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

"""
apply_to_board: calls function() for
every square with a block in p on the
corresponding squares in board
"""
def apply_to_board(p, function):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                function(p.squares[i][j])

# def
