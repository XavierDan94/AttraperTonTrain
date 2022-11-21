import pygame
from settings import *
from classes.player import Player
from classes.overlay import Overlay
from classes.sprites import Generic, Generic_Railway
from classes.railway import *
from pytmx.util_pygame import load_pygame
from support import *

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)


    def setup(self):
        # railways
        self.railways = [ 
            Railway(1, None, 0), 
            Railway(2, None, 300),
            Railway(3, None, 600),
            Railway(4, None, 900),
            Railway(5, None, 1200),
            Railway(6, None, 1500)
        ]

        # Add railways in self.all_sprites
        for obj in self.railways:
            Generic_Railway((obj.rectX, obj.rectY), obj.background, self.all_sprites, "name")

        # Add player and ground 
        self.player = Player((640,360), self.all_sprites)
        Generic(
            pos = (0,0),
            surf = pygame.transform.scale(pygame.image.load('graphics/platform/main-platform.png'), (4000,4000)).convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])

    def run(self,dt):
        # level background
        self.display_surface.fill('black')
        
        # sprites draw and update
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        #self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        '''
        Constructeur de la classe CameraGroup\n
        parametres :\n 
                    - self
        '''
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        '''
        Affichage personnalisée du joueur pour que la caméra le suit\n
        parametres :\n
                    - self
                    - player (Player) : Joueur
        '''
        # Empêche le joueur de se déplacer dans une direction d'un axe selon une position x ou y donnée
        if player.rect.centerx - SCREEN_WIDTH / 2 > 500:
            self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        if player.rect.centery - SCREEN_HEIGHT / 2 > 0:
            self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)