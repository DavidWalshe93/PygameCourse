"""
Author:         David Walshe
Date:           26/05/2020   
"""

# Core libs
import sys

# 3rd party libs
import pygame
from pygame.locals import *

print(pygame.__version__)

# Initialise Game
pygame.init()

# GAME Constants
DISPLAY_SURFACE = pygame.display.set_mode((400, 300))


pygame.display.set_caption('Hello World!')

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

