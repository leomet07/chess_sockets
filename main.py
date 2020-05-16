import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pygame


pygame.init()
winh = 500
winw = winh
win = pygame.display.set_mode((winw, winh))

pygame.display.set_caption("Selest")


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece:
    def __init__(self, x, y, piece_type, color):
        self.pos = Pos(x, y)

        self.color = color
        self.type = piece_type


class Board:
    def __init__(self):
        self.r = 8
        self.c = 8

        self.pieces = []
        for row in range(0, self.r):
            for column in range(0, self.c):
                if row == 1:
                    self.pieces.append(Piece(column, row, "PAWN", "white"))
                elif row == 6:
                    self.pieces.append(Piece(column, row, "PAWN", "black"))

        self.print_board()
        # start intial pawn line up

        self.print_board()

    def print_board(self):
        print("---------------------")


def update():

    pass


board = Board()


def draw():

    win.fill([146, 144, 255])

    # draw background grids

    # for dev grid
    offset = 20
    bx = offset
    by = offset
    bw = winw - (offset * 2)
    bh = winh - (offset * 2)

    pygame.draw.rect(win, (255, 0, 0), [bx, by, bw, bh], 0)
    pygame.draw.rect(win, (0, 0, 0), [bx - 1, by - 1, bw + 1, bh + 1], 1)

    # draw lines
    square_w = bw / board.r
    square_h = bh / board.c

    for row in range(1, board.r):
        x = row * (square_w) + offset
        pygame.draw.line(win, (0, 0, 0), (x, by), (x, by + bh - 1))
    # draw lines
    for column in range(1, board.c):
        y = column * (square_h) + offset
        pygame.draw.line(win, (0, 0, 0), (bx, y), (bx + bw - 1, y))

    # draw in pieces

    colors = {"black": [0, 0, 0], "white": [255, 255, 255]}
    for i in range(len(board.pieces)):

        piece = board.pieces[i]

        if piece.type == "PAWN":
            pygame.draw.rect(
                win,
                colors[piece.color],
                [
                    (8 - (piece.pos.x)) * square_w,
                    (8 - (piece.pos.y)) * square_h,
                    20,
                    20,
                ],
                0,
            )

    pygame.display.update()


clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():

        # check if window was losed to stop the game loop
        if event.type == pygame.QUIT:
            run = False

    # run update after key recog
    update()
    draw()


pygame.quit()
