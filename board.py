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
            squares[row].append(Square(True, "yellow", row, col))
