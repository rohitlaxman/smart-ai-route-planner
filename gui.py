"""
===========================================================
Smart AI Route Planner
gui.py

Main application window.
===========================================================
"""

import time
import customtkinter as ctk
from tkinter import messagebox

from constants import *
from grid import Grid
from sidebar import Sidebar
from algorithms import SearchAlgorithms
from visualizer import Visualizer
from stats import SearchStats


class SmartRoutePlannerGUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Smart AI Route Planner")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # ---------------- Statistics ----------------

        self.stats = SearchStats()

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

        self.sidebar.update_statistics(self.stats)

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

        self.stats.reset()

        self.sidebar.update_statistics(self.stats)

    # ----------------------------------------------------

    def run_algorithm(self):

        if self.grid_object.start is None:

            messagebox.showerror(
                "Missing Start Node",
                "Please select a START node."
            )

            return

        if self.grid_object.goal is None:

            messagebox.showerror(
                "Missing Goal Node",
                "Please select a GOAL node."
            )

            return

        algorithm = self.sidebar.get_selected_algorithm()

        # ---------------- Search Started ----------------

        self.stats.start_search(algorithm)

        self.sidebar.update_statistics(self.stats)

        self.update()

        start_time = time.perf_counter()

        # ---------------- BFS ----------------

        if algorithm == "Breadth First Search":

            path, visited = SearchAlgorithms.bfs(
                self.grid_object
            )

        else:

            messagebox.showinfo(
                "Coming Soon",
                f"{algorithm} will be implemented soon."
            )

            return

        execution_time = time.perf_counter() - start_time

        # ---------------- Statistics ----------------

        if path:

            self.stats.finish_search(
                visited_nodes=len(visited),
                path_length=len(path),
                execution_time=execution_time
            )

        else:

            self.stats.no_path(
                visited_nodes=len(visited),
                execution_time=execution_time
            )

        self.sidebar.update_statistics(self.stats)

        # ---------------- Animate ----------------

        self.visualizer.animate(
            visited,
            path
        )