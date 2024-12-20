"""AoC 2024 Day 18 Task 1"""

from collections import deque

# pylint: disable=E0606,E0601,C0103


def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def find_shortest_path(maze, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_pos = (next_x, next_y)

            if (
                0 <= next_x < len(maze)
                and 0 <= next_y < len(maze[0])
                and maze[next_x][next_y] == "."
                and next_pos not in visited
            ):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

    return None


def make_map(width, read_bytes, moves):
    board = []
    for row in range(width):
        board.append([x for x in "." * width])
    for index in range(read_bytes):
        items = moves[index].split(",")
        col, row = int(items[0]), int(items[1])
        board[row][col] = "#"
    return board


def task1(width, start, end, num_bytes, moves):
    board = make_map(width, num_bytes, moves)
    return len(find_shortest_path(board, start, end)) - 1


def task2(width, start, end, moves):

    for index in range(2200, len(moves)):
        board = make_map(width, index, moves)
        if find_shortest_path(board, start, end) is None:
            return moves[index - 1]


if __name__ == "__main__":

    # Task 1
    moves_input = read_file("data/input/18.txt")
    print(f"Task1: {task1(71,(0,0),(70,70),1024, moves_input)}")
    print()
    # Task 2
    print(f"Task2: {task2(71, (0,0), (70,70), moves_input)}")
