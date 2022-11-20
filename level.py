import pygame
from settings import *
from classes.player import Player
from classes.overlay import Overlay
from classes.railway import *
class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

        # railways
        self.railways = [ Railway(1, None, 500),      
        ]


    def setup(self):
        self.player = Player((640,360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')

        # Draw railway in first, because Player have to priority order 
        for railway in self.railways:
            railway.draw()
        
        
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        #self.overlay.display()