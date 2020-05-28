"""
Author:     David Walshe
Date:       28 May 2020
"""

# core
import sys
import os

# 3rd partt
import pygame
from pygame.locals import QUIT

# custom libs
from res.colors import WHITE



GOLEM_WALKING = os.path.join(os.pardir, os.environ["GOLEM_WALKING"], "Golem_01_Walking_000.png")

GOLEM_WALKING = GOLEM_WALKING.replace("\\", "/")

print(GOLEM_WALKING)

pygame.init()

FPS = 60
fps_clock = pygame.time.Clock()

DISPLAY_SURFACE = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption("Animation")

golem = pygame.image.load(GOLEM_WALKING)
golem_x = 10
golem_y = 10
direction = "right"

while True:
    DISPLAY_SURFACE.fill(WHITE)

    if direction == 'right':
        golem_x += 5
        if golem_x == 280:
            direction = 'down'
    elif direction == 'down':
        golem_y += 5
        if golem_y == 220:
            direction = 'left'
    elif direction == 'left':
        golem_x -= 5
        if golem_x == 10:
            direction = 'up'
    elif direction == 'up':
        golem_y -= 5
        if golem_y == 10:
            direction = 'right'

    DISPLAY_SURFACE.blit(golem, (golem_x, golem_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps_clock.tick(FPS)
