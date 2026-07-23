"""
===========================================================
Smart AI Route Planner
visualizer.py

Handles all search animations.
===========================================================
"""

from constants import *


class Visualizer:

    def __init__(self, grid):

        self.grid = grid

        # Default animation delay (milliseconds)
        self.delay = 25

    # ----------------------------------------------------

    def set_speed(self, delay):
        """
        Update animation speed.
        """

        self.delay = delay

    # ----------------------------------------------------

    def animate(self, visited, path):
        """
        Animate the complete search process.
        """

        self.grid.reset_search()

        current_delay = 0

        current_delay = self.animate_visited(
            visited,
            current_delay
        )

        self.animate_path(
            path,
            current_delay
        )

    # ----------------------------------------------------

    def animate_visited(
        self,
        visited,
        delay
    ):
        """
        Animate explored nodes.
        """

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

        return delay

    # ----------------------------------------------------

    def animate_path(
        self,
        path,
        delay
    ):
        """
        Animate the final shortest path.
        """

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