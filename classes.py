import pygame, math
from random import randint

class BaseClass(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()
    def __init__(self,x,y,image_string):
        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self, ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self

class Bug(BaseClass):

    List = pygame.sprite.Group()
    going_right = True
    
    def __init__(self,x,y,image_string):

        BaseClass.__init__(self,x,y,image_string)
        Bug.List.add(self)
        self.velx, self.vely = 0, 5
        self.jumping, self.go_down = False, False
        
    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        predicted_locationx = self.rect.x + self.velx
        predicted_locationy = self.rect.y + self.vely
        
        if predicted_locationx < 0:
            self.velx = 0
        elif predicted_locationx + self.rect.width > SCREENWIDTH:
            self.velx = 0
            
        if predicted_locationy + self.rect.width > SCREENHEIGHT:
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

    count = 0
    List = pygame.sprite.Group()
    def __init__(self,x,y,image_string):
        BaseClass.__init__(self,x,y,image_string)
        Fly.List.add(self)
        self.go_down = False
        self.vely = 2
        self.health = 100
        self.half_health = self.health/2.0
        self.velx = randint(1, 4)
        self.amplitude, self.period = randint(20,140), randint(4, 5)/100.0

    @staticmethod
    def update_all(SCREENWIDTH,SCREENHEIGHT):
        for fly in Fly.List:
            
            fly.fly(SCREENWIDTH,SCREENHEIGHT)
            
            if fly.health <= 0:
                fly.destroy(Fly)
                Fly.count += 1
                
    @staticmethod
    def score(screen):
        font = pygame.font.SysFont(None, 40)
        text = font.render("Score : "+str(Fly.count), True,  (255,255,255))
        screen.blit(text,(0,0))
    
    def fly(self, SCREENWIDTH,SCREENHEIGHT):
        if self.rect.x + self.rect.width > SCREENWIDTH or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image,True, False)
            self.velx = -self.velx
            
        self.rect.x += self.velx

        # a * sin(bx + c) + y
        if self.go_down:
            if self.rect.y+self.rect.height >= SCREENHEIGHT:
                self.vely = 0
            self.rect.y += self.vely
        else:
            self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 140
        
        #@staticmethod
        #def movement(SCREENWIDTH):
        #   for fly in Fly.List:
        #        fly.fly(SCREENWIDTH)
    
class BugAttack(pygame.sprite.Sprite):
    List = pygame.sprite.Group()
    normal_list = []
    fire = True
    
    def __init__(self,x,y,image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        try:
            last_element = BugAttack.normal_list[-1]
            difference = abs(self.rect.x - last_element.rect.x)

            if difference < self.rect.width:
                return
        except Exception:
            pass
        
        BugAttack.normal_list.append(self)
        BugAttack.List.add(self)
        self.velx = None

    @staticmethod
    def movement():
        for attack in BugAttack.List:
            attack.rect.x += attack.velx
    
    def destroy(self):
        BugAttack.List.remove(self)
        BugAttack.normal_list.remove(self)
        del self
        
class Game:
    end = False
    start = False
    
