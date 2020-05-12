import pygame as pygame
import os

pygame.init()
winh = 500
winw = winh
win = pygame.display.set_mode((winw, winh))

pygame.display.set_caption("Selest")


class Board:
    def __init__(self):
        self.r = 8
        self.c = 8

        self.spaces = []
        for row in range(self.r):
            appender = []
            for column in range(self.c):
                appender.append("")

            self.spaces.append(appender)

        self.print_board()
        # start intial pawn line up
        for c in range(self.c):
            self.spaces[1][c] = "PAWN WHITE"
            self.spaces[6][c] = "PAWN BLACK"

        self.print_board()

    def print_board(self):
        print("---------------------")
        for i in range(len(self.spaces)):
            row = self.spaces[i]
            print(str(i) + str(row) + str(i))


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
    for i in range(len(board.spaces)):
        row = board.spaces[i]

        for c in range(len(row)):
            piece = row[c]
            if piece == "PAWN WHITE":
                pygame.draw.rect(
                    win,
                    (255, 255, 255),
                    [(c + 1) * square_w, (i + 1) * square_h, 20, 20],
                    0,
                )
            elif piece == "PAWN BLACK":
                pygame.draw.rect(
                    win, (0, 0, 0), [(c + 1) * square_w, (i + 1) * square_h, 20, 20], 0,
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
