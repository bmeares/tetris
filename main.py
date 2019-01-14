import board, Canvas, utils, time, globs, square
from pieces import *

def main():
    globs.start_time = time.time()
    state()


def state():
    board.populate()
    utils.spawn_new()

    while True:
        if (utils.elapsed_time() % 0.5 == 0):
            Canvas.draw_board()
            if(not globs.current_piece.collision()):
                globs.current_piece.move_down()
                utils.insert_piece(globs.current_piece)
            else:
                utils.de_select_piece(globs.current_piece)
                utils.spawn_new()
        utils.actions(utils.get_dir())



if __name__ == '__main__':
    main()
