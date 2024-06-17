import pygame

from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):

        # general
        super().__init__(group)

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color=color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)

    def horizontal_collide(self, x):
        if not 0 <= x < COLUMNS:
            return True

    def vertical_collide(self, y):
        if y >= ROWS:
            return True

    def update(self):
        # self.pos -> rect
        self.rect.topleft = self.pos * CELL_SIZE
