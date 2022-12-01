import pygame, sys
from classes.button import Button
from settings import *
from level import Level
from classes.timer import *
class Game: 
    def __init__(self) -> None:
        '''
        Constructeur de la classe Game\n
        parametres :\n
                    - self
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
        self.timer = Timer(self.get_font(25), self.screen)
        self.start_time = pygame.time.get_ticks()

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    # Play Screen
    def play(self) -> None:
        '''
        Lancement du jeu (lorsque l'on clique sur "play" dans le menu)
        '''
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.screen.fill("green")

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
                
                # if key escape is pressed, open main menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            
            # Affichage du score lorsque le temps restant est à 0
            if self.level.overlay.timer.getTotalSeconds() >= TIME_LEVEL:
                # Score
                self.end_level_menu()

            pygame.display.update()


    # Options Screen
    def options(self) -> None:
        '''
        Affichage de l'écran d'options du menu
        '''
        while True:
            w, h = pygame.display.get_surface().get_size()
            # On applique le background du menu sur l'intégralité de la taille de la fenêtre du jeu
            self.screen.blit(self.background, (0, 0))

            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Chargement des boutons pour passer en plein écran ou revenir en arrière
            OPTIONS_FULLSCREEN = Button(image=None, pos=(w/2, 200), 
                                text_input="FULLSCREEN", font=self.get_font(75), base_color="#d7fcd4", hovering_color="white")

            OPTIONS_BACK = Button(image=None, pos=(w/2, 550), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            # On modifie le hover (couleur au survol de la souris) des boutons
            OPTIONS_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_FULLSCREEN.update(self.screen)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)

            # Gestion des événements (quitter le jeu, retour en arrière, passage en mode plein écran)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
            
                    # adaptation du background du menu en cas de passage en mode plein écran
                    elif OPTIONS_FULLSCREEN.checkForInput(OPTIONS_MOUSE_POS):
                        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                        w, h = pygame.display.get_surface().get_size()
                        
                        self.background = pygame.transform.scale(self.background, (w, h))
                        self.screen.blit(self.background, (0, 0))

            pygame.display.update()

    # Score Screen
    def end_level_menu(self) -> None:
        '''
        Ecran de score
        '''
        while True:
            # Score Screen FULLSCREEN
            w, h = pygame.display.get_surface().get_size()

            # On applique le background du menu sur l'intégralité de la taille de la fenêtre du jeu
            self.background = pygame.transform.scale(self.background, (w, h))
            self.screen.blit(self.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # Titre de la fenêtre 
            MENU_TEXT = self.get_font(100).render("YOUR IS SCORE : "+str(self.level.score), True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(w/2, 300))

            # Chargement des boutons présents
            RETRY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(w/2, 500), 
                                text_input="RETRY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(w/2, 800), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)
            
            # Pour chaque bouton, on modifie son hover
            for button in [RETRY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
            # Gestion des événements relatifs au menu
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETRY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.level = Level()
                        self.play()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # Menu Screen
    def main_menu(self) -> None:
        '''
        Ecran principal (menu)
        '''
        while True:
            # Main menu FULLSCREEN
            w, h = pygame.display.get_surface().get_size()

            # On applique le background du menu sur l'intégralité de la taille de la fenêtre du jeu
            self.background = pygame.transform.scale(self.background, (w, h))
            self.screen.blit(self.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # Titre de la fenêtre 
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(w/2, 300))

            # Chargement des boutons présents
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(w/2, 500), 
                                text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(w/2, 650), 
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(w/2, 800), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)
            
            # Pour chaque bouton, on modification son hover
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
            # Gestion des événements relatifs au menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.main_menu()