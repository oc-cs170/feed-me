import pygame

class Hero(pygame.sprite.Sprite):
    """docstring for Hero"""
    def __init__(self, screen, png='PlanetCute PNG/Character Cat Girl.png'):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.screen.get_width() / 2, self.screen.get_height()))
        

