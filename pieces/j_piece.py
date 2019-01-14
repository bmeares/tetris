from pieces import Piece
from square import Square

class J_piece(Piece):
    def __init__(self):
        Piece.__init__(self)

        self.squares[0][2].pieceStatus = True
        self.squares[1][2].pieceStatus = True
        self.squares[2][2].pieceStatus = True
        self.squares[2][1].pieceStatus = True

        self.set_color("b_blue")
        # [
        # [0, 0, 1, 0]
        # [0, 0, 1, 0]
        # [0, 1, 1, 0]
        # [0, 0, 0, 0]
        # ]


    # FOR TESTING ONLY! Printing individual pieces will break the board
    def __str__(self):
        out = ""
        for row in range(len(self.squares)):
            for col in range(len(self.squares[row])):
                out += str(self.squares[row][col])
            out += "\n"
        return out
