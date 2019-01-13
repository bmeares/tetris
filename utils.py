import board, Canvas, copy
from pieces import *

def move_down(p):
    reset_piece(p)
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            p.squares[i][j].row += 1

    insert_piece(p)

def insert_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                new_row = p.squares[i][j].row
                new_col = p.squares[i][j].col
                board.squares[new_row][new_col] = copy.deepcopy(p.squares[i][j])

def reset_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                row = p.squares[i][j].row
                col = p.squares[i][j].col
                board.squares[row][col].pieceStatus = False
                board.squares[row][col].color = "none"
