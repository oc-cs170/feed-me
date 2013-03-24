import pygame

class splashScreen(object):
    def __init__(self, screen):
        self.screen = screen

    def intro_splash(self):

        waiting = True
        while waiting:
            pygame.mixer.pre_init(frequency=22050, size=-16, channels=4, buffersize=4096)


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
            self.screen.fill(pygame.Color('skyblue'))
            font = pygame.font.SysFont(pygame.font.get_default_font(), 60, bold = False)
            
            lines = ["Feed-Me",
                     "",
                     "",
                     "kiwi (worth 50 points)",
                     "fires (worth 30 points)",
                     "watermelon (worth 30 points)",
                     "popcorn (worth 20 points)",
                     "lemon (worth 20 points)",
                     "eggplant (worth 10 points)",
                     "",
                     "Move: Right and Left Arrows",
                     "Space: Jump"
                     
                    ]

            for i in range(len(lines)):
                x = lines[i]
                label = font.render(x, 1, (0,0,0))
                width = label.get_width()
                #self.screen.blit(label, (self.screen.get_width() /2 - width /2, i*50))
                self.screen.blit(label, (0, i*45))



            pygame.display.flip()
