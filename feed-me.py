#!/usr/bin/env python

"""Main file with game loop for PyGame.
"""

import pygame
import random
from hero import Hero
from giant import Giant
from plate import Plate

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
        self.hero = pygame.sprite.GroupSingle(Hero(self.screen))
        self.giant = pygame.sprite.GroupSingle(Giant(self.screen))
        self.plates = pygame.sprite.GroupSingle(Plate(self.screen))


        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

    def splashScreen(beginning):
        if beginning == True:
            #Show the screen
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
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

        for i in range(0, self.background.get_height(), 75):
            rect = pygame.Rect((0, 0), (50, 50))
            rect.center = (random.randint(0, WINDOW_WIDTH), i)
            pygame.draw.rect(self.background, pygame.Color('Black'), rect)


        self.vp = [0, -WINDOW_HEIGHT * 4] 

    def play(self):
        """Start PyGame program.
        """

        running = True
        while running:
            self.clock.tick(FPS)  # Max frames per second
            
            """ This area controls when to display splashScreen at the beginning"""
            # Grabs time since Pygame init
            playTime = pygame.time.get_ticks()
            # Converts ticks from milliseconds into seconds
            playTime = playTime * 1000
            beginning = False
            if playTime < 5:
                beginning = True
                splashScreen(beginning)



            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

            # Draw the scene
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, self.vp)
            self.hero.draw(self.screen)
            self.plates.draw(self.screen)

            self.giant.draw(self.background)

            pygame.display.flip()
            
            self.vp[1] += 15



if __name__ == '__main__':
    game = PyGame()
    game.play()



