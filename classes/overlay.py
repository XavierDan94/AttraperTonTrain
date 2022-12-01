import pygame
from settings import *
from classes.timer import *
class Overlay:
    def __init__(self, score):
        '''
        Constructeur de la classe Overlay\n
        Paramètres :\n
                    - score (int) : Score du joueur pour le niveau en cours
        '''
        # general setup
        self.display_surface = pygame.display.get_surface()

        self.font = pygame.font.Font("assets/font.ttf", 25)
        self.timer = Timer(self.font, self.display_surface)

        # rectangle de l'overlay et sa couleur
        self.overlay = pygame.Rect(0, 0, 4500, 100)
        self.color = OVERLAY["background_color"]

        self.clockGame = pygame.time.Clock()
        self.score = score
        self.screen_width = self.display_surface.get_width()
        

    def display(self):
        '''
        Afficher l'overlay\n
        '''
        pygame.draw.rect(self.display_surface, self.color, self.overlay)

        # Timer
        self.timer.setup()
        
        # Score
        self.display_score()

        pygame.display.update()

    def display_score(self) -> None:
        '''
        Affichage du score du joueur pour le niveau actuel sur l'overlay
        '''
        # Use python string formatting 
        output_string = "SCORE: "+str(self.score)

        # Blit to the screen
        text = self.font.render(output_string, True, (255,255,255))
        
        self.display_surface.blit(text, [self.screen_width - (text.get_width()+20), 40])
        self.clockGame.tick(1000)
        pygame.display.update()
