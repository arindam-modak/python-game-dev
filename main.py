import pygame, sys
from classes import *
from process import process

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug2right.png")

while True:

    process(bug)
    
    bug.motion(SCREENWIDTH,SCREENHEIGHT)
    screen.fill((255,0,200))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
