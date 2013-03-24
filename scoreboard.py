import pygame

HEIGHT = 48
FONT_SIZE = 18
BG = (211, 211, 211)
FG = (0, 0, 0)

class SBTextItem(pygame.sprite.Sprite):
    def __init__(self, font, text, location=(0, 0), prefix='', suffix=''):
        pygame.sprite.Sprite.__init__(self)

        self.font = font
        self.text = text
        self.location = location
        self.prefix = prefix
        self.suffix = suffix
        self.update()

    def update(self):
        message = ''.join([self.prefix, str(self.text), self.suffix])
        self.image = self.font.render(message, True, FG, BG)
        self.rect = self.image.get_rect(topleft=self.location)


class SBImageItem(pygame.sprite.Sprite):
    def __init__(self, font, image, location=(0,0), prefix=''):
        pygame.sprite.Sprite.__init__(self)

        self.font= font
        self.location = location
        self.prefix = prefix
        self.image = image
        self.rect = image.get_rect(topleft=self.location)

        # # Hero chareacter
        # self.image = pygame.image.load('PlanetCute PNG/Character Cat Girl.png').convert_alpha()
        # self.rect = self.image.get_rect(topleft=(self.location))


        self.update()

    def update(self):
        pass
    #     self.image = pygame.Surface((80, 16)).convert_alpha()
    #     self.image.fill((169, 169, 169), (2, 2, 76, 12))
    #     self.health = self.image.get_rect(topleft=(0, 0))
        



class ScoreBoard(pygame.sprite.Group):
    """A Scoreboard class that is aware of pygame.

    Keep track of score and lives remaining for 1 or 2 players.
    Info is displayed in a screen width rectangle, located at the top
    or bottom of the screen.

    Format: (1 player)
    [Level 001                                           O O O   Score: 000001]
    """
    def __init__(self, screen, icon=None, num_players=1, top=True):
        """Create a Scoreboard object.
        Args:
            screen: a surface, where the scoreboard will be displayed
            icon: a surface, an image of the player, used to display lives
                  if none is given, don't display lives
            num_players: an int, determine the display style
            top: a boolean, display scoreboard at top or bottom of screen
        """
        pygame.sprite.Group.__init__(self)
        self.image = None
        self.screen = screen
        self.scoreboard = pygame.sprite.Sprite()
        self.scoreboard.image = pygame.Surface((screen.get_width(), HEIGHT))
        self.scoreboard.image.fill(BG)
        y = 0 if top else screen.get_height() - HEIGHT
        self.scoreboard.rect = self.scoreboard.image.get_rect(topleft=(0, 0))
        self.add(self.scoreboard)

        font = pygame.font.SysFont('Arial', FONT_SIZE, True)

        self.items = pygame.sprite.Group()

        # Scoreboard values
        self.level1 = 1
        self.lives1 = 'X  X  X'
        
        self.health = pygame.Surface((100, 16))
        pygame.draw.rect(self.health, (255, 255, 255), self.health.get_rect())
        
        image = pygame.image.load('PlanetCute PNG/Character Cat Girl.png').convert_alpha()
        self.hero = pygame.transform.scale(image, (40, 65))


        self.player1 = 0

        if num_players == 1:
            self.items.add(SBTextItem(font, self.level1, location=(3, 0), prefix='Level: '),
                           SBTextItem(font, 'Lives: ', location=(280, 12)),
                           SBTextItem(font, self.player1, location=(700, 24), prefix='Score: '),
                           SBTextItem(font, 'Goal: ', location=(640, 3)),
                           SBImageItem(font, self.health, location=(690, 5), prefix='Goal: '),
                           SBImageItem(font, self.hero, location=(335, -15)),
                           SBImageItem(font, self.hero, location=(365, -15)),
                           SBImageItem(font, self.hero, location=(395, -15)))

    def update(self):
        self.items.update()
        pygame.sprite.Group.update(self)

    def draw(self, surface):
        self.items.draw(self.scoreboard.image)
        pygame.sprite.Group.draw(self, surface)
