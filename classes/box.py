import pygame
class Box(pygame.sprite.Sprite):
    def __init__(self, railwayNumber , borderColor, width, height) -> None:
        '''
        Constructeur de la classe Box\n
        Paramètres :\n
                    - railwayNumber (int) : Numéro de la voie reliée à l ordinateur de préparation de train
                    - borderColor (Tuple de 3) : Couleur de la bordure sous la forme rgb (red,green,blue)
                    - width (int) : Largeur de la Box
                    - height (int) : Hauteur de la Box
        '''
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Objet qui permet de préparer le train 
        self.image = pygame.Surface((width, height))
        
        
        # Couleur du background, ajout du texte et configuration de la font
        self.image.fill((255, 255, 255))
        self.text = str(railwayNumber)
        self.font = pygame.font.SysFont("Arial", 50)

        # Rendu du texte
        self.textSurf = self.font.render(self.text, 1, (0,0,0))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

        self.rectangle = self.image
        
        self.border_color = borderColor
        self.image = pygame.draw.rect(self.image, self.border_color, self.image.get_rect(), 6, 3) # image.get_rect() not rect!


    def getRect(self) -> pygame.Rect:
        '''
        Accesseur du rectangle où est placé le préparateur
        Retourne:\n
                    - self.rectangle (pygame.Rect) : Rectangle du préparateur de train
        '''
        return self.rectangle