import board, os, platform, colors, utils, globs

def draw_board():
    clear()
    utils.generate_preview(globs.current_piece)

    out = h_buffer() + w_buffer()
    out += colors.BOX_TOP_LEFT
    for i in range(board.WIDTH * 2):
        out += colors.BOX_HORIZ
    out += colors.BOX_TOP_RIGHT + "\n" + w_buffer()
    for row in range(len(board.squares) - board.SPAWN):
        out += colors.BOX_VERT
        for col in range(len(board.squares[row + board.SPAWN])):
            out += str(board.squares[row + board.SPAWN][col])
        out += colors.BOX_VERT + "\n" + w_buffer()

    out += colors.BOX_BOTTOM_LEFT
    for i in range(board.WIDTH * 2):
        out += colors.BOX_HORIZ
    out += colors.BOX_BOTTOM_RIGHT + "\n"

    print(out, end = "")
    if not utils.met_preview(globs.current_piece):
        utils.reset_piece(globs.preview_pc)

def w_buffer():
    b = int(os.get_terminal_size().columns / 2) - board.WIDTH
    out = ""
    for i in range(b):
        out += " "
    return out

def h_buffer():
    b = int(os.get_terminal_size().lines / 2) - (int(board.HEIGHT / 2))
    out = ""
    for i in range(b):
        out += "\n"
    return out

def clear():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("CLS")
    else:
        print("\033c")
