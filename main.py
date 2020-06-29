# this is going to be some kind of graphics demo that has a bunch of lines all moving around
# in a systematic and hypnotising way, probably using some kind of math

# post-completion report: yeah i did pretty much what i said i was gonna do

import pygame
import math
from pygame.locals import *

NUM_LINES = 200
WIDTH = 800
HEIGHT = 600

flags = HWSURFACE | DOUBLEBUF
bpp = 16

pygame.init()
pygame.display.set_caption("Lines")
screen = pygame.display.set_mode((800, 600), flags, bpp)
game_over = False
ang_init = 0
ang = ang_init
clock = pygame.time.Clock()

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("Hello, world!")
    
    screen.fill((0, 0, 0))
    ang = ang_init
    radius = math.sqrt(WIDTH ** 2 + HEIGHT ** 2)
    
    for i in range(NUM_LINES):
        # polar coordinates : x_origin + radius * cos(ang)
        x2 = radius * math.cos(ang)
        y2 = radius * math.sin(ang)
        pygame.draw.line(screen, (255, 0, 0), (WIDTH / 2, HEIGHT / 2), (x2, y2))
        ang += 360 / NUM_LINES
    
    ang_init += 1
    if ang_init >= 360:
        ang_init = 0

    pygame.display.update()

    clock.tick(15)

pygame.quit()