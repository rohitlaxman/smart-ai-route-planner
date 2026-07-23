"""
===========================================================
Smart AI Route Planner
sidebar.py

Contains the left control panel.
===========================================================
"""

import customtkinter as ctk

from constants import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, width=280)

        self.run_callback = None
        self.clear_callback = None
        self.mode_callback = None

        self.create_widgets()

    # ----------------------------------------------------

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Smart AI Route Planner",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        # ---------------- Algorithm ----------------

        ctk.CTkLabel(
            self,
            text="Algorithm"
        ).pack(anchor="w", padx=20)

        self.algorithm_menu = ctk.CTkOptionMenu(
            self,
            values=ALGORITHMS
        )

        self.algorithm_menu.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # ---------------- Mode ----------------

        ctk.CTkLabel(
            self,
            text="Edit Mode"
        ).pack(anchor="w", padx=20, pady=(20, 0))

        self.mode_menu = ctk.CTkOptionMenu(
            self,
            values=[
                MODE_OBSTACLE,
                MODE_START,
                MODE_GOAL,
                MODE_ERASE
            ],
            command=self.mode_changed
        )

        self.mode_menu.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # ---------------- Run ----------------

        self.run_button = ctk.CTkButton(
            self,
            text="Run Algorithm",
            command=self.run_pressed
        )

        self.run_button.pack(
            fill="x",
            padx=20,
            pady=(30, 10)
        )

        # ---------------- Clear ----------------

        self.clear_button = ctk.CTkButton(
            self,
            text="Clear Grid",
            command=self.clear_pressed
        )

        self.clear_button.pack(
            fill="x",
            padx=20
        )

        # ==================================================
        # SEARCH STATISTICS
        # ==================================================

        divider = ctk.CTkLabel(
            self,
            text="────────────────────────"
        )
        divider.pack(pady=(25, 10))

        heading = ctk.CTkLabel(
            self,
            text="Search Statistics",
            font=("Arial", 16, "bold")
        )
        heading.pack()

        # ---------------- Status ----------------

        self.status_value = ctk.CTkLabel(
            self,
            text="Ready",
            font=("Arial", 14)
        )
        self.status_value.pack(pady=(10, 5))

        # ---------------- Algorithm ----------------

        self.algorithm_value = ctk.CTkLabel(
            self,
            text="Algorithm : -",
            anchor="w"
        )
        self.algorithm_value.pack(fill="x", padx=20)

        # ---------------- Nodes ----------------

        self.nodes_value = ctk.CTkLabel(
            self,
            text="Visited Nodes : 0",
            anchor="w"
        )
        self.nodes_value.pack(fill="x", padx=20)

        # ---------------- Path ----------------

        self.path_value = ctk.CTkLabel(
            self,
            text="Path Length : 0",
            anchor="w"
        )
        self.path_value.pack(fill="x", padx=20)

        # ---------------- Time ----------------

        self.time_value = ctk.CTkLabel(
            self,
            text="Execution Time : 0.000 s",
            anchor="w"
        )
        self.time_value.pack(fill="x", padx=20)

        # ==================================================

        self.mode_status = ctk.CTkLabel(
            self,
            text="Mode : Obstacle",
            font=("Arial", 14)
        )

        self.mode_status.pack(
            side="bottom",
            pady=20
        )

    # ----------------------------------------------------

    def update_statistics(self, stats):

        """
        Update all statistics shown in the sidebar.
        """

        self.status_value.configure(
            text=stats.status
        )

        algorithm = stats.algorithm if stats.algorithm else "-"

        self.algorithm_value.configure(
            text=f"Algorithm : {algorithm}"
        )

        self.nodes_value.configure(
            text=f"Visited Nodes : {stats.visited_nodes}"
        )

        self.path_value.configure(
            text=f"Path Length : {stats.path_length}"
        )

        self.time_value.configure(
            text=f"Execution Time : {stats.execution_time:.4f} s"
        )

    # ----------------------------------------------------

    def mode_changed(self, mode):

        self.mode_status.configure(
            text=f"Mode : {mode}"
        )

        if self.mode_callback:
            self.mode_callback(mode)

    # ----------------------------------------------------

    def run_pressed(self):

        if self.run_callback:
            self.run_callback()

    # ----------------------------------------------------

    def clear_pressed(self):

        if self.clear_callback:
            self.clear_callback()

    # ----------------------------------------------------

    def get_selected_algorithm(self):

        return self.algorithm_menu.get()