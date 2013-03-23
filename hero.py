import pygame

class Hero(pygame.sprite.Sprite):
    """docstring for Hero"""
    def __init__(self, arg):
        pygame.sprite.Sprite.__init__(self)
        self.arg = arg
