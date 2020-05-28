"""
Author:     David Walshe
Date:       28 May 2020
"""

import pygame
import sys
from pygame.locals import *

from res.colors import WHITE, RED, GREEN, BLUE, BLACK

pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

DISPLAY_SURFACE.fill(WHITE)

# Pentagon
pygame.draw.polygon(DISPLAY_SURFACE, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Z shapes
pygame.draw.line(DISPLAY_SURFACE, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAY_SURFACE, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAY_SURFACE, BLUE, (60, 120), (120, 120), 4)

# Circle
pygame.draw.circle(DISPLAY_SURFACE, BLUE, (300, 50), 20, 0)

# Ellipse
pygame.draw.ellipse(DISPLAY_SURFACE, RED, (300, 250, 40, 80), 1)

# Rectangle
pygame.draw.rect(DISPLAY_SURFACE, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAY_SURFACE)

pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
# Show if the surface is locked
# If it is locked, drawing images cannot take place.
# Raises a "pygame.error: Surfaces must not be locked during blit" Exception if locked.
print(DISPLAY_SURFACE.get_locked())
del pixObj
print(DISPLAY_SURFACE.get_locked())


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
