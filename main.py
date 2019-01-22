import board, Canvas, utils, time, globs, square
from pieces import *

def main():
    globs.start_time = time.time()
    state()


def state():
    board.populate()
    utils.spawn_new()

    while not utils.check_loss():
        # print(utils.elapsed_time())
        # thresh = round(utils.elapsed_time() % globs.delay, 2)
        # print(thresh)
        if (utils.elapsed_time() % globs.delay == 0):
            Canvas.draw_board()
            if(not globs.current_piece.collision()):
                globs.current_piece.move_down()
                utils.insert_piece(globs.current_piece)
            else:
                utils.de_select_piece(globs.current_piece)
                utils.clear_board()
                # print("DONE CLEARING")
                # time.sleep(1)
                utils.spawn_new()
                # print("SPAWNED")
            # time.sleep(0.1)

        if globs.current_piece.collision():
            Canvas.draw_board()
            utils.actions(utils.get_dir(0.2))
        else:
            utils.actions(utils.get_dir(0.05))



if __name__ == '__main__':
    main()
