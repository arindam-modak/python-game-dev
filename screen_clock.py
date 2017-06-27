import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

clock = pygame.time.Clock()
FPS = 24
totalframes = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    totalframes += 1
    
    
    pygame.display.flip()

    clock.tick(FPS)
