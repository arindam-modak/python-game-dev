import pygame, sys

pygame.init()
WIDTH,HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

clr1 = (22,122,211)
clr2 = (0,44,166)
clr3 = (34,55,245)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x1 = 0
    y1 = 0
    x2 = 640
    y2 = 360
    thickness = 5
    x = 40
    y = 40
    width = 300
    height = 45
    x3 = 350
    y3 = 200
    radius = 80
    hallow = 40
    
    screen.fill((0,0,100))
    
    pygame.draw.line(screen, clr2, (x1, y1),(x2,y2),thickness)
    pygame.draw.rect(screen, clr3, (x, y,width,height))
    pygame.draw.circle(screen,clr1,(x3,y3),radius,hallow)
    
    pygame.display.flip()
