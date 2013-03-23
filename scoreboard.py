import pygame


HEIGHT = 62
FONT_SIZE = 18
BG = (218, 218, 218)
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
        text = ''.join([self.prefix, str(self.text), self.suffix])
        self.image = self.font.render(text, True, FG, BG)
        self.rect = self.image.get_rect(topleft=self.location)


class ScoreBoard(pygame.sprite.Group):
    """A Scoreboard class that is aware of pygame.

    Keep track of score and lives remaining for 1 or 2 players.
    Info is displayed in a screen width rectangle, located at the top
    or bottom of the screen.

    Format: (1 player)
    [Level 001                                           O O O   Score: 000001]

    Format: (2 players)
    [Player 1: 000001 Level 001   O O O     O O O   Player 2: 000001 Level 001]
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
        self.player1 = 0
        self.level1 = 0
        self.lives1 = 'X  X  X'


        if num_players == 1:
            self.items.add(SBTextItem(font, self.level1, location=(3, 0), prefix='Level: '),
                           SBTextItem(font, self.lives1, location=(335, 0), prefix='Lives: '),
                           SBTextItem(font, self.player1, location=(710, 42), prefix='Score: '))

    def update(self):
        self.items.update()
        pygame.sprite.Group.update(self)

    def draw(self, surface):
        self.items.draw(self.scoreboard.image)
        pygame.sprite.Group.draw(self, surface)

        