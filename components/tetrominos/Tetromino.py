import pygame

# Components
from components.tetrominos.Block import Block

from settings import *


class Tetromino:
    def __init__(self, shape, group):

        # setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        # create blocks
        # Instancia dentro de la clase Block para cada una de las posiciones del diccionario de TETROMINOS
        self.blocks = [Block(group=group, pos=pos, color=self.color)
                       for pos in self.block_positions]

    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1
