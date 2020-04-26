from gamelife.model.cell import Cell

class GridWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(j, i) for j in range(width)] for i in range(height)]

        # Set neighbors
        for i in range(height):
            for j in range(width):
                self.cells[i][j].neighbors = [self.cells[i-1][j-1],
                                        self.cells[i-1][j],
                                        self.cells[i][j-1],
                                        self.cells[i-1][(j+1) % width],
                                        self.cells[(i+1) % height][j-1],
                                        self.cells[(i+1) % height][j],
                                        self.cells[i][(j+1) % width],
                                        self.cells[(i+1) % height][(j+1) % width]
                ]

    def update_next_state(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].update_next_state()

    def update_state(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].update()

    def update_map(self):
        self.update_next_state()
        self.update_state()
