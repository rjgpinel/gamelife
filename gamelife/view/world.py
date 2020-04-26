import pygame

from gamelife.view.cell import CellView

class GridWorldView:
    def __init__(self, width, height, world):
        self.cell_size = min(int(width/world.width), int(height/world.height))
        self.width = world.width
        self.height = world.height
        self.cells_view = [[CellView(world.cells[i][j], self.cell_size) for j in range(self.width)] for i in range(self.height)]

    def draw(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                self.cells_view[i][j].draw(screen)
