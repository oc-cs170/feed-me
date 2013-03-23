import pygame

class Scoreboard(pygame.sprite.Sprite):
	"""docstring for Scoreboard"""
	def __init__(self, arg):
		pygame.sprite.Sprite.__init__(self)
		self.arg = arg
