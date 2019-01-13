import board, Canvas, utils, time, globs
from pieces import *

def main():
    globs.start_time = time.time()
    # input("input: ")
    state()


def state():
    board.populate()
    utils.spawn_new()

    while True:
        if (utils.elapsed_time() % 0.5 == 0):
            Canvas.draw_board()
            if utils.still_falling(globs.current_piece):
                globs.current_piece.move_down()
            else:
                utils.spawn_new()
        utils.actions(utils.get_dir())



if __name__ == '__main__':
    main()
