"""
===========================================================
Smart AI Route Planner
models.py

Contains data models used throughout the project.
===========================================================
"""

from dataclasses import dataclass


@dataclass
class Cell:
    """
    Represents a single cell in the grid.
    """

    row: int
    col: int
    state: str = "EMPTY"

    def position(self):
        """
        Returns the (row, col) tuple.
        """
        return (self.row, self.col)

    def is_empty(self):
        return self.state == "EMPTY"

    def is_obstacle(self):
        return self.state == "OBSTACLE"

    def is_start(self):
        return self.state == "START"

    def is_goal(self):
        return self.state == "GOAL"

    def set_empty(self):
        self.state = "EMPTY"

    def set_obstacle(self):
        self.state = "OBSTACLE"

    def set_start(self):
        self.state = "START"

    def set_goal(self):
        self.state = "GOAL"