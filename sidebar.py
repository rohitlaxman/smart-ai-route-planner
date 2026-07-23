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

        # ---------------- Status ----------------

        self.status = ctk.CTkLabel(
            self,
            text="Mode : Obstacle",
            font=("Arial", 14)
        )

        self.status.pack(pady=30)

    # ----------------------------------------------------

    def mode_changed(self, mode):

        self.status.configure(
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