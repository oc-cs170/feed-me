import pygame

class Food(pygame.sprite.Sprite):
    """docstring for Food"""
    def __init__(self, arg):
        pygame.sprite.Sprite.__init__(self)
        self.arg = arg
