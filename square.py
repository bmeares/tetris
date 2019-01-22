import colors

class Square:
    def __init__(self, pieceStatus, color, row, col):
        self.pieceStatus = pieceStatus
        self.selected = False
        self.debug = False
        self.spawn = False
        self.color = color
        self.row = row
        self.col = col

    def __str__(self):
        # highlight selected pieces for debugging
        # if self.selected:
        #     return colors.BRIGHT_CYAN_BG + "  " + colors.RESET
        if self.debug:
            return colors.BRIGHT_CYAN_BG + "  " + colors.RESET

        # if self.spawn:
        #     return colors.BRIGHT_CYAN_BG + "  " + colors.RESET

        if self.pieceStatus:
            if self.color == "blue":
                return colors.DULL_BLUE_BG + "  " + colors.RESET
            elif self.color == "b_blue":
                return colors.BRIGHT_BLUE_BG + "  " + colors.RESET
            elif self.color == "green":
                return colors.DULL_GREEN_BG + "  " + colors.RESET
            elif self.color == "b_green":
                return colors.BRIGHT_GREEN_BG + "  " + colors.RESET
            elif self.color == "yellow":
                return colors.DULL_YELLOW_BG + "  " + colors.RESET
            elif self.color == "b_yellow":
                return colors.BRIGHT_YELLOW_BG + "  " + colors.RESET
            elif self.color == "red":
                return colors.DULL_RED_BG + "  " + colors.RESET
            elif self.color == "b_red":
                return colors.BRIGHT_RED_BG + "  " + colors.RESET
            elif self.color == "cyan":
                return colors.DULL_CYAN_BG + "  " + colors.RESET
            else:
                return colors.RESET + "  "

        else:
            # TODO RESET THIS
            return  " ."

def de_select(args, sq):
    sq.selected = False

def select(args, sq):
    sq.selected = True

class boardSquare(Square):
    def __init__(self, row, col):
        Square.__init__(self, False, "none", row, col)
