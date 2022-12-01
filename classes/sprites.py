import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        '''
        Constructeur de la classe Generic\n
        Paramètres:\n
                    - pos : Position x et y 
                    - surf : Image relié à l objet (deviendra rect)
                    - groups 
        '''
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        rect = self.rect
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class Generic_Railway(Generic):
    '''
    Constructeur d'une voie Railway
    '''
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups) 
        
class Generic_Train(Generic):
    '''
    Constructeur d'un train Train
    '''
    def __init__(self, pos, surf, groups, heure_depart):
        self.heure_depart = heure_depart
        super().__init__((pos[0]+50, pos[1]-180), surf, groups, z= 6) 

class Generic_Box(Generic):
    '''
    Constructeur d'un préparateur de train (computer) Box
    '''
    def __init__(self, pos, surf, groups, railway_number):
        super().__init__((pos[0]-250, pos[1]+100), surf, groups, z= 6) 
        
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.1,-self.rect.height * 0.1)
        self.railway_number = railway_number