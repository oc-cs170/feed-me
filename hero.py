import pygame

class Hero(pygame.sprite.Sprite):
    """docstring for Hero"""
    def __init__(self, screen, png='PlanetCute PNG/Character Cat Girl.png'):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.screen.get_width() / 2, self.screen.get_height()))
        self.plate = None

        self.xv = 0
        self.yv = 0
        self.jump = False

    def update(self):
        self.yv += .8
        if self.plate:
            self.yv = 5
            if self.jump == True:
                self.yv = -15
        else:
            self.jump = False

        self.rect.move_ip(self.xv, self.yv)
        self.rect.right = min(self.rect.right,self.screen.get_width())
        self.rect.left = max(self.rect.left, 0)


