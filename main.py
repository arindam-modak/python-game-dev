import pygame, sys
from classes import *
from process import process

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 24

background = pygame.image.load("images/forest.jpg")
bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug2right.png")
fly = Fly(40,100,40,40,"images/fly.png")
fly1 = Fly(40,100,40,40,"images/fly.png")
fly2= Fly(40,100,40,40,"images/fly.png")
fly3= Fly(40,100,40,40,"images/fly.png")

while True:

    process(bug)
    
    bug.motion(SCREENWIDTH,SCREENHEIGHT)
    Fly.movement(SCREENWIDTH)
    #screen.fill((255,0,200))
    screen.blit(background,(0,0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
