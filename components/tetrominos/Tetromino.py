# Components
from components.tetrominos.Block import Block

from settings import *


class Tetromino:
    def __init__(self, shape, group, create_new_tetromino, field_data):

        # setup
        self.shape = shape
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.create_new_tetromino = create_new_tetromino
        self.field_data = field_data

        # create blocks
        # Instancia dentro de la clase Block para cada una de las posiciones del diccionario de TETROMINOS
        self.blocks = [Block(group=group, pos=pos, color=self.color)
                       for pos in self.block_positions]

    # collisions
    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(
            int(block.pos.x + amount), self.field_data) for block in blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(
            int(block.pos.y + amount), self.field_data) for block in blocks]
        return True if any(collision_list) else False

    # movement
    def move_horizontal(self, amount):
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount

    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

    # rotate
    def rotate(self):
        if self.shape != 'O':

            # 1. pivot point
            pivot_pos = self.blocks[0].pos

            # 2. New block position
            new_block_positions = [block.rotate(
                pivot_pos) for block in self.blocks]

            # 3. Collision check
            for pos in new_block_positions:
                # horizontal
                if pos.x < 0 or pos.x >= COLUMNS:
                    return
                # field
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                # vertical / floor
                if pos.y > ROWS:
                    return

            # 4. new position
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
