import pygame, sys
from classes.button import Button
from settings import *
from level import Level

class Game: 
    def __init__(self) -> None:
        
        pygame.init()

        #self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        pygame.display.set_caption("SNCF Train Game")
        self.clock = pygame.time.Clock()
        self.level = Level()

        self.background = pygame.image.load("assets/Background.png")

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    # Play Screen
    def play(self):
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
            pygame.display.update()

    # Options Screen
    def options(self):
        while True:
            w, h = pygame.display.get_surface().get_size()
            self.screen.blit(self.background, (0, 0))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()


            OPTIONS_FULLSCREEN = Button(image=None, pos=(w/2, 200), 
                                text_input="FULLSCREEN", font=self.get_font(75), base_color="#d7fcd4", hovering_color="white")

            OPTIONS_BACK = Button(image=None, pos=(w/2, 550), 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            OPTIONS_FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_FULLSCREEN.update(self.screen)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
            
                    elif OPTIONS_FULLSCREEN.checkForInput(OPTIONS_MOUSE_POS):
                        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                        w, h = pygame.display.get_surface().get_size()
                        
                        self.background = pygame.transform.scale(self.background, (w, h))
                        self.screen.blit(self.background, (0, 0))



            pygame.display.update()

    # Menu Screen
    def main_menu(self):
        while True:
            # Main menu FULLSCREEN
            w, h = pygame.display.get_surface().get_size()
            self.background = pygame.transform.scale(self.background, (w, h))

            self.screen.blit(self.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(w/2, 300))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(w/2, 500), 
                                text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(w/2, 650), 
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(w/2, 800), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
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