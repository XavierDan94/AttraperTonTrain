from xmlrpc.client import Boolean
import pygame
from classes.box import *
class Railway:
    '''
    Classe qui représente une voie
    '''
    def __init__(self, railwayNumber, train, rectY):
        '''
        Constructeur de la classe Railway\n
        parametres :\n
                - self
                - railwayNumber (int) : Numéro de voie 
                - train (Train) : Train présent sur la voie
                - rectY (int) : Position y de la voie
        '''
        self.railway_number = railwayNumber # Numéro de la voie
        self.train = train # Train sur la voie

        self.rectX = 900 # Positionnement horizontal
        self.rectY = rectY # Positionnement vertical (dynamique)
        self.rectWidth = 600 # Largeur de la voie
        self.rectHeight = 100 # Hauteur de la voie

        # Visuel de la voie
        self.display_surface = pygame.display.get_surface() 
        self.railway = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)
        self.background = pygame.image.load("graphics/platform/platform.png")

        # Objet qui permet de préparer le train 
        self.bg_width = 3000 
        self.bg_height = 300
        self.background = pygame.transform.scale(self.background, (self.bg_width,self.bg_height)).convert_alpha()
        self.border_color = (255, 0, 0)
        self.computer = Box(self.railway_number, self.border_color, self.bg_height/2, self.bg_height/2).getRect()

        # Etat du train 
        self.train_is_prepared = False
        
        self.font = pygame.font.Font("assets/font.ttf", 50)
        
        # define rect for collision detect
        self.rect = self.railway

        
    def hasTrain(self) -> bool:
        '''
        Savoir si un train est présent sur la voie\n
        parametres :\n
                    - self 
        Retourne :\n 
                    - res (bool) : true si un train est présent, false sinon
        '''
        res = False
        if self.train != None:
            res = True
        return res

    def getTrainIsPrepared(self):
        return self.train_is_prepared

    def setTrainIsPrepared(self, train_is_prepared):
        self.train_is_prepared = train_is_prepared

    def removeTrain(self) -> None:
        '''
        Suppression du train présent sur la voie

        '''
        self.train = None
        self.border_color = (255, 0, 0)
    
    def addTrain(self, train) -> None:
        '''
        Ajouter un train à la voie\n
        Paramètres :\n
                    - train (Generic_Train) : Train
        '''
        self.train = train
        self.border_color = (255,165,0)

    def getRailwayNumber(self) -> int:
        '''
        Accesseur du numéro de voie \n
        Retourne :\n 
                    - self.railway_number (int) : Numéro de voie
        '''
        return self.railway_number

    def setTrain(self, train) -> None:
        '''
        Modificateur du numéro de voie\n
        parametres :\n
                    - self
                    - train (Train) : Nouveau train
        '''
        self.train = train

    def getRectX(self) -> int:
        '''
        Accesseur de la coordonné X de la voie\n
        Retourne :\n
                    - self.rectX (int) : coordonné x (horizontal)
        '''
        return self.rectX

    def getRectY(self) -> int:
        '''
        Accesseur de la coordonné Y de la voie\n
        Retourne :\n
                    - self.rectX (int) : coordonné y (vertical)
        '''
        return self.rectY

    def getRectWidth(self) -> int:
        '''
        Accesseur de la largeur de la voie\n
        Retourne :\n
                    - self.rectWidth (int) : largeur de la voie
        '''
        return self.rectWidth

    def getRectHeight(self) -> int:
        '''
        Accesseur de la hauteur de la voie\n
        Retourne :\n
                    - self.rectWidth (int) : hauteur de la voie
        '''
        return self.rectHeight

    def getComputer(self) -> Box:
        '''
        Accesseur de l'ordinateur (box) pour préparer le train sur la voie
        '''
        return self.computer

    def changeComputerWhenTrain(self) -> None:
        '''
        Changer l'ordinateur de préparation du train quand il y a un train
        '''
        self.computer = Box(self.railway_number, self.border_color, self.bg_height/2, self.bg_height/2).getRect()

    def changeComputerWhenNotTrain(self) -> None:     
        '''
        Changer l'ordinateur de préparation du train quand il n'y a pas de train
        '''   
        self.computer = Box(self.railway_number, self.border_color, self.bg_height/2, self.bg_height/2).getRect()
        self.train_is_prepared = False

    def changeComputerWhenTrainPrepared(self) -> None:
        '''
        Changer l'ordinateur de préparation du train quand le train a été préparé
        '''
        self.computer = Box(self.railway_number, (0,255,0), self.bg_height/2, self.bg_height/2).getRect()
        self.train_is_prepared = True

    def prepareTrain(self) -> None:
        '''
        Préparer le train
        '''
        output_string = "PREPARATION DU TRAIN"

        # Blit to the screen
        text = self.font.render(output_string, True, (255,255,255))
                

        self.display_surface.blit(text, [(self.display_surface.get_width() - text.get_width())/2, self.display_surface.get_height()/2])
        pygame.time.Clock().tick(1000)
        pygame.display.update()