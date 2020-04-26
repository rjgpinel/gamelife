import pygame

from gamelife.model.cell import CellState

class CellView:

    BG_COLOR = {}
    BG_COLOR[CellState.DEAD] = (120, 120, 120)
    BG_COLOR[CellState.ALIVE] = (255, 255, 255)
    BORDER_COLOR = (0, 0, 0)

    def __init__(self, cell, size):
        self.cell = cell
        self.size = size


    def draw(self, screen):
        rect_shape = (self.size * self.cell.x, self.size * self.cell.y, self.size, self.size)

        pygame.draw.rect(screen, CellView.BG_COLOR[self.cell.state], rect_shape, 0)
        pygame.draw.rect(screen, CellView.BORDER_COLOR, rect_shape, 1)
