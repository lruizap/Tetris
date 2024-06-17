import pygame
from random import choice

# Components
from components.Timer import Timer
from components.tetrominos.Tetromino import Tetromino

from settings import *


class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        # border
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))

        # sprites
        self.sprites = pygame.sprite.Group()

        # lines
        self.line_surface = self.surface.copy()
        # hide the color green for this surface
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(120)

        # tetromino
        self.tetromino = Tetromino(shape=choice(
            list(TETROMINOS.keys())), group=self.sprites)

        # timer
        self.timers = {
            'vertical move': Timer(UPDATE_START_SPEED, True, self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(surface=self.line_surface, color=LINE_COLOR,
                             start_pos=(x, 0), end_pos=(x, self.surface.get_height()), width=1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(surface=self.line_surface, color=LINE_COLOR, start_pos=(
                0, y), end_pos=(self.surface.get_width(), y), width=1)

        self.surface.blit(self.line_surface, (0, 0))

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

    def run(self):

        # update
        self.input()
        self.timer_update()
        self.sprites.update()

        # drawing
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        pygame.draw.rect(surface=self.display_surface, color=LINE_COLOR,
                         rect=self.rect, width=2, border_radius=2)
