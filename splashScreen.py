import pygame

class splashScreen(object):
    def __init__(self, screen):
        self.screen = screen







    def intro_splash(self):
        while pygame.time.get_ticks() < 5000:

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
