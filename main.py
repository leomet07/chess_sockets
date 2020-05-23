import os
from generate_full_textures import generate_full_textures

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pygame
import pieces

pygame.init()
winh = 500
winw = winh
win = pygame.display.set_mode((winw, winh))

imgs = generate_full_textures("img")
print(imgs)
pygame.display.set_caption("Chess")


class Board:
    def __init__(self):
        self.r = 8
        self.c = 8

        self.pieces = []
        for row in range(0, self.r):
            for column in range(0, self.c):
                if row == 1:
                    self.pieces.append(pieces.Pawn(column, row, "white"))

                elif row == 6:
                    self.pieces.append(pieces.Pawn(column, row, "black"))

                if row == 0:
                    if column == 0 or column == 7:
                        self.pieces.append(pieces.Rook(column, row, "white"))

        self.pieces.append(pieces.Pawn(4, 0, "white"))
        self.print_board()
        # start intial pawn line up

        self.print_board()

    def print_board(self):
        print("---------------------")


def update():

    pass


board = Board()
offset = 20
bx = offset
by = offset
bw = winw - (offset * 2)
bh = winh - (offset * 2)
square_w = bw // board.r
square_h = bh // board.c

def draw():

    win.fill([146, 144, 255])

    # draw background grids

    # for dev grid
    

    pygame.draw.rect(win, (255, 0, 0), [bx, by, bw, bh], 0)
    pygame.draw.rect(win, (0, 0, 0), [bx - 1, by - 1, bw + 1, bh + 1], 1)

    # draw lines
    

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

        piece_offset = 5

        width = square_w - piece_offset
        height = square_h - piece_offset
        """
        pygame.draw.rect(
            win,
            colors[piece.color],
            [
                ((piece.pos.x + 1) * square_w) - (square_w // 2 - width // 2),
                ((8 - (piece.pos.y)) * square_h) - (square_h // 2 - height // 2),
                width,
                height,
            ],
            0,
        )
        """

        char = pygame.transform.scale(
            imgs[str(piece.color)][str(piece.type).lower()], (width, height)
        )
        win.blit(
            char,
            (
                ((piece.pos.x) * (square_w)) + offset + (2),
                ((7 - (piece.pos.y)) * (square_h)) + offset + (2),
            ),
        )

    pygame.display.update()


clock = pygame.time.Clock()

run = True
last_sector = []
while run:
    clock.tick(60)
    for event in pygame.event.get():

        # check if window was losed to stop the game loop
        if event.type == pygame.QUIT:
            run = False

    # run update after key recog
    mouse_cords = pygame.mouse.get_pos()
    #print(mouse_cords)

    sector_x  = (mouse_cords[0] - 20) // square_w
    sector_y  = (mouse_cords[1] - 20) // square_h
    if sector_x < 0:
        sector_x = 0
        
    if sector_y < 0:
        sector_y = 0

    # reverse the y
    sector_y = 7 - sector_y

    sector = [sector_x, sector_y]
    
    print((sector_x, sector_y))


    update()
    draw()

    last_sector = sector

pygame.quit()
