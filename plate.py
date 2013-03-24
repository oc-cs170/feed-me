import pygame
import random

PLATE_WIDTH = 80
PLATE_HEIGHT = 16

class Plate(pygame.sprite.Sprite):
    """docstring for Plate"""
    plate = pygame.Surface((PLATE_WIDTH, PLATE_HEIGHT))
    plate.fill((169, 169, 169), (2, 2, PLATE_WIDTH - 4, PLATE_HEIGHT - 4))
    def __init__(self, x = 0, y = 0):
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = self.plate.convert_alpha()
        self.rect = self.image.get_rect(midtop=(x, y))

