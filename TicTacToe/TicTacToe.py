"""
Author:     David Walshe
Date:       28 May 2020
"""

import pygame
from pygame.locals import QUIT


from res.colors import WHITE, BLACK

pygame.init()

FPS = 30
fps_clock = pygame.time.Clock()

DISPLAY_SURFACE = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption("Tic Tac Toe")

X = pygame.image.load("X.png")
O = pygame.image.load("O.png")


def draw_board():
    X_SPACE = 333
    Y_SPACE = 333
    for x, y in zip(range(0, X_SPACE*2, X_SPACE), range(0, Y_SPACE*2, Y_SPACE)):
        pygame.draw.line(DISPLAY_SURFACE, BLACK, (0, y+Y_SPACE), (1000, y+Y_SPACE), 4)
        pygame.draw.line(DISPLAY_SURFACE, BLACK, (x + X_SPACE, 0), (x + X_SPACE, 1000), 4)


def adj_placement(x: int, y: int):
    x = x - 70
    y = y - 70

    return (x, y)


while True:
    DISPLAY_SURFACE.fill(WHITE)

    draw_board()
    DISPLAY_SURFACE.blit(X, adj_placement(0, 0))
    DISPLAY_SURFACE.blit(O, adj_placement(333, 0))
    DISPLAY_SURFACE.blit(X, adj_placement(0, 0))
    DISPLAY_SURFACE.blit(O, adj_placement(333, 666))
    DISPLAY_SURFACE.blit(X, adj_placement(0, 666))
    DISPLAY_SURFACE.blit(O, adj_placement(666, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps_clock.tick(FPS)