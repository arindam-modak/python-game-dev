import pygame, sys, classes, random

def process(bug,FPS,total_frames):

    # processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        classes.Bug.going_right = True
        bug.image = pygame.image.load("images/bug2right.png")
        bug.velx = 5
    elif keys[pygame.K_a]:
        classes.Bug.going_right = False
        bug.image = pygame.image.load("images/bug2left.png")
        bug.velx = -5
    else:
        bug.velx = 0
        
    if keys[pygame.K_w]:
        bug.jumping = True

    if keys[pygame.K_SPACE]:
        p = classes.BugAttack(bug.rect.x,bug.rect.y, 40,20, "images/fire2.gif")
        if classes.Bug.going_right:
            p.velx = 8
        else:
            p.image = pygame.transform.flip(p.image, True, False)
            p.velx = -8

    spawn(FPS,total_frames)
    
def spawn(FPS,total_frames):

    four_seconds = FPS * 4

    if total_frames % four_seconds==0:
        r = random.randint(1,2)
        x = 1
        if r == 2:
            x = 640 - 40
        classes.Fly(x,130,40,40,"images/fly.png")





















