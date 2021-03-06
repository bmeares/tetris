import colors, globs

class Square:
    def __init__(self, pieceStatus, color, row, col):
        self.pieceStatus = pieceStatus
        self.selected = False
        self.debug = False
        self.spawn = False
        self.color = color
        self.row = row
        self.col = col
        self.clear = False
        self.preview = False


    def __str__(self):
        # highlight selected pieces for debugging
        # if self.selected:
        #     return colors.BRIGHT_CYAN_BG + "  " + colors.RESET
        if self.debug:
            return colors.BRIGHT_CYAN_BG + "  " + colors.RESET

        if globs.mono:
            if self.pieceStatus:
                if self.preview:
                    if not globs.ascii:
                        return "╳╳"
                    else:
                        return "::"
                else: # not a preview
                    if not globs.ascii:
                        return colors.BLOCK + colors.BLOCK
                    else:
                        return "##" # returns only for -am
            else:
                return "  "


        out = ""
        block = "  "
        if self.clear:
            out += colors.BLINK

        if self.preview:
            if globs.ascii:
                block = "::"
            else:
                block = "╳╳"
            block = colors.DARK_BLACK_FG + block

            # print(block)
            # input()

        # if self.spawn:
        #     return colors.BRIGHT_CYAN_BG + "  " + colors.RESET

        if self.pieceStatus:
            if self.color == "blue":
                out = colors.DULL_BLUE_BG + block + colors.RESET
            elif self.color == "b_blue":
                out = colors.BRIGHT_BLUE_BG + block + colors.RESET
            elif self.color == "green":
                out = colors.DULL_GREEN_BG + block + colors.RESET
            elif self.color == "b_green":
                out = colors.BRIGHT_GREEN_BG + block + colors.RESET
            elif self.color == "yellow":
                out = colors.DULL_YELLOW_BG + block + colors.RESET
            elif self.color == "b_yellow":
                out = colors.BRIGHT_YELLOW_BG + block + colors.RESET
            elif self.color == "red":
                out = colors.DULL_RED_BG + block + colors.RESET
            elif self.color == "b_red":
                out = colors.BRIGHT_RED_BG + block + colors.RESET
            elif self.color == "cyan":
                out = colors.DULL_CYAN_BG + block + colors.RESET
            else:
                out = colors.RESET + block

        else:
            # TODO RESET THIS
            out = block + colors.RESET

        return out

def de_select(args, sq):
    sq.selected = False

def select(args, sq):
    sq.selected = True

def prev(args, sq):
    sq.preview = True


# def init_sq():
#     if globs.mono:


# def ascii_sq_str(sq):


# def unicode_sq_str(sq):


class boardSquare(Square):
    def __init__(self, row, col):
        Square.__init__(self, False, "none", row, col)
