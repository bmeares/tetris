import board, Canvas, copy, globs, square, random, time
# import sys, termios, tty, os, time, random
import pieces, colors

def remove_sq(sq):
    row = sq.row
    col = sq.col
    top_sq = copy.deepcopy(board.squares[row - 1][col])
    # if top_sq.pieceStatus:
    #     top_sq.clear = True
    board.squares[row][col] = top_sq
    board.squares[row][col].row += 1
    # board.squares[top_sq.row][top_sq.col].pieceStatus = False


def check_loss():
    for i in range(board.SPAWN):
        for j in range(board.WIDTH):
            if board.squares[i][j].pieceStatus and not board.squares[i][j].selected:
                return True
    return False


def clear_board():

    def clear_line(row):
        for i in range(board.WIDTH):
            remove_sq(board.squares[row][i])

    rows_cleared = 0
    for row in board.squares:
        ps_count = 0
        for s in row:
            if s.pieceStatus:
                ps_count += 1
        if ps_count == board.WIDTH:
            # print("ABOUT TO CLEAR!")
            # input()
            r = s.row
            rows_cleared += 1
            while r > 0:
                clear_line(r)
                # print("cleared line " + str(r))
                # input()
                r -= 1
            # Canvas.draw_board()
    award_points(rows_cleared)
    globs.lines_cleared += rows_cleared

def award_points(n):
    if n == 0:
        return
    #  else:
        #  print("n is : " + str(n))
        #  input()
    if n == 1:
        globs.score += 40
    elif n == 2:
        globs.score += 100
    elif n == 3:
        globs.score += 300
    elif n == 4:
        globs.score += 1200


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

def drop_to_bottom(p):
    globs.distance_dropped = 0
    while not p.collision():
        p.move_down()
        globs.distance_dropped += 1
        #  print("distance_dropped is now " + str(globs.distance_dropped))

    return p
    # insert_piece(p)
    # globs.dropped = True

def check_level():
    # increase level when surpassed level * LINES_PER_LEVEL
    if globs.lines_cleared >= globs.current_level * globs.LINES_PER_LEVEL:
        globs.current_level += 1

def spawn_new():
    globs.dropped = False
    num = random.randint(0,6)
    new_pc = None
    if num == 0:
        new_pc = pieces.T_piece()
    elif num == 1:
        new_pc = pieces.L_piece()
    elif num == 2:
        new_pc = pieces.J_piece()
    elif num == 3:
        new_pc = pieces.O_piece()
    elif num == 4:
        new_pc = pieces.S_piece()
    elif num == 5:
        new_pc = pieces.Z_piece()
    else:
        new_pc = pieces.I_piece()

    new_pc.apply_to_squares(square.select, [])
    globs.current_piece = new_pc

    insert_piece(globs.current_piece)

def insert_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus and p.squares[i][j].selected:
                # only if the square is visible on the board
                if p.squares[i][j].row >= 0 and p.squares[i][j].col >= 0 and p.squares[i][j].col < board.WIDTH:
                    new_row = p.squares[i][j].row
                    new_col = p.squares[i][j].col
                    board.squares[new_row][new_col] = copy.deepcopy(p.squares[i][j])

def reset_piece(p):
    for i in range(len(p.squares)):
        for j in range(len(p.squares[i])):
            if p.squares[i][j].pieceStatus:
                row = p.squares[i][j].row
                col = p.squares[i][j].col
                board.squares[row][col] = square.boardSquare(row, col)
                # board.squares[row][col].pieceStatus = False
                # board.squares[row][col].color = "none"
                # board.squares[row][col].selected = False

def de_select_piece(p):
    board.apply_to_board(p, square.de_select, [])

def reset_board():
    for row in range(len(board.squares)):
        for col in range(len(board.squares[row])):
            board.squares[row][col].pieceStatus = False
            board.squares[row][col].color = "yellow"

def elapsed_time():
    return round(time.time() - globs.start_time, 1)

def met_preview(p):
    return top_sq(globs.preview_pc).row == top_sq(p).row

def generate_preview(p):
    globs.preview_pc = copy.deepcopy(p)
    globs.preview_pc.apply_to_squares(square.prev, [])
    globs.preview_pc.preview = True
    globs.preview_pc = drop_to_bottom(globs.preview_pc)
    if met_preview(p):
        return
    insert_piece(globs.preview_pc)
