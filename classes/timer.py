import pygame
from settings import *
class Timer:
    def __init__(self, font, screen) -> None:
        '''
        Constructeur de la classe Timer\n
        Paramètres :\n
                    - font (Font) : Font du texte d'affichage du Timer
                    - screen : Ecran 
        '''
        self.font = font
        self.screen = screen

        self.text_color = pygame.Color(255,255,255)
        self.clockGame = pygame.time.Clock()

        self.frame_count = 1
        self.frame_rate = 1000
        self.frame_rate_value = 40
        self.start_time = TIME_LEVEL
        self.total_seconds = 1

    def getTotalSeconds(self) -> int:
        '''
        Accesseur du temps total en secondes écoulés depuis l'instanciation de l'objet timer\n
        Retourne :\n
                    self.total_seconds (int) : Temps écoulés en secondes
        '''
        return self.total_seconds

    def getStartTime(self) -> int:
        '''
        Accesseur du temps restant\n
        Retourne:\n
                    - self.start_time (int) : Temps restant
        '''
        return self.start_time

    def setup(self) -> None:
        '''
        Lancement du timer
        '''
        
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = self.frame_count // self.frame_rate_value
        self.total_seconds = self.frame_count / self.frame_rate_value
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
        
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        text = self.font.render(output_string, True, self.text_color)
        self.screen.blit(text, [20, 20])
        
        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = self.start_time - (self.frame_count // self.frame_rate_value)
        if total_seconds < 0:
            total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
        
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        
        # Blit to the screen
        text = self.font.render(output_string, True, self.text_color)
        
        self.screen.blit(text, [20, 60])
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        self.frame_count += 1
        
        # Limit frames per second
        self.clockGame.tick(self.frame_rate)
        pygame.display.update()
