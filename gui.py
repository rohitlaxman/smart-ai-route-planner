"""
===========================================================
Smart AI Route Planner
gui.py

Main application window.
===========================================================
"""

import customtkinter as ctk

from constants import *
from grid import Grid
from sidebar import Sidebar
from algorithms import SearchAlgorithms
from visualizer import Visualizer


class SmartRoutePlannerGUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Smart AI Route Planner")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # ---------------- Layout ----------------

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ns"
        )

        # ---------------- Grid ----------------

        self.grid_frame = ctk.CTkFrame(self)

        self.grid_frame.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.grid_object = Grid(self.grid_frame)

        self.visualizer = Visualizer(self.grid_object)

        # ---------------- Connect Callbacks ----------------

        self.sidebar.mode_callback = self.change_mode
        self.sidebar.clear_callback = self.clear_grid
        self.sidebar.run_callback = self.run_algorithm

    # ----------------------------------------------------

    def change_mode(self, mode):

        self.grid_object.set_mode(mode)

    # ----------------------------------------------------

    def clear_grid(self):

        self.grid_object.clear_grid()

    # ----------------------------------------------------

    def run_algorithm(self):

        if self.grid_object.start is None:

            print("Please select a START node.")

            return

        if self.grid_object.goal is None:

            print("Please select a GOAL node.")

            return

        algorithm = self.sidebar.get_selected_algorithm()

        if algorithm == "Breadth First Search":

            path, visited = SearchAlgorithms.bfs(
                self.grid_object
            )

            self.visualizer.animate(
                visited,
                path
            )

        else:

            print(f"{algorithm} will be implemented soon.")