import pygame
from classes.train import Train


class TER(Train):
    def __init__(self, capacite, numeroTrain, heureDepart):
        '''
        Constructeur de la classe TER héritant de la classe Train\n
        Paramètres :\n
                    - capacite (int) : Capacite du TER
                    - numeroTrain (int) : Numéro du train
                    - heureDepart (int) : Heure de départ du TER (en secondes)
        '''
        self.background = pygame.image.load("graphics/trains/TER.png")

        self.background = pygame.transform.scale(self.background, (3000,200)).convert_alpha()

        super().__init__("TER", capacite, numeroTrain, heureDepart)



    def getBackground(self) -> pygame.Surface:
        '''
        Accesseur du background (image) du train TER\n
        Retourne:\n
                    self.background (Surface) : Background du TER
        '''
        return self.background

    def getHeureDepart(self) -> int:
        '''
        Accesseur de l heure de départ du train
        '''
        return super().getHeureDepart()

    def setHeureDepart(self, newHeureDepart) -> None:
        '''
        Modificateur de l heure de départ du train\n
        Paramètres:\n
                    - newHeureDepart (int) : Nouvelle heure de départ (en secondes)
        '''
        return super().setHeureDepart(newHeureDepart)