"""
===========================================================
Smart AI Route Planner
constants.py

Stores all colors and application settings.
===========================================================
"""

# ---------------- Window ----------------

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

GRID_ROWS = 20
GRID_COLS = 20

CELL_SIZE = 30

# ---------------- Colors ----------------

EMPTY_COLOR = "white"

OBSTACLE_COLOR = "black"

START_COLOR = "green"

GOAL_COLOR = "red"

VISITED_COLOR = "yellow"

PATH_COLOR = "purple"

FRONTIER_COLOR = "deepskyblue"

HOVER_COLOR = "lightgray"

# ---------------- Modes ----------------

MODE_OBSTACLE = "Obstacle"

MODE_START = "Start"

MODE_GOAL = "Goal"

MODE_ERASE = "Erase"

# ---------------- Algorithms ----------------

ALGORITHMS = [
    "Breadth First Search",
    "Depth First Search",
    "Uniform Cost Search",
    "A* Search",
    "Hill Climbing"
]