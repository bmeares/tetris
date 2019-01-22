from square import Square
import copy, utils, board

SIZE = 4

class Piece:
    def __init__(self):
        self.squares = []
        global SIZE
        for i in range(SIZE):
            self.squares.append([])

        w_buff = int(int(board.WIDTH / 2) - ((SIZE / 2) + 1))

        for i in range(SIZE):
            for j in range(SIZE):
                # self.squares[i].append(Square(False, "none", (i - 1), j + w_buff))
                # self.squares[i].append(Square(False, "none", i, j + w_buff))
                self.squares[i].append(Square(False, "none", i, j + w_buff))
                # self.squares[i].append(Square(False, "none", i - 4, j + w_buff))

    def apply_to_squares(self, function, args=[]):
        flipped = False
        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                if self.squares[i][j].pieceStatus:
                    if(function(args, self.squares[i][j])):
                        flipped = True
        return flipped

    def apply_to_all(self, function, args=[]):
        flipped = False
        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                if(function(args, self.squares[i][j])):
                    flipped = True
        return flipped

    def collision(self):
        # collision for just one square
        def sq_collide(args, sq):
            # if not at the bottom, check if there's a piece below
            if sq.row >= board.HEIGHT - 1:
                return True
            else:
                return ((board.squares[sq.row + 1][sq.col].pieceStatus) and (not board.squares[sq.row + 1][sq.col].selected))

        return self.apply_to_squares(sq_collide, [])

    def l_collision(self):
        # collision for just one square
        def l_sq_collide(args, sq):
            # if not at the bottom, check if there's a piece below
            if sq.col <= 0:
                return True
            else:
                return ((board.squares[sq.row][sq.col - 1].pieceStatus) and (not board.squares[sq.row][sq.col - 1].selected))

        return self.apply_to_squares(l_sq_collide, [])

    def r_collision(self):
        # collision for just one square
        def r_sq_collide(args, sq):
            # if not at the bottom, check if there's a piece below
            if sq.col >= board.WIDTH - 1:
                return True
            else:
                return ((board.squares[sq.row][sq.col + 1].pieceStatus) and (not board.squares[sq.row][sq.col + 1].selected))

        return self.apply_to_squares(r_sq_collide, [])


    def set_color(self, color):
        args = [color]
        def sc(args, sq):
            sq.color = args[0]
        self.apply_to_squares(sc, args)

    def move_right(self):
        utils.reset_piece(self)
        def mr(args, sq):
            sq.col += 1
        self.apply_to_all(mr)
        # utils.insert_piece(self)

    def move_left(self):
        utils.reset_piece(self)
        def mr(args, sq):
            sq.col -= 1
        self.apply_to_all(mr)

    def move_down(self):
        utils.reset_piece(self)
        def mr(args, sq):
            sq.row += 1
        self.apply_to_all(mr)

    def rotate(self):
        # utils.reset_piece(self)
        array_2d = self.squares
        list_of_tuples = zip(*array_2d[::-1])
        rotated = [list(elem) for elem in list_of_tuples]

        mat = copy.deepcopy(self.squares)
        mat = clockwise(mat)

        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                row = self.squares[i][j].row
                col = self.squares[i][j].col
                mat[i][j].row = self.squares[i][j].row
                mat[i][j].col = self.squares[i][j].col
        self.squares = mat

def clockwise(mat):
    cols = [[], [], [], []]
    for col in range(len(mat[0])):
        for row in range(len(mat)):
            cols[col].append(mat[row][col])

    top_row = cols[0]
    for i in range(len(cols)):
        for j in range(len(cols)):
            mat[i][j] = cols[i][len(cols[0]) - 1 - j]

    return mat
