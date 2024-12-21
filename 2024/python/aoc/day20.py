"""AoC 2024 Day 20 Task 1"""

import heapq
from dataclasses import dataclass, field

# pylint: disable=E0606,E0601,C0103


# File Handeling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

@dataclass(slots=True)
class Node:
    """A* node"""
    position: tuple[int, int]
    parent: object = field(default=None)
    cost: int = field(default=0)       # Cost from start node to current node
    heuristic: int = field(default=0)  # Heuristic (estimated cost from current node to goal)
    total_cost: int = field(default=0) # Total cost (g + h)

    def __lt__(self, other):
        return self.total_cost < other.total_cost


def astar(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for neighbor in get_neighbors(maze, current_node.position):
            if neighbor in closed_set:
                continue

            neighbor_node = Node(neighbor, current_node)
            neighbor_node.cost = current_node.cost + 1
            neighbor_node.heuristic = manhattan_distance(neighbor, end_node.position)
            neighbor_node.total_cost = neighbor_node.cost + neighbor_node.heuristic

            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found


def get_neighbors(maze, position):
    x, y = position
    neighbors = []
    if x > 0 and maze[x - 1][y] == 0:
        neighbors.append((x - 1, y))
    if x < len(maze) - 1 and maze[x + 1][y] == 0:
        neighbors.append((x + 1, y))
    if y > 0 and maze[x][y - 1] == 0:
        neighbors.append((x, y - 1))
    if y < len(maze[0]) - 1 and maze[x][y + 1] == 0:
        neighbors.append((x, y + 1))
    return neighbors


def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


def make_maze(filename: str = "../data/test/20.txt"):
    """Return (start, end, maze) converted to ints"""
    output = []
    start = (None, None)
    end = (None, None)
    raw_data = read_file(filename)
    for rindex, row in enumerate(raw_data):
        temp_row = []
        for cindex, col in enumerate(row):
            if col == "S":
                start = (rindex, cindex)
            if col == "E":
                end = (rindex, cindex)
            if col in "SE.":
                temp_row.append(0)
            if col == "#":
                temp_row.append(1)

        output.append(temp_row)
    return start, end, output
