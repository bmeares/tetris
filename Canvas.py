import board
import os
import platform

def draw_board():
    clear()
    out = "\n" + buffer()
    for row in range(len(board.squares) - board.SPAWN):
        for col in range(len(board.squares[row + board.SPAWN])):
            out += str(board.squares[row + board.SPAWN][col])
        out += "\n" + buffer()

    print(out, end = "")


def buffer():
    b = int(os.get_terminal_size().columns / 2) - board.WIDTH
    out = ""
    for i in range(b):
        out += " "
    return out

def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("CLS")
    else:
        print("\033c")
