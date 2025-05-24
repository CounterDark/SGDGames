import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
points = [
    (200, 50),
    (220, 130),
    (300, 130),
    (235, 180),
    (260, 260),
    (200, 210),
    (140, 260),
    (165, 180),
    (100, 130),
    (180, 130)
]
pygame.draw.polygon(DISPLAYSURF, GREEN, points)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
