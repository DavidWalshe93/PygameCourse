"""
Author:     David Walshe
Date:       28 May 2020
"""

# core
import sys
import os

# 3rd partt
import pygame

# Init Pygame
pygame.init()

# Retrieve audio file
audio = os.path.join(os.path.pardir, os.environ["GOLEM_AUDIO"], "golem_attack.mp3")
audio = audio.replace("\\", "/")
print(audio)

# Setup sound playback object
soundObj = pygame.mixer.Sound(audio)
soundObj.play()

# Wait 2 seconds while the sound plays.
import time
time.sleep(2)   # wait and let the sound play for 1 second

# Stop the sound.
soundObj.stop()
