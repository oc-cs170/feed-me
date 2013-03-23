import pygame
import random

PLATE_WIDTH = 80
PLATE_HEIGHT = 16

class Plate(pygame.sprite.Sprite):
    """docstring for Plate"""
    def __init__(self, background, x = 0, y = 0):
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.background = background

        self.image = pygame.Surface((PLATE_WIDTH, PLATE_HEIGHT))
        self.image.fill((169, 169, 169), (2, 2, PLATE_WIDTH - 4, PLATE_HEIGHT - 4))
        self.rect = self.image.get_rect(topleft=(x, y))
