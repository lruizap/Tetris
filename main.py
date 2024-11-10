import pygame
from sys import exit

# Components
from components.Game import Game
from components.Score import Score
from components.Preview import Preview

from settings import *

from random import choice


class Main:
    def __init__(self):
        # general
        pygame.init()

        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('🗿 TETRIS 🗿')

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys()))
                            for shape in range(3)]

        # Components
        self.game = Game(self.get_next_shapes)
        self.score = Score()
        self.preview = Preview()

    def get_next_shapes(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            # Components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            # updating the game
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    main = Main()
    main.run()
