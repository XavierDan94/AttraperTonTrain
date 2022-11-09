from xmlrpc.client import Boolean
import pygame

class Railway:

    def __init__(self, railway_number, train, rectY):
        self.railway_number = railway_number # Numéro de la voie
        self.train = train

        self.rectX = 600
        self.rectY = rectY
        self.rectWidth = 600
        self.rectHeight = 100
        self.display_surface = pygame.display.get_surface() 
        self.railway = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)
        self.background = pygame.image.load("graphics/platform/platform.png")
        self.background = pygame.transform.scale(self.background, (2500,300))
        self.BGCOLOR = (3, 115, 46)

    def hasTrain(self) -> Boolean:
        res = False
        if self.train != None:
            res = True
        return res

    def getRailwayNumber(self) -> int:
        return self.railway_number

    def setTrain(self, train) -> None:
        self.train = train


    def draw(self) -> None:
        self.display_surface.blit(self.background,self.railway)

        #pygame.draw.rect(s,self.BGCOLOR, self.railway)    
