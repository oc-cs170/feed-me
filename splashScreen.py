import pygame

WINDOW_TITLE = 'Feed-Me'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
BORDER = 20


class SplashScreen():
    def __init__(self):
        pygame.mixer.init(11025,-16,2,4096)    
        pygame.mixer.set_num_channels(3)
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

        self.bsound = pygame.mixer.Sound('sounds/bsound.ogg')
        self.die = pygame.mixer.Sound('sounds/die.ogg')
        self.elvlsound = pygame.mixer.Sound('sounds/small pin.wav')
        self.egamesound = pygame.mixer.Sound('sounds/small pin.wav')
        self.bsound.set_volume(.2)
        self.bsound.play()
        self.messages = [['YOU DIED', 'Please wait', 'to try again!', ' ', "Note: Don't fall below the screen!"],
                         ['YOU DIED', 'Goal meter was not met', ' ', 'Please wait', 'to try again!'],
                         ['CONGRATULATIONS', ' ', 'Please wait to move', 'onto next level!']]

       

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
        lines = ['To move cat girl use left or right',
                 'arrow keys',
                 ' ',
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
                 'Press enter to start...',
                 ' ',
                 'Press q or escape to quit.']
        for line in lines:
            self.clock.tick(10)
            surf = font2.render(line, antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            y += surf.get_height()
            pygame.display.flip()


        while True:           # Pause loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return False

    def message(self, message):
        # Build the splash screen

        self.bsound.stop()
        self.die.play(loops=0, maxtime=0, fade_ms= 0)
        self.die.set_volume(1.0)
        
        title = self.messages[message][0]
        self.splash = self.screen.copy()
        self.splash.fill((65, 105, 225))
        self.inner = (BORDER, BORDER, self.screen_width - 2 * BORDER, self.screen_height - 2 * BORDER)
        self.splash.fill(self.bg, self.inner)

        font1 = pygame.font.SysFont('Arial', 70, bold=True)
        antialias = True
        width, height = font1.size(title)
        x = ((self.screen_width - width) / 2)
        y = 2 * BORDER

        for i in range(len(title)):
            self.clock.tick(4)
            self.screen.blit(self.splash, (0, 0))
            surf = font1.render(title[0:i + 1], antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            pygame.display.flip()

        # clock.tick(1)
        font2 = pygame.font.SysFont('Arial', 24, bold=True)
        x += 35
        y = y + height + BORDER
        lines = self.messages[message][1:]

        for line in lines:
            self.clock.tick(10)
            surf = font2.render(line, antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
            y += surf.get_height()
            pygame.display.flip()

        pygame.display.flip()
        pygame.time.wait(4000)
        #restart music
        self.bsound.play()

    def game_over(self):
        # Build the splash screen
        
        self.bsound.stop()
        self.egamesound.play(loops=0, maxtime=7000, fade_ms= 0)
        self.egamesound.set_volume(1.0)

        title = 'GAME OVER'
        self.splash = self.screen.copy()
        self.splash.fill((65, 105, 225))
        self.inner = (BORDER, BORDER, self.screen_width - 2 * BORDER, self.screen_height - 2 * BORDER)
        self.splash.fill(self.bg, self.inner)

   # hide_screen = pygame.time.get_ticks()
        font1 = pygame.font.SysFont('Arial', 80, bold=True)
        antialias = True
        width, height = font1.size(title)
        x = ((self.screen_width - width) / 2) + 7
        y = 2 * BORDER

        for i in range(len(title)):
            self.clock.tick(4)
            self.screen.blit(self.splash, (0, 0))
            surf = font1.render(title[0:i + 1], antialias, self.fg, self.bg)
            self.screen.blit(surf, (x, y))
        
        pygame.display.flip()

        pygame.time.wait(5000)
        self.bsound.play()

