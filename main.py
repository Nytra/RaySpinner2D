# this is going to be some kind of graphics demo that has a bunch of lines all moving around
# in a systematic and hypnotising way, probably using some kind of math

# post-completion report: yeah i did pretty much what i said i was gonna do

# next: make the origin point move to the beat of a song

import pygame
import math
import random
from pygame.locals import *
from pygame import mixer

NUM_LINES = 200
WIDTH = 800
HEIGHT = 600
AUTO = True

def random_point():
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    return x, y

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

flags = HWSURFACE | DOUBLEBUF
bpp = 16

pygame.init()
mixer.init()
pygame.display.set_caption("Lines")
screen = pygame.display.set_mode((800, 600), flags, bpp)
game_over = False
ang_init = 0
ang = ang_init
clock = pygame.time.Clock()

line_origin = random_point()
line_colour = random_colour()

mixer.music.load("the_road_ahead.mp3")
mixer.music.play()

start_time = pygame.time.get_ticks()
spin_start_time = pygame.time.get_ticks()

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                line_origin = random_point()
            elif event.key == pygame.K_q:
                game_over = True
    
    screen.fill((0, 0, 0))
    ang = ang_init
    radius = math.sqrt(WIDTH ** 2 + HEIGHT ** 2)

    for i in range(NUM_LINES):
        # polar coordinates : x_origin + radius * cos(ang)
        x2 = radius * math.cos(ang)
        y2 = radius * math.sin(ang)
        pygame.draw.line(screen, line_colour, line_origin, (x2, y2))
        ang += 360 / NUM_LINES
    
    if pygame.time.get_ticks() - spin_start_time > 1000 / 15:
        spin_start_time = pygame.time.get_ticks()
        ang_init += 1
        if ang_init >= 360:
            ang_init = 0

    # 100 beats per minute , 
    if AUTO and (pygame.time.get_ticks() - start_time) > 60 / 107 * 1000:
        line_origin = random_point()
        line_colour = random_colour()
        start_time = pygame.time.get_ticks()

    pygame.display.update()

    clock.tick(999)

pygame.quit()