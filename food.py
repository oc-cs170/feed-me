import pygame

class Food(pygame.sprite.Sprite):
    """docstring for Food"""
    "foods is the list of food images"
    foods = []
    foods.append(pygame.image.load("PlanetCute PNG/Gem Blue.png").convert_alpha)
    foods.append(pygame.image.load("PlanetCute PNG/Gem Green.png").convert_alpha)
    foods.append(pygame.image.load("PlanetCute PNG/Gem Orange.png").convert_alpha)
    foods.append(pygame.image.load("PlanetCute PNG/Heart.png").convert_alpha)
    foods.append(pygame.image.load("PlanetCute PNG/Key.png").convert_alpha)
    foods.append(pygame.image.load("PlanetCute PNG/Rock.png").convert_alpha)
    worth = [10, 20, 20, 30, 30, 50]

    def __init__(self, food, plate):
        """food argument should be an integer specifying the type of food:
                0: bread (worth 10 points)
                1: tomato (worth 20 points)
                2: lettuce (worth 20 points)
                3: ham (worth 30 points)
                4: turkey (worth 30 points)
                5: chicken (worth 50 points)

            plate argument is the plate the food will be on top of"""
        pygame.sprite.Sprite.__init__(self)
        self.image = self.foods[food]
        self.rect = self.image.get_rect()
        self.rect.midbottom = plate.rect.midtop
        self.points = self.worth[food]
