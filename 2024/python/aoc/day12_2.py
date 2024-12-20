"""AoC 2024 Day12 Task 1"""

from collections import deque

masks = [
    ((0, -1), (-1, 0), (-1, -1)),  # L U L+U
    ((-1, 0), (0, 1), (-1, 1)),  # U R U+R
    ((1, 0), (0, 1), (1, 1)),  # D R D+R
    ((1, 0), (0, -1), (1, -1)),  # D L D+L
]


# File reading
def fread_all(file_path: str) -> list[str]:
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def flood(board: list[str]):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    clusters = {}

    def fill(point, debug=False):
        row, col = point
        cur_char = board[row][col]

        visited.add(point)
        queue = deque([point])
        neighborhood = {point: set([point])}

        while len(queue) > 0:
            if debug:
                print("queue", queue)

            cur_row, cur_col = queue.popleft()
            for row_off, col_off in directions:
                neighbor_row = cur_row + row_off
                neighbor_col = cur_col + col_off
                pos = (neighbor_row, neighbor_col)
                if (
                    is_valid(pos)
                    and pos not in visited
                    and board[neighbor_row][neighbor_col] == cur_char
                ):
                    visited.add(pos)
                    neighborhood[point].add(pos)
                    queue.append((neighbor_row, neighbor_col))

        for item in neighborhood.items():
            key, values = item
            if key not in clusters:
                clusters[key] = values

        if debug:
            for line in board:
                print(line)
            return neighborhood
        return True

    def tuple_sum(a: tuple, b: tuple):
        ar, ac = a
        br, bc = b
        r = ar + br
        c = ac + bc
        return (r, c)

    def is_valid(point: tuple) -> bool:
        rows, cols = len(board), len(board[0])
        r, c = point
        if 0 <= r < rows and 0 <= c < cols:
            return True
        return False

    def get_char(point: tuple) -> chr:
        row, col = point
        if is_valid((row, col)):
            return board[row][col]
        return None

    def find_clusters():
        for row in range(len(board)):
            for col in range(len(board[0])):
                point = (row, col)
                if point not in visited:
                    fill(point)

    def get_area(point: tuple | None = None) -> int:
        area = 0
        if point is None:
            points = clusters
        else:
            points = [point]
        for item in points:
            area += len(clusters[item])
        return area

    def find_perimeters(clusters: dict):
        res = {}
        for item in clusters.items():
            key, values = item
            total = 0
            for position in values:
                perimeter = len(directions)
                for direction in directions:
                    new_pos = tuple_sum(position, direction)
                    if new_pos in clusters[key]:
                        perimeter += -1
                total += perimeter
            res[key] = total
        return res

    def find_corners(clusters: dict):
        res = {}
        for item in clusters.items():
            key, values = item
            row, col = key
            char = board[row][col]
            total = 0

            for point in values:
                for mask in masks:
                    mask1, mask2, dmask = mask
                    point1 = tuple_sum(point, mask1)
                    point2 = tuple_sum(point, mask2)
                    dpoint = tuple_sum(point, dmask)

                    val1 = get_char(point1)
                    val2 = get_char(point2)
                    dval = get_char(dpoint)

                    if val1 == val2 == char != dval:
                        total += 1

                    elif val1 != char != val2:
                        total += 1

            if key not in res:
                res[key] = 0

            res[key] += total
        return res

    def get_total_cost() -> int:
        res = 0
        perimeters = find_perimeters(clusters)
        for item in perimeters.items():
            key, value = item
            res += value * get_area(key)
        return res

    def get_total_cost2() -> int:
        res = 0
        sides = find_corners(clusters)
        for item in sides.items():
            key, value = item
            res += value * get_area(key)
        return res

    # Exposed vars
    fill.visited = visited
    fill.clusters = clusters
    # Exposed Methods
    fill.is_valid = is_valid
    fill.find_clusters = find_clusters
    fill.get_area = get_area
    fill.find_perimeters = find_perimeters
    fill.get_total_cost = get_total_cost
    fill.get_total_cost2 = get_total_cost2
    fill.find_corners = find_corners

    return fill


def solution(filename: str) -> int:
    data = fread_all(filename)
    data = [x.strip() for x in data]
    board = []
    for line in data:
        board.append([x for x in line])
    del data
    closure = flood(board)
    closure.find_clusters()
    return closure.get_total_cost()


def solution2(filename: str) -> int:
    data = fread_all(filename)
    data = [x.strip() for x in data]
    board = []
    for line in data:
        board.append(list(line))
    del data
    closure = flood(board)
    closure.find_clusters()
    return closure.get_total_cost2()


def main() -> None:
    """Main function"""
    print("Task1:", solution("data/input/12.txt"))
    print("Task2:", solution2("data/input/12.txt"))


if __name__ == "__main__":
    main()
