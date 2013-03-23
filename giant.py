import pygame

class Giant(object):
	"""docstring for Giant"""
	def __init__(self, background, png='Planetcute PNG/Enemy Bug.png'):
		self.background = background
		#Initialize Sprite
		pygame.sprite.Sprite.__init__(self)
	
		# Image place holder for Giant
		self.image = pygame.image.load(png).convert_alpha()
		self.rect = self.image.get_rect(topleft=(20, 20))
