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
    elif keys[pygame.K_a]:
        bug.image = pygame.image.load("images/bug2left.png")
        bug.velx = -5
    else:
        bug.velx = 0
        
    if keys[pygame.K_w]:
        bug.jumping = True
    
    






















