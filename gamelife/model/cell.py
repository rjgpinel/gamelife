from enum import Enum

class CellState(Enum):
    DEAD = 0
    ALIVE = 1

class Cell:
    def __init__(self, x, y, neighbors=None):
        self.state = CellState.DEAD
        self.next_state = CellState.DEAD
        self.x = x
        self.y = y
        self.neighbors = [] if neighbors is None else neighbors

    def is_alive(self):
        return self.state == CellState.ALIVE

    def update_next_state(self):
        """Compute next state (t+1) of the cell given the state of
        its neighbors at the present state(t).

        Updates follows original Conway's game of life rules:
           - Birth: Cell with CellState.DEAD at time t will
           transit to CellState.ALIVE at time t+1 if and only if
           3 neighbors were alive at time t.
           - Survival: Cell with CellState.ALIVE will maintain
           in this state if 2 or 3 neighbors with CellState.ALIVE
           at time t.
           - Death: two cases are devised:
              * Overcrowding: Cell that would have CellState.ALIVE
              at time t+1 with 4 or more neighbors with CellState.ALIVE at
              time t, will modify its next state to CellState.ALIVE.
              * Exposure: Cell with CellState.ALIVE at time step t that
              has less than 2 neighbors with CellState.STATE will transit
              to CellState.DEAD at time t+1.
        """
        alive_count = sum([int(neighbor.is_alive()) for neighbor in self.neighbors])

        self.next_state = self.state

        if self.state == CellState.ALIVE:
            if alive_count < 2 or alive_count > 3:
                self.next_state = CellState.DEAD
        elif alive_count == 3:
            self.next_state = CellState.ALIVE

    def update(self):
        self.state = self.next_state

