import pygame
from settings import *

class Overlay:
	def __init__(self,player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports 
		overlay_path = 'graphics/overlay/'
		#self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
		self.money_surf = pygame.image.load(f'{overlay_path}money.png').convert_alpha() 

	def display(self):

		# money
		money_rect = self.money_surf.get_rect(midbottom = OVERLAY_POSITIONS['money'])
		self.display_surface.blit(self.money_surf,money_rect)
