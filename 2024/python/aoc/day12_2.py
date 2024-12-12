"""AoC 2024 Day12 Task 1"""

from collections import deque


# File reading
def fread_all(file_path: str) -> list[str]:
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def flood(board: list[str]):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    clusters = {}

    def fill(point, new_char: chr = "#", debug=False):
        row, col = point
        cur_char = board[row][col]
        if new_char == cur_char:
            return board

        visited.add(point)
        queue = deque([point])
        neighborhood = {point: set([point])}

        while len(queue) > 0:
            if debug:
                print("queue", queue)

            cur_row, cur_col = queue.popleft()
            board[cur_row][cur_col] = new_char
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

    def is_valid(point: tuple) -> bool:
        row, col = point
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def tuple_sum(a: tuple, b: tuple):
        return tuple(sum(x) for x in zip(a, b))

    def find_clusters():
        for row in range(len(board)):
            for col in range(len(board[0])):
                point = (row, col)
                if point not in visited:
                    fill(point)

    def get_area(point=None) -> int:
        area = 0
        if point is None:
            points = clusters
        else:
            points = [point]
        for item in points:
            area += len(clusters[item])
        return area

    def find_perimeters(clusters):
        res = {}
        for key in clusters:
            total = 0
            for position in clusters[key]:
                perimeter = len(directions)
                for direction in directions:
                    new_pos = tuple_sum(position, direction)
                    if new_pos in clusters[key]:
                        perimeter += -1
                total += perimeter
            res[key] = total
        return res

    def get_total_cost():
        res = 0
        perimeters = find_perimeters(clusters)
        for item in perimeters.items():
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

    return fill


def solution(filename):
    data = fread_all(filename)
    data = [x.strip() for x in data]
    board = []
    for line in data:
        board.append([x for x in line])
    del data
    closure = flood(board)
    closure.find_clusters()
    return closure.get_total_cost()

def main() -> None:
    """Main function"""
    print(solution('data/input/12.txt'))

if __name__ == "__main__":
    main()
