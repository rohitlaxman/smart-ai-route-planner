"""
===========================================================
Smart AI Route Planner
stats.py

Stores statistics of the current search algorithm.
===========================================================
"""


class SearchStats:
    """
    Stores all statistics related to the currently running
    search algorithm.
    """

    def __init__(self):
        self.reset()

    # --------------------------------------------------

    def reset(self):
        """
        Reset all statistics.
        """

        self.algorithm = ""

        self.status = "Ready"

        self.visited_nodes = 0

        self.path_length = 0

        self.execution_time = 0.0

    # --------------------------------------------------

    def start_search(self, algorithm):
        """
        Called before the algorithm starts.
        """

        self.algorithm = algorithm

        self.status = "Searching..."

        self.visited_nodes = 0

        self.path_length = 0

        self.execution_time = 0.0

    # --------------------------------------------------

    def finish_search(
        self,
        visited_nodes,
        path_length,
        execution_time
    ):
        """
        Called when the search completes successfully.
        """

        self.status = "Completed"

        self.visited_nodes = visited_nodes

        self.path_length = path_length

        self.execution_time = execution_time

    # --------------------------------------------------

    def no_path(
        self,
        visited_nodes,
        execution_time
    ):
        """
        Called when no valid path exists.
        """

        self.status = "No Path Found"

        self.visited_nodes = visited_nodes

        self.path_length = 0

        self.execution_time = execution_time

    # --------------------------------------------------

    def update(
        self,
        algorithm,
        visited_nodes,
        path_length,
        execution_time,
        status
    ):
        """
        Generic update method.
        """

        self.algorithm = algorithm

        self.visited_nodes = visited_nodes

        self.path_length = path_length

        self.execution_time = execution_time

        self.status = status