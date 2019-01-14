import board, Canvas, copy, globs, select, square
import sys, termios, tty, os, time, random
import pieces

def actions(dir):
    if (dir == "UP"):
        globs.current_piece.rotate()
        Canvas.draw_board()

    elif (dir == "DOWN"):
        if still_falling(globs.current_piece):
            globs.current_piece.move_down()
            Canvas.draw_board()

    elif (dir == "LEFT"):
        globs.current_piece.move_left()
        Canvas.draw_board()

    elif (dir == "RIGHT"):
        globs.current_piece.move_right()
        Canvas.draw_board()

def elapsed_time():
    return round(time.time() - globs.start_time, 1)

def get_dir():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = ""
    try:
        tty.setraw(sys.stdin.fileno())
        i, o, e = select.select( [sys.stdin], [], [], 0.05 )
        if (i):
            ch = sys.stdin.read(3).strip()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if ch == "qqq":
        exit()
    elif ch == "\x1b[A":
        return "UP"
    elif ch == "\x1b[B":
        return "DOWN"
    elif ch == "\x1b[C":
        return "RIGHT"
    elif ch == "\x1b[D":
        return "LEFT"

def still_falling(p):
    bs = bottom_sq(p)

    # if(p.collision()):
    #     input("COLLISION!")

    if bs.row >= board.HEIGHT - 1:
        return False

    if board.squares[bs.row + 1][bs.col].pieceStatus:
        return False
    else:
        return True

def bottom_sq(p):
    bs = p.squares[0][0]
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                bs = p.squares[i][j]
    return bs

def spawn_new():
    num = random.randint(0,2)
    if num == 0:
        globs.current_piece = pieces.T_piece()
    elif num == 1:
        globs.current_piece = pieces.L_piece()
    elif num == 2:
        globs.current_piece = pieces.J_piece()
    globs.current_piece.apply_to_squares(square.select, [])

    insert_piece(globs.current_piece)

def insert_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                new_row = p.squares[i][j].row
                new_col = p.squares[i][j].col
                board.squares[new_row][new_col] = copy.deepcopy(p.squares[i][j])
                # board.squares[new_row][new_col].selected = False

def reset_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                row = p.squares[i][j].row
                col = p.squares[i][j].col
                board.squares[row][col].pieceStatus = False
                board.squares[row][col].color = "none"
                board.squares[row][col].selected = False

def reset_board():
    for row in range(len(board.squares)):
        for col in range(len(board.squares[row])):
            board.squares[row][col].pieceStatus = False
            board.squares[row][col].color = "yellow"
