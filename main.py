import pygame, sys
from classes import *
from process import process

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 24
total_frames = 0
background = pygame.image.load("images/forest.jpg")
bug = Bug(0,SCREENHEIGHT - 40,"images/bug2right.png")


while True:

    process(bug,FPS,total_frames)
    if Game.start:
        bug.motion(SCREENWIDTH,SCREENHEIGHT)
        #Fly.movement(SCREENWIDTH)
        Fly.update_all(SCREENWIDTH,SCREENHEIGHT)
        BugAttack.movement()
        total_frames += 1
        #screen.fill((255,0,200))
        screen.blit(background,(0,0))
        Fly.score(screen)
        BaseClass.allsprites.draw(screen)
        BugAttack.List.draw(screen)
        pygame.display.flip()
    else:
        screen.fill((200,100,100))
        font = pygame.font.SysFont(None, 40)
        text = font.render("START ", True,  (0,255,50))
        screen.blit(text,(SCREENWIDTH/2,SCREENHEIGHT/2))
        text = font.render("(Press SPACE)", True,  (50,100,50))
        screen.blit(text,(SCREENWIDTH/2 - 20,SCREENHEIGHT/2 + 60))
        Fly.score(screen)
        pygame.display.flip()
        
    clock.tick(FPS)
