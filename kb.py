import sys, termios, tty, os, time, random, select, utils, copy
import Canvas, globs, board

def actions(dir):
    collided = globs.current_piece.collision()

    if (dir == "UP"):
        if not collided:
            temp_rotated_p = copy.deepcopy(globs.current_piece)
            temp_rotated_p.rotate()
            t_thru_r_wall = utils.right_sq(temp_rotated_p).col >= board.WIDTH
            t_thru_l_wall = utils.left_sq(temp_rotated_p).col < 0

            # if temp piece doesn't clip through walls
            if (not t_thru_l_wall) and (not t_thru_r_wall):
                utils.reset_piece(globs.current_piece)
                globs.current_piece.rotate()
                utils.insert_piece(globs.current_piece)
                Canvas.draw_board()

    elif (dir == "DOWN"):
        if not collided:
            globs.current_piece.move_down()
            utils.insert_piece(globs.current_piece)
            Canvas.draw_board()

    elif (dir == "LEFT"):
        if not globs.current_piece.l_collision():
            globs.current_piece.move_left()
            utils.insert_piece(globs.current_piece)
            Canvas.draw_board()

    elif (dir == "utils.right"):
        if not globs.current_piece.r_collision():
            globs.current_piece.move_right()
            utils.insert_piece(globs.current_piece)
            Canvas.draw_board()

    elif dir == "DROP":
        utils.drop_to_bottom(globs.current_piece)
        utils.insert_piece(globs.current_piece)
        globs.dropped = True
        Canvas.draw_board()

    elif dir == "QUIT":
        Canvas.clear()
        exit()

    elif dir == "PAUSE":
        input("Press Enter to resume.")

    # if dir:
    #     input("dir is: " + dir)



def get_dir(delay):

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = "DUMMY_TEXT"
    try:
        tty.setraw(sys.stdin.fileno())
        i, o, e = select.select( [sys.stdin], [], [], delay )
        if (i):
            # time.sleep(4)
            # ch = sys.stdin.read(3).strip()
            p1 = sys.stdin.read(1).strip()
            p2 = ""
            if(p1 == "["):
                p2 = sys.stdin.read(1).strip()
            ch = p1 + p2
            # if p2:
            #     print(ch)
                # time.sleep(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # if ch == "qqq":
    if ch == "q":
        return "QUIT"
    elif ch == "w" or ch == "W" or ch == "5":
        return "UP"
    elif ch == "s" or ch == "S" or ch == "2":
        return "DOWN"
    elif ch == "d" or ch == "D" or ch == "3":
        return "utils.right"
    elif ch == "a" or ch == "A" or ch == "1":
        return "LEFT"
    elif ch == "":
        return "DROP"
    elif ch == "p":
        return "PAUSE"

    elif ch == "[A":
        return "UP"
    elif ch == "[B":
        return "DOWN"
    elif ch == "[C":
        return "utils.right"
    elif ch == "[D":
        return "LEFT"
