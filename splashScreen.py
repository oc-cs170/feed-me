import pygame


class splashScreen(object):
    def __init__(self, screen):
        self.screen = screen
        # pygame.mixer.init(11025,-16,2,4096)    
        # pygame.mixer.set_num_channels(3)
        # self.bsound = pygame.mixer.Sound('sounds/bsound.ogg')

    def intro_splash(self):
        #music
        # self.bsound.set_volume(0.2)
        # self.bsound.play(loops=100, maxtime=0, fade_ms=0)
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
