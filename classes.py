import pygame, math
from random import randint

class BaseClass(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

class Bug(BaseClass):

    List = pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):

        BaseClass.__init__(self,x,y,width,height,image_string)
        Bug.List.add(self)
        self.velx, self.vely = 0, 5
        self.jumping, self.go_down = False, False
        
    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        predicted_locationx = self.rect.x + self.velx
        predicted_locationy = self.rect.y + self.vely
        
        if predicted_locationx < 0:
            self.velx = 0
        elif predicted_locationx + self.width > SCREENWIDTH:
            self.velx = 0
            
        if predicted_locationy + self.width > SCREENHEIGHT:
            self.vely *= -1
            self.jumping, self.go_down = False, False
                
        self.rect.x += self.velx

        max_jump = 75
        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down = True
                self.vely *= -1
            
            self.rect.y += self.vely

class Fly(BaseClass):

    List = pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        BaseClass.__init__(self,x,y,width,height,image_string)
        Fly.List.add(self)
        self.velx = randint(1, 4)
        self.amplitude, self.period = randint(20,140), randint(4, 5)/100.0

    def fly(self, SCREENWIDTH):
        if self.rect.x + self.width > SCREENWIDTH or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image,True, False)
            self.velx = -self.velx
            
        self.rect.x += self.velx

        # a * sin(bx + c) + y

        self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 140
        
    @staticmethod
    def movement(SCREENWIDTH):
        for fly in Fly.List:
            fly.fly(SCREENWIDTH)
    
        
