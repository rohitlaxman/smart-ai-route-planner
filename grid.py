"""
===========================================================
Smart AI Route Planner
grid.py

Handles the grid, cell states, and user interaction.
===========================================================
"""

import customtkinter as ctk

from constants import *
from models import Cell


class Grid:

    def __init__(self, parent):

        self.parent = parent

        self.rows = GRID_ROWS
        self.cols = GRID_COLS

        self.current_mode = MODE_OBSTACLE

        self.start = None
        self.goal = None

        self.cells = []
        self.buttons = []

        self.create_grid()

    # --------------------------------------------------

    def create_grid(self):

        for row in range(self.rows):

            self.parent.grid_rowconfigure(row, weight=1)
            self.parent.grid_columnconfigure(row, weight=1)

            cell_row = []
            button_row = []

            for col in range(self.cols):

                cell = Cell(row, col)

                button = ctk.CTkButton(
                    self.parent,
                    text="",
                    width=CELL_SIZE,
                    height=CELL_SIZE,
                    fg_color=EMPTY_COLOR,
                    hover_color=HOVER_COLOR,
                    corner_radius=2,
                    command=lambda r=row, c=col: self.cell_clicked(r, c)
                )

                button.grid(
                    row=row,
                    column=col,
                    padx=1,
                    pady=1,
                    sticky="nsew"
                )

                cell_row.append(cell)
                button_row.append(button)

            self.cells.append(cell_row)
            self.buttons.append(button_row)

    # --------------------------------------------------

    def set_mode(self, mode):

        self.current_mode = mode

    # --------------------------------------------------

    def cell_clicked(self, row, col):

        if self.current_mode == MODE_START:
            self.set_start(row, col)

        elif self.current_mode == MODE_GOAL:
            self.set_goal(row, col)

        elif self.current_mode == MODE_OBSTACLE:
            self.toggle_obstacle(row, col)

        elif self.current_mode == MODE_ERASE:
            self.erase(row, col)

    # --------------------------------------------------

    def paint(self, row, col, color):

        self.buttons[row][col].configure(
            fg_color=color,
            hover_color=color
        )

    # --------------------------------------------------

    def set_start(self, row, col):

        if self.goal == (row, col):
            return

        if self.start is not None:

            old_row, old_col = self.start

            self.cells[old_row][old_col].set_empty()

            self.paint(old_row, old_col, EMPTY_COLOR)

        self.start = (row, col)

        self.cells[row][col].set_start()

        self.paint(row, col, START_COLOR)

    # --------------------------------------------------

    def set_goal(self, row, col):

        if self.start == (row, col):
            return

        if self.goal is not None:

            old_row, old_col = self.goal

            self.cells[old_row][old_col].set_empty()

            self.paint(old_row, old_col, EMPTY_COLOR)

        self.goal = (row, col)

        self.cells[row][col].set_goal()

        self.paint(row, col, GOAL_COLOR)

    # --------------------------------------------------

    def toggle_obstacle(self, row, col):

        if (row, col) == self.start:
            return

        if (row, col) == self.goal:
            return

        cell = self.cells[row][col]

        if cell.is_obstacle():

            cell.set_empty()

            self.paint(row, col, EMPTY_COLOR)

        else:

            cell.set_obstacle()

            self.paint(row, col, OBSTACLE_COLOR)

    # --------------------------------------------------

    def erase(self, row, col):

        if self.start == (row, col):
            self.start = None

        if self.goal == (row, col):
            self.goal = None

        self.cells[row][col].set_empty()

        self.paint(row, col, EMPTY_COLOR)

    # --------------------------------------------------

    def clear_grid(self):

        self.start = None
        self.goal = None

        for row in range(self.rows):

            for col in range(self.cols):

                self.cells[row][col].set_empty()

                self.paint(row, col, EMPTY_COLOR)

    # --------------------------------------------------

    def reset_search(self):

        for row in range(self.rows):

            for col in range(self.cols):

                cell = self.cells[row][col]

                if cell.is_empty():
                    self.paint(row, col, EMPTY_COLOR)

                elif cell.is_start():
                    self.paint(row, col, START_COLOR)

                elif cell.is_goal():
                    self.paint(row, col, GOAL_COLOR)

                elif cell.is_obstacle():
                    self.paint(row, col, OBSTACLE_COLOR)

    # --------------------------------------------------

    def get_neighbors(self, row, col):

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        neighbors = []

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols:

                if not self.cells[nr][nc].is_obstacle():
                    neighbors.append((nr, nc))

        return neighbors