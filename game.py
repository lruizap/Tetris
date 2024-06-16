import pygame

from settings import *


class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        # border
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))

        # lines
        self.line_surface = self.surface.copy()
        # hide the color green for this surface
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(120)

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

    def run(self):

        # drawing
        self.surface.fill(GRAY)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        pygame.draw.rect(surface=self.display_surface, color=LINE_COLOR,
                         rect=self.rect, width=2, border_radius=2)
