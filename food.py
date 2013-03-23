import pygame

class Food(pygame.sprite.Sprite):
    """docstring for Food"""
    "foods is the list of food images"
    food_sprites = pygame.image.load("food_sprites.png")
    foods = [None] * 6
    for i in range(0, 6):
        foods[i] = food_sprites.subsurface(pygame.Rect((i * 64, 0), (64, 48)))

    worth = [50, 30, 30, 20, 20, 10]

    def __init__(self, food, plate):
        """food argument should be an integer specifying the type of food:
                0: kiwi (worth 50 points)
                1: fires (worth 30 points)
                2: watermelon (worth 30 points)
                3: popcorn (worth 20 points)
                4: lemon (worth 20 points)
                5: eggplant (worth 10 points)

            plate argument is the plate the food will be on top of"""
        pygame.sprite.Sprite.__init__(self)
        self.image = self.foods[food]
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = plate.rect.midtop
        self.points = self.worth[food]
