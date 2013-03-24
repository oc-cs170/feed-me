import pygame

WINDOW_TITLE = 'Feed-Me'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
BORDER = 20


class SplashScreen():
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = self.screen.copy()
        pygame.display.set_caption(WINDOW_TITLE)

        self.title = 'FEED-ME!'
        self.bg = (135, 206, 250)
        # self.bg = (216, 216, 255)
        self.fg = (65, 105, 255)
        self.clock = pygame.time.Clock()

    def draw(self):
        # Build the splash screen
        self.splash = self.screen.copy()
        self.splash.fill((65, 105, 225))
        self.inner = (BORDER, BORDER, self.screen_width - 2 * BORDER, self.screen_height - 2 * BORDER)
        self.splash.fill(self.bg, self.inner)

        # hide_screen = pygame.time.get_ticks()
        font1 = pygame.font.SysFont('Arial', 80, bold=True)
        antialias = True
        width, height = font1.size(self.title)
        x = ((self.screen_width - width) / 2)
        y = 2 * BORDER

        for i in range(len(self.title)):
            self.clock.tick(4)
            self.screen.blit(self.splash, (0, 0))
            surf = font1.render(self.title[0:i + 1], antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            pygame.display.flip()

        # clock.tick(1)
        font2 = pygame.font.SysFont('Arial', 24, bold=True)
        x += 35
        y = y + height + BORDER
        lines = ['To move cat girl use <-, ->',
                 'To jump use Space Bar',
                 ' ',
                 'Collect the various food items to',
                 'score points:',
                 '      kiwi (worth 50 points),',
                 '      fries (worth 30 points)',
                 '      watermelon (worth 30 points)',
                 '      popcorn (worth 20 points)',
                 '      lemon (worth 20 points)',
                 '      eggplant (worth 10 points)',
                 ' ',
                 ' ',
                 'Press enter to start...',
                 ' ',
                 'Press q or escape to quite.']
        for line in lines:
            self.clock.tick(10)
            surf = font2.render(line, antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            y += surf.get_height()
            pygame.display.flip()

        waiting = True
        while waiting:           # Pause loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    if event.key == pygame.K_q:
                        self.game_over = True
                    break

    def game_over(self):
        # Build the splash screen
        self.title = 'GAME OVER'
        self.splash = self.screen.copy()
        self.splash.fill((0, 0, 0))
        self.inner = (BORDER, BORDER, self.screen_width - 2 * BORDER, self.screen_height - 2 * BORDER)
        self.splash.fill(self.bg, self.inner)

   # hide_screen = pygame.time.get_ticks()
        font1 = pygame.font.SysFont('Arial', 80, bold=True)
        antialias = True
        width, height = font1.size(self.title)
        x = ((self.screen_width - width) / 2) + 7
        y = 2 * BORDER

        for i in range(len(self.title)):
            self.clock.tick(4)
            self.screen.blit(self.splash, (0, 0))
            surf = font1.render(self.title[0:i + 1], antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            pygame.display.flip()

        # clock.tick(1)
        font2 = pygame.font.SysFont('Arial', 24, bold=True)
        x *= 2
        y = y + height + BORDER
        lines = ['Would you like to',
                 'play again?',
                 ' ',
                 ' ',
                 ' ',
                 'Press y for Yes...',
                 ' ',
                 'Press n for No...']
        for line in lines:
            self.clock.tick(10)
            surf = font2.render(line, antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            y += surf.get_height()
            pygame.display.flip()

        waiting = True
        while waiting:           # Pause loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting = False
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE or event.key == pygame.K_n:
                        self.game_over = True
                    break


    def intro_splash(self):
        button_press = False
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
            self.screen.fill(pygame.Color('skyblue'))
            font = pygame.font.SysFont(pygame.font.get_default_font(), 60, bold = False)
            
            lines = ["Feed-Me",
                     "",
                     "",
                     "Move: Right and Left Arrows",
                     "Space: Jump",
                     "",
                    "kiwi (worth 50 points)",
                    "fires (worth 30 points)",
                    "watermelon (worth 30 points)",
                    "popcorn (worth 20 points)",
                    "lemon (worth 20 points)",
                    "eggplant (worth 10 points)"
                    ]

            for i in range(len(lines)):
                x = lines[i]
                label = font.render(x, 1, (0,0,0))
                width = label.get_width()
                self.screen.blit(label, (self.screen.get_width() /2 - width /2, i*50))


            pygame.display.flip()
