import board, Canvas, utils, time, globs, square, sys, colors, kb
from pieces import *

def main():
    globs.start_time = time.time()
    if len(sys.argv):
        parse_args(sys.argv)
        colors.init_box()
    state()

def state():
    board.populate()
    utils.spawn_new()

    while not utils.check_loss():
        # print(utils.elapsed_time())
        # thresh = round(utils.elapsed_time() % globs.delay, 2)
        # print(thresh)
        #  if (utils.elapsed_time() % globs.delay == 0):
        t = str(utils.elapsed_time())
        #  print(t)
        drop_nums = globs.drop_lists[globs.current_level - 1]
        if (any(x in t for x in drop_nums)):
            Canvas.draw_board()

            if(not globs.current_piece.collision()):
                globs.current_piece.move_down()
                utils.insert_piece(globs.current_piece)

            else:
                # utils.reset_piece(globs.preview_pc)
                utils.de_select_piece(globs.current_piece)
                utils.clear_board()
                # print("DONE CLEARING")
                # time.sleep(1)
                utils.spawn_new()
                # print("SPAWNED")
                globs.num_placed += 1
                utils.check_level()
            # time.sleep(0.1)

        # give player 0.2 seconds to make a last-second adjustment
        if globs.current_piece.collision() and not globs.dropped:
            Canvas.draw_board()
            kb.actions(kb.get_dir(0.2))
        # give player 0.5 seconds to slide piece once made contact
        # TODO set timer, only stop accepting input once timer runs out
        # reset timer when key is pressed
        else:
            kb.actions(kb.get_dir(0.05))


def parse_args(args):
    args.pop(0) # remove main.py
    s = "".join(args)
    globs.ascii = ("a" in s)
    globs.mono = ("m" in s)

if __name__ == '__main__':
    main()
