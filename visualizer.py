"""
===========================================================
Smart AI Route Planner
visualizer.py
===========================================================
"""

from constants import *


class Visualizer:

    def __init__(self, grid):

        self.grid = grid

        self.delay = 25

    # ----------------------------------------------------

    def animate(self, visited, path):

        self.grid.reset_search()

        delay = 0

        for row, col in visited:

            if (row, col) == self.grid.start:
                continue

            if (row, col) == self.grid.goal:
                continue

            self.grid.buttons[row][col].after(
                delay,
                lambda r=row, c=col:
                self.grid.paint(r, c, VISITED_COLOR)
            )

            delay += self.delay

        for row, col in path:

            if (row, col) == self.grid.start:
                continue

            if (row, col) == self.grid.goal:
                continue

            self.grid.buttons[row][col].after(
                delay,
                lambda r=row, c=col:
                self.grid.paint(r, c, PATH_COLOR)
            )

            delay += self.delay