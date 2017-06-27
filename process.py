import pygame, sys

def process(bug):

    # processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        bug.image = pygame.image.load("images/bug2right.png")
        bug.velx = 5
        bug.vely = 0
    elif keys[pygame.K_a]:
        bug.image = pygame.image.load("images/bug2left.png")
        bug.velx = -5
        bug.vely = 0
    elif keys[pygame.K_w]:
        bug.image = pygame.image.load("images/bug2up.png")
        bug.vely = -5
        bug.velx = 0
    elif keys[pygame.K_s]:
        bug.image = pygame.image.load("images/bug2down.png")
        bug.vely = +5
        bug.velx = 0
    else:
        bug.velx = 0
        bug.vely = 0






















