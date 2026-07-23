"""
===========================================================
Smart AI Route Planner
algorithms.py

Classical AI Search Algorithms
===========================================================
"""

from collections import deque


class SearchAlgorithms:

    @staticmethod
    def bfs(grid):
        """
        Breadth First Search

        Parameters:
            grid -> Grid object

        Returns:
            path
            visited
        """

        if grid.start is None or grid.goal is None:
            return [], []

        start = grid.start
        goal = grid.goal

        queue = deque([start])

        visited = {start}

        parent = {}

        exploration_order = []

        while queue:

            current = queue.popleft()

            exploration_order.append(current)

            if current == goal:
                break

            row, col = current

            for neighbor in grid.get_neighbors(row, col):

                if neighbor not in visited:

                    visited.add(neighbor)

                    parent[neighbor] = current

                    queue.append(neighbor)

        if goal not in visited:
            return [], exploration_order

        path = []

        node = goal

        while node != start:

            path.append(node)

            node = parent[node]

        path.append(start)

        path.reverse()

        return path, exploration_order