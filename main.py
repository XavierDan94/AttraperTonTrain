import pygame
from level import Level
from classes.timer import *
from menu import *
class Game: 
    def __init__(self) -> None:
        '''
        Constructeur de la classe Game\n
        '''
        pygame.init()

        # Taille de l'écran du jeu par défaut
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        # Titre de la fenêtre
        pygame.display.set_caption("SNCF Train Game")

        # Initialisation du temps, et du niveau
        self.clock = pygame.time.Clock()
        self.level = Level()

        #self.background = pygame.image.load("assets/Background.png")
        self.background = pygame.image.load("assets/background_gare.jpg")

        # Initialisation du Timer
        self.timer = Timer(pygame.font.Font("assets/font.ttf", 25), self.screen)
        self.start_time = pygame.time.get_ticks()

        # Initialisation du Menu
        self.menu = Menu(self)

if __name__ == '__main__':
	game = Game()
	game.menu.main_menu()