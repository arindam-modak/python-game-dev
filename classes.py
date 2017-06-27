import pygame

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
        self.velx = 0
        self.vely = 0
        
    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        predicted_locationx = self.rect.x + self.velx
        predicted_locationy = self.rect.y + self.vely
        if predicted_locationx < 0:
            self.velx = 0
        elif predicted_locationx + self.width > SCREENWIDTH:
            self.velx = 0
        elif predicted_locationy  < 0:
            self.vely = 0
        elif predicted_locationy + self.height > SCREENHEIGHT:
            self.vely = 0
        
        self.rect.x += self.velx
        self.rect.y += self.vely
        
