import pygame
from classes.train import *


class TGV(Train):
    def __init__(self, capacite, numeroTrain, heureDepart) -> None:
        '''
        Constructeur de la classe TGV héritant de la classe Train\n
        Paramètres :\n
                    - capacite (int) : Capacite du TGV
                    - numeroTrain (int) : Numéro du train
                    - heureDepart (int) : Heure de départ du TGV (en secondes)
        '''
        self.background = pygame.image.load("graphics/trains/TGV.png")

        self.background = pygame.transform.scale(self.background, (3000,200)).convert_alpha()
        super().__init__("TGV", capacite, numeroTrain, heureDepart)

    def getBackground(self) -> pygame.Surface:
        '''
        Accesseur du background (image) du train TGV\n
        Retourne:\n
                    self.background (Surface) : Background du TGV
        '''
        return self.background

    def getHeureDepart(self) -> int:
        '''
        Accesseur de l heure de départ du TGV
        '''
        return super().getHeureDepart()
        
    def setHeureDepart(self, newHeureDepart) -> None:
        '''
        Modificateur de l heure de départ du TGV\n
        Paramètres:\n
                    - newHeureDepart (int) : Nouvelle heure de départ (en secondes)
        '''
        return super().setHeureDepart(newHeureDepart)