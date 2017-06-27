import pygame, sys, classes, random

def process(bug,FPS,total_frames):

    # processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                classes.BugAttack.fire = not classes.BugAttack.fire
                
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
        def direction():
            if classes.Bug.going_right:
                p.velx = 8
            else:
                p.image = pygame.transform.flip(p.image, True, False)
                p.velx = -8
        if (classes.BugAttack.fire):
            p = classes.BugAttack(bug.rect.x,bug.rect.y, "images/fire2.gif")
            direction()
        else:
            p = classes.BugAttack(bug.rect.x,bug.rect.y, "images/bolt.gif")
            direction()
            
    spawn(FPS,total_frames)
    collisions()
    
def spawn(FPS,total_frames):

    four_seconds = FPS * 4

    if total_frames % four_seconds==0:
        r = random.randint(1,2)
        x = 1
        if r == 2:
            x = 640 - 40
        classes.Fly(x,130,"images/fly.png")

def collisions():

    for fly in classes.Fly.List:
        if pygame.sprite.spritecollide(fly, classes.BugAttack.List, False):
            if classes.BugAttack.fire:
                fly.health -= fly.half_health
            else:
                fly.velx = 0

    for attack in classes.BugAttack.List:
        if pygame.sprite.spritecollide(attack, classes.Fly.List, False):
            attack.rect.x = 2 * -attack.rect.width
            attack.destroy()
            
















