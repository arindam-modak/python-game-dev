import pygame, sys

pygame.init()
WIDTH,HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
img_bug = pygame.image.load("bug3.png")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,0,100))
    screen.blit(img_bug , (200,80))
    
    pygame.display.flip()
