"""
===========================================================
Smart AI Route Planner
stats.py

Stores statistics of the current algorithm.
===========================================================
"""


class SearchStats:

    def __init__(self):

        self.reset()

    # --------------------------------------------------

    def reset(self):

        self.algorithm = ""

        self.visited_nodes = 0

        self.path_length = 0

        self.execution_time = 0.0

        self.status = "Ready"

    # --------------------------------------------------

    def update(
        self,
        algorithm,
        visited_nodes,
        path_length,
        execution_time,
        status
    ):

        self.algorithm = algorithm

        self.visited_nodes = visited_nodes

        self.path_length = path_length

        self.execution_time = execution_time

        self.status = status