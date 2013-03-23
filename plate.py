import pygame

PLATE_WIDTH = 80
PLATE_HEIGHT = 16

class Plate(pygame.sprite.Sprite):
    """docstring for Plate"""
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.image = pygame.Surface((PLATE_WIDTH, PLATE_HEIGHT))
        self.image.fill((169, 169, 169), (2, 2, PLATE_WIDTH - 4, PLATE_HEIGHT - 4))

        plate_x = self.screen.get_width() / 2
        plate_y = self.screen.get_height() - (2 * PLATE_HEIGHT)
        self.rect = self.image.get_rect(midtop=(plate_x, plate_y))

