#!/usr/bin/env python

"""Main file with game loop for PyGame.
"""

import pygame
import random
from hero import Hero
from giant import Giant
from plate import Plate
from food import Food

WINDOW_TITLE = 'PyGame'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 750
FPS = 30



class PyGame(object):
    """Create a game of PyGame."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.make_background()
        self.hero = pygame.sprite.GroupSingle(Hero(self.background))
        self.giant = pygame.sprite.GroupSingle(Giant(self.screen))
        self.plates = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()


        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

    def splashScreen(self):
        # Converts ticks from milliseconds into seconds
        while pygame.time.get_ticks() < 5:
            self.screen.fill(pygame.Color('green'))
            pygame.display.flip()



    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        floor = pygame.sprite.Sprite()
        floor.image = pygame.Surface((90, 16)).convert_alpha()
        floor.image.fill(pygame.Color('green'))
        floor.rect = floor.image.get_rect(midbottom=(self.screen.get_width() / 2, self.background.get_height() + 10))

        self.plates.add(floor)
        food_probability = [5, 10, 20, 35, 50, 70]

        # self.plates = pygame.sprite.Group()
        plate_yloc = self.background.get_height() - 50
                
        while plate_yloc > 60:

            plate_xloc = (random.randint(0, WINDOW_WIDTH))
            plate = Plate(self.background, plate_xloc, plate_yloc)
            self.plates.add(plate)
            food_check = random.randint(1, 100)

            for i in range(6):
                if food_check < food_probability[i]:
                    self.foods.add(Food(i, plate))
                    break
            
            plate_yloc -= 40

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

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.hero.sprite.xv = 0
                
            # Is the hero colliding with a plate?
            contact = pygame.sprite.spritecollide(self.hero.sprite, self.plates, False,
                                                  pygame.sprite.collide_mask)

            if contact:
                print contact[0].rect.center
                self.hero.sprite.plate = contact
            else:
                self.hero.sprite.plate = contact

            # Draw the scene
            self.screen.fill((0, 0, 0))
            self.background.fill(pygame.Color('skyblue'))
            self.giant.draw(self.background)
            self.plates.draw(self.background)
            self.foods.draw(self.background)
            self.hero.update()
            self.hero.draw(self.background)
            self.screen.blit(self.background, self.vp)
            pygame.display.flip()
            
            self.vp[1] += 0
            self.vp[1] = min(self.vp[1], 0)

if __name__ == '__main__':
    game = PyGame()
    game.play()



