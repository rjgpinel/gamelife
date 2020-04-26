import sys

import pygame
from pygame.locals import *

from gamelife.model.world import GridWorld
from gamelife.view.world import GridWorldView
from gamelife.model.cell import CellState

pygame.init()

fps = 10
fpsClock = pygame.time.Clock()

width, height = 480, 480
num_cells_x, num_cells_y = 24, 24

world = GridWorld(num_cells_x, num_cells_y)
world_view = GridWorldView(width, height, world)

screen = pygame.display.set_mode((width, height))

paused = False

# Define initial state
world.cells[4][4].state = CellState.ALIVE
world.cells[4][5].state = CellState.ALIVE
world.cells[4][6].state = CellState.ALIVE

while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
        paused = not paused

  if not paused:
      screen.fill((0, 0, 0))

      # Update world
      world.update_map()

      # Draw world
      world_view.draw(screen)


  pygame.display.flip()
  fpsClock.tick(fps)
