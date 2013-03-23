import pygame

class Giant(pygame.sprite.Sprite):
	"""docstring for Giant"""
	def __init__(self, background, png='PlanetCute PNG/Enemy Bug.png'):
		self.background = background
		#Initialize Sprite
		pygame.sprite.Sprite.__init__(self)
	
		# Image place holder for Giant
		self.image = pygame.image.load(png).convert_alpha()
		self.rect = self.image.get_rect(topleft=(35, 20))
