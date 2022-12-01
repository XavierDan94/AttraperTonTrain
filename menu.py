import pygame, sys
from settings import *
from classes.button import *
from level import *

class Menu:
    def __init__(self, game) -> None:
        '''
        Constructeur de la classe Menu\n
        Paramètres:\n
                    - game (Game) : Instance de la classe Game (le jeu)
        '''
        self.game = game
        self.font = pygame.font.SysFont('Arial', 25)

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    # Menu Screen
    def main_menu(self) -> None:
        '''
        Ecran principal (menu)
        '''
        while True:
            # Main menu FULLSCREEN
            w, h = pygame.display.get_surface().get_size()

            # On applique le background du menu sur l'intégralité de la taille de la fenêtre du jeu
            self.game.background = pygame.transform.scale(self.game.background, (w, h))
            self.game.screen.blit(self.game.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # Titre de la fenêtre 
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(w/2, 300))

            # Chargement des boutons présents
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(w/2, 600), 
                                text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(w/2, 800), 
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            CREDITS_BUTTON = Button(image=pygame.image.load("assets/Credits Rect.png"), pos=(w/2, 1000), 
                                text_input="CREDITS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(w/2, 1200), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.game.screen.blit(MENU_TEXT, MENU_RECT)
            
            # Pour chaque bouton, on modification son hover
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.game.screen)
            
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
                    if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.credits()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # Play Screen
    def play(self) -> None:
        '''
        Lancement du jeu (lorsque l'on clique sur "play" dans le menu)
        '''
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.game.screen.fill("green")

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.game.screen)

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

            dt = self.game.clock.tick() / 1000
            self.game.level.run(dt)
            
            # Affichage du score lorsque le temps restant est à 0
            if self.game.level.overlay.timer.getTotalSeconds() >= TIME_LEVEL:
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
            self.game.screen.blit(self.game.background, (0, 0))

            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Chargement des boutons pour passer en plein écran ou revenir en arrière
            OPTIONS_FULLSCREEN = Button(image=None, pos=(w/2, 200), 
                                text_input="FULLSCREEN", font=self.get_font(75), base_color="#d7fcd4", hovering_color="white")

            OPTIONS_BACK = Button(image=None, pos=(w/2, 550), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            # On modifie le hover (couleur au survol de la souris) des boutons
            OPTIONS_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_FULLSCREEN.update(self.game.screen)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.game.screen)

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
                        self.game.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                        w, h = pygame.display.get_surface().get_size()
                        
                        self.game.background = pygame.transform.scale(self.game.background, (w, h))
                        self.game.screen.blit(self.game.background, (0, 0))

            pygame.display.update()
    
    # Credits Screen
    def credits(self) -> None:
        '''
        Affichage de l'écran credits du menu
        '''
        while True:
            w, h = pygame.display.get_surface().get_size()
            # On applique le background du menu sur l'intégralité de la taille de la fenêtre du jeu
            self.game.screen.blit(self.game.background, (0, 0))

            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Chargement des boutons pour passer en plein écran ou revenir en arrière

            OPTIONS_BACK = Button(image=None, pos=(w/2, 950), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.game.screen)

            title_color = (178,124,69)
            text_color = (255,255,255)
            title1 = self.get_font(120).render('CREATED BY', True, title_color)
            name1 = self.get_font(60).render('CARDOSO Samuel', True, text_color)
            name2 = self.get_font(60).render('DAN Xavier', True, text_color)

            self.game.screen.blit(title1, ((w-title1.get_width())/2, 450))
            self.game.screen.blit(name1, ((w-name1.get_width())/2, 650))
            self.game.screen.blit(name2, ((w-name2.get_width())/2, 750))

            # Gestion des événements (quitter le jeu, retour en arrière, passage en mode plein écran)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
            

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
            self.game.background = pygame.transform.scale(self.game.background, (w, h))
            self.game.screen.blit(self.game.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # Titre de la fenêtre 
            MENU_TEXT = self.get_font(100).render("YOUR IS SCORE : "+str(self.game.level.score), True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(w/2, 300))

            # Chargement des boutons présents
            RETRY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(w/2, 500), 
                                text_input="RETRY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(w/2, 800), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.game.screen.blit(MENU_TEXT, MENU_RECT)
            
            # Pour chaque bouton, on modifie son hover
            for button in [RETRY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.game.screen)
            
            # Gestion des événements relatifs au menu
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETRY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.game.level = Level()
                        self.play()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()