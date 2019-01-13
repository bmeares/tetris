from square import Square

SIZE = 4

class Piece:
    def __init__(self):
        self.squares = []
        global SIZE
        for i in range(SIZE):
            self.squares.append([])

        for i in range(SIZE):
            for j in range(SIZE):
                self.squares[i].append(Square(False, "none", i, j))

    def set_color(self, color):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                self.squares[i][j].color = color

    def rotate(self):
        array_2d = self.squares
        list_of_tuples = zip(*array_2d[::-1])
        return [list(elem) for elem in list_of_tuples]

        # global SIZE
        # N = SIZE
        # mat = self.squares
        #
        # # Consider all squares one by one
        # for x in range(0, int(N/2)):
        #
        #     # Consider elements in group
        #     # of 4 in current square
        #     for y in range(x, N-x-1):
        #
        #         # store current cell in temp variable
        #         temp = mat[x][y]
        #
        #         # move values from right to top
        #         mat[x][y] = mat[y][N-1-x]
        #
        #         # move values from bottom to right
        #         mat[y][N-1-x] = mat[N-1-x][N-1-y]
        #
        #         # move values from left to bottom
        #         mat[N-1-x][N-1-y] = mat[N-1-y][x]
        #
        #         # assign temp to left
        #         mat[N-1-y][x] = temp
