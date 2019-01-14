import colors

class Square:
    def __init__(self, pieceStatus, color, row, col):
        self.pieceStatus = pieceStatus
        self.selected = False
        self.color = color
        self.row = row
        self.col = col
#        preview

    def __str__(self):
        if self.selected:
            return colors.BRIGHT_CYAN_BG + "  " + colors.RESET


        if self.pieceStatus:
            if self.color == "blue":
                return colors.DULL_BLUE_BG + "  " + colors.RESET
            elif self.color == "b_blue":
                return colors.BRIGHT_BLUE_BG + "  " + colors.RESET
            elif self.color == "green":
                return colors.DULL_GREEN_BG + "  " + colors.RESET
            elif self.color == "yellow":
                return colors.DULL_YELLOW_BG + "  " + colors.RESET
            elif self.color == "red":
                return colors.DULL_RED_BG + "  " + colors.RESET
            elif self.color == "b_red":
                return colors.BRIGHT_RED_BG + "  " + colors.RESET
            else:
                return colors.RESET + "  "

        else:
            # TODO RESET THIS
            return colors.DULL_YELLOW_BG + "  " + colors.RESET

def de_select(args, sq):
    sq.selected = False

def select(args, sq):
    sq.selected = True
