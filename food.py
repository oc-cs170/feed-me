import pygame

class Food(pygame.sprite.Sprite):
    """docstring for Food"""
    "foods is the list of food images"
    foods = []
    foods.append(pygame.image.load("PlanetCute PNG/Gem Blue.png"))
    foods.append(pygame.image.load("PlanetCute PNG/Gem Green.png"))
    foods.append(pygame.image.load("PlanetCute PNG/Gem Orange.png"))
    foods.append(pygame.image.load("PlanetCute PNG/Heart.png"))
    foods.append(pygame.image.load("PlanetCute PNG/Key.png"))
    foods.append(pygame.image.load("PlanetCute PNG/Rock.png"))
    worth = [50, 30, 30, 20, 20, 10]

    def __init__(self, food, plate):
        """food argument should be an integer specifying the type of food:
                0: chicken (worth 50 points)
                1: turkey (worth 30 points)
                2: ham (worth 30 points)
                3: lettuce (worth 20 points)
                4: tomato (worth 20 points)
                5: bread (worth 10 points)

            plate argument is the plate the food will be on top of"""
        pygame.sprite.Sprite.__init__(self)
        self.image = self.foods[food]
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = plate.rect.midtop
        self.points = self.worth[food]
