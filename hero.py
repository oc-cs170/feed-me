import pygame

class Hero(pygame.sprite.Sprite):
    """docstring for Hero"""
    xv = 0
    yv = 0
    def __init__(self, screen, png='PlanetCute PNG/Character Cat Girl.png'):
        self.screen_width, self.screen_height = screen.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.screen_width / 2, self.screen_height))
        self.plate = None
        self.jump = False
    def update(self):
        self.yv += 1

        if self.plate:
            for plate in self.plate:
                if self.rect.bottom - 32 <= plate.rect.bottom and self.yv >= 0:
                    self.rect.bottom = plate.rect.top + 35
                    self.yv = 0
                    if self.jump == True:
                        self.yv = -15
                        self.plate = None

        else:
            self.jump = False

        self.yv = min(self.yv, 15)
        self.rect.move_ip(self.xv, self.yv)
        self.rect.centerx = max(0, min(self.rect.centerx,self.screen_width))
