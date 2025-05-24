import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
cat1x = 10
cat1y = 10
cat2x = 280
cat2y = 10
cat1Direction = 'right'
cat2Direction = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    # cat 1 direction
    if cat1Direction == 'right':
        cat1x += 5
        if cat1x == 280:
            cat1Direction = 'down'
    elif cat1Direction == 'down':
        cat1y += 5
        if cat1y == 220:
            cat1Direction = 'left'
    elif cat1Direction == 'left':
        cat1x -= 5
        if cat1x == 10:
            cat1Direction = 'up'
    elif cat1Direction == 'up':
        cat1y -= 5
        if cat1y == 10:
            cat1Direction = 'right'

    #cat 2 directions
    if cat2Direction == 'right':
        cat2x += 5
        if cat2x == 280:
            cat2Direction = 'up'
    elif cat2Direction == 'down':
        cat2y += 5
        if cat2y == 220:
            cat2Direction = 'right'
    elif cat2Direction == 'left':
        cat2x -= 5
        if cat2x == 10:
            cat2Direction = 'down'
    elif cat2Direction == 'up':
        cat2y -= 5
        if cat2y == 10:
            cat2Direction = 'left'

    DISPLAYSURF.blit(catImg, (cat1x, cat1y))
    DISPLAYSURF.blit(catImg, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)