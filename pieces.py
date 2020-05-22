class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece:
    def __init__(self, x, y, color):
        self.pos = Pos(x, y)

        self.color = color


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.type = "PAWN"

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.type = "Rook"

