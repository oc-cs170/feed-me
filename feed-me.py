#!/usr/bin/env python

"""Main file with game loop for PyGame.
"""

import pygame
import random
import math
from hero import Hero
from giant import Giant
from plate import Plate
from food import Food
from scoreboard import ScoreBoard


WINDOW_TITLE = 'Feed-Me'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
FPS = 30



class PyGame(object):
    """Create a game of PyGame."""
    def __init__(self):
        pygame.mixer.init(11025,-16,2,4096)    
        pygame.mixer.set_num_channels(3)
       
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.make_background()

        self.scoreboard = ScoreBoard(self.screen)

        self.hero = pygame.sprite.GroupSingle(Hero(self.background))
        self.giant = pygame.sprite.GroupSingle(Giant(self.background))
        self.plates = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()
       
        self.level = self.scoreboard.items.sprites()[1]
        self.score = self.scoreboard.items.sprites()[4]
        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

        #music
   
        self.bounce = pygame.mixer.Sound('sounds/bounce.ogg')
        self.bsound = pygame.mixer.Sound('sounds/bsound.ogg')
        self.chew = pygame.mixer.Sound('sounds/eating.wav')


        
    def splashScreen(self):
        # Converts ticks from milliseconds into seconds
        
        #music
        self.bsound.set_volume(0.2)
        self.bsound.play(loops=100, maxtime=0, fade_ms=0)


        while pygame.time.get_ticks() < 5000:
            self.screen.fill(pygame.Color('skyblue'))
            font = pygame.font.SysFont(pygame.font.get_default_font(), 60, bold = True)
            
            lines = ["Feed-Me",
                     "",
                     "",
                     "Move: Right and Left Arrows",
                     "Space: Jump"
                    ]

            for i in range(5):
                x = lines[i]
                label = font.render(x, 1, (0,0,0))
                width = label.get_width()
                self.screen.blit(label, (WINDOW_WIDTH /2 - width /2, i*50))

            pygame.display.flip()

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """

        self.scrollspeed = 0

        floor = pygame.sprite.Sprite()
        floor.image = pygame.Surface((self.screen.get_width(), 16)).convert_alpha()
        floor.image.fill(pygame.Color('green'))
        floor.rect = floor.image.get_rect(midbottom=(self.screen.get_width() / 2, self.background.get_height() + 10))

        ceiling = pygame.sprite.Sprite()
        ceiling.image = floor.image.copy()
        ceiling.image.fill(pygame.Color('black'))
        ceiling.rect = ceiling.image.get_rect(top=self.giant.sprite.rect.bottom)

        self.plates.add(floor)
        self.plates.add(ceiling)

        food_probability = [5, 10, 20, 35, 50, 70]

        # self.plates = pygame.sprite.Group()
        
        plate_xloc = self.screen.get_width() / 2
        plate_yloc = self.background.get_height() - 50
                
        while plate_yloc > ceiling.rect.bottom:
            xlocs = [9999999]
            
            for i in range(random.randint(1, 3)):
                approved = False
                while not approved:
                    new_xloc = random.choice((random.randint(plate_xloc - 240, plate_xloc - 80),
                                          random.randint(plate_xloc + 80, plate_xloc + 240)))
                    new_xloc = max(min(new_xloc, self.screen.get_width() - 40), 40)

                    good = [j for j in xlocs if math.fabs(j - new_xloc) > 80]
                    if len(good) == len(xlocs):
                        approved = True

                xlocs.append(new_xloc)
                plate_xloc = new_xloc
                plate = Plate(self.background, plate_xloc, plate_yloc)
                self.plates.add(plate)

                food_check = random.randint(1, 100)
                for i in range(6):
                    if food_check < food_probability[i]:
                        self.foods.add(Food(i, plate))
                        break

            plate_yloc -= random.randint(40, 120)

        self.game_over = False
        self.round = 0

        self.new_round()

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """
        self.round += 1   

    def make_background(self):
        self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT * 5))
        self.background.fill(pygame.Color('skyblue'))
        self.vp = [0, -WINDOW_HEIGHT * 4] 

    def play(self):
        """Start PyGame program.
        """

        self.new_game()
        self.splashScreen()
        
        running = True
        while running:
            self.clock.tick(FPS)  # Max frames per second

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.hero.sprite.xv = 5
                    if event.key == pygame.K_LEFT:
                        self.hero.sprite.xv = -5
                    if event.key == pygame.K_SPACE:
                        self.hero.sprite.jump = True
                        self.bounce.set_volume(0.3)
                        self.bounce.play(loops=0, maxtime=0, fade_ms=0)

                    # cheat code
                    # if event.key == pygame.K_UP:
                    #     self.hero.sprite.yv = -20

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.hero.sprite.xv = 0


            # Is the hero colliding with a plate?
            contact = pygame.sprite.spritecollide(self.hero.sprite, self.plates, False,
                                                  pygame.sprite.collide_mask)

            self.hero.sprite.plate = contact


            # If hero picks up food
            collect = pygame.sprite.spritecollide(self.hero.sprite, self.foods, True,
                                                  pygame.sprite.collide_mask) 

            if collect:
                for meal in collect:
                    self.score.text += meal.points
                    self.chew.play(loops=0, maxtime=1500, fade_ms=0)
                    self.chew.set_volume(1.0)


            if self.background.get_height() - self.hero.sprite.rect.centery > WINDOW_HEIGHT / 2:
                self.scrollspeed = self.level.text + 1


            # Draw the scene
            self.screen.fill((0, 0, 0))
            self.background.fill(pygame.Color('skyblue'))

            self.giant.draw(self.background)
            self.plates.draw(self.background)
            self.foods.draw(self.background)

            self.hero.update()
            self.hero.draw(self.background)

            self.screen.blit(self.background, self.vp)

            # Do the scoreboard
            self.scoreboard.update()
            self.scoreboard.draw(self.screen)

            pygame.display.flip()
            self.vp[1] += self.scrollspeed
            self.vp[1] = min(self.vp[1], 0)

if __name__ == '__main__':
    game = PyGame()
    game.play()



