import board
import os
import platform

def draw_board():
    clear()
    out = ""
    for row in range(len(board.squares)):
        for col in range(len(board.squares[row])):
            out += str(board.squares[row][col])
        out += "\n"

    print(out, end = "")


def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("CLS")
    else:
        print("\033c")
