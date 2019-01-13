import board, Canvas, utils, time
from pieces import *

def main():
    state()


def state():
    board.populate()
    t = T_piece()
    utils.insert_piece(t)

    for i in range(board.HEIGHT):
        Canvas.draw_board()
        utils.move_down(t)
        t.rotate()
        time.sleep(0.5)




if __name__ == '__main__':
    main()
