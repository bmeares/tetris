import board, Canvas, copy, globs, select, square
import sys, termios, tty, os, time, random
import pieces

def actions(dir):
    collided = globs.current_piece.collision()

    if (dir == "UP"):
        if not collided:
            temp_rotated_p = copy.deepcopy(globs.current_piece)
            temp_rotated_p.rotate()
            t_thru_r_wall = right_sq(temp_rotated_p).col >= board.WIDTH
            t_thru_l_wall = left_sq(temp_rotated_p).col < 0

            # if temp piece doesn't clip through walls
            if (not t_thru_l_wall) and (not t_thru_r_wall):
                reset_piece(globs.current_piece)
                globs.current_piece.rotate()
                insert_piece(globs.current_piece)
                Canvas.draw_board()

    elif (dir == "DOWN"):
        if not collided:
            globs.current_piece.move_down()
            insert_piece(globs.current_piece)
            Canvas.draw_board()

    elif (dir == "LEFT"):
        if not globs.current_piece.l_collision():
            globs.current_piece.move_left()
            insert_piece(globs.current_piece)
            Canvas.draw_board()

    elif (dir == "RIGHT"):
        if not globs.current_piece.r_collision():
            globs.current_piece.move_right()
            insert_piece(globs.current_piece)
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
        # TODO uncomment this
        # Canvas.clear()
        exit()
    elif ch == "\x1b[A":
        return "UP"
    elif ch == "\x1b[B":
        return "DOWN"
    elif ch == "\x1b[C":
        return "RIGHT"
    elif ch == "\x1b[D":
        return "LEFT"

def bottom_sq(p):
    bs = p.squares[0][0]
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                bs = p.squares[i][j]
    return bs

def top_sq(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                return p.squares[i][j]

def left_sq(p):
    least_col = board.WIDTH
    for list in p.squares:
        for s in list:
            if s.col < least_col and s.selected and s.pieceStatus:
                least_col = s.col
                l_sq = s
    return l_sq

def right_sq(p):
    most_col = -1
    for list in p.squares:
        for s in list:
            if s.col > most_col and s.selected and s.pieceStatus:
                most_col = s.col
                m_sq = s
    return m_sq


def spawn_new():
    num = random.randint(0,6)
    if num == 0:
        globs.current_piece = pieces.T_piece()
    elif num == 1:
        globs.current_piece = pieces.L_piece()
    elif num == 2:
        globs.current_piece = pieces.J_piece()
    elif num == 3:
        globs.current_piece = pieces.O_piece()
    elif num == 4:
        globs.current_piece = pieces.S_piece()
    elif num == 5:
        globs.current_piece = pieces.Z_piece()
    elif num == 6:
        globs.current_piece = pieces.I_piece()

    globs.current_piece.apply_to_squares(square.select, [])

    insert_piece(globs.current_piece)

def insert_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus and p.squares[i][j].selected:
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
                board.squares[row][col].selected = False

def de_select_piece(p):
    board.apply_to_board(p, square.de_select, [])

def reset_board():
    for row in range(len(board.squares)):
        for col in range(len(board.squares[row])):
            board.squares[row][col].pieceStatus = False
            board.squares[row][col].color = "yellow"
