"""AoC 2024 Day 10 Task 1

The map indicates the height at each position using a scale from 0 (lowest) to 9 (highest).
For example:

0123
1234
8765
9876

A hiking trail == start height 0, ends at height 9, increases by a height of exactly 1 at each step.
Hiking trails never include diagonal steps - only up, down, left, or right

"""

small = [
    "0123",
    "1234",
    "8765",
    "9876",
]

one_trail = [
    "...0...",
    "...1...",
    "...2...",
    "6543456",
    "7.....7",
    "8.....8",
    "9.....9",
]

two_trails = [
    "...0...",
    "...1...",
    "...2...",
    "6543456",
    "......7",
    "......8",
    "......9",
]

four_trails = [
    "..90..9",
    "...1.98",
    "...2..7",
    "6543456",
    "765.987",
    "876....",
    "987....",
]

nine_trails = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]

nine_trails_scores = [5, 6, 5, 3, 1, 3, 5, 3, 5]


# File reading
def fread_all(file_path: str) -> list[str]:
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def tuple_sum(self, a: tuple, b: tuple):
    return tuple(sum(x) for x in zip(a, b))


def is_valid(point: tuple, rows: int, cols: int) -> bool:
    """Checks for OOB"""
    row, col = point
    if 0 <= row < rows and 0 <= col < cols:
        return True


def find_moves(point, value, board):
    rows, cols = len(board), len(board[0])
    moves = []
    row, col = point
    up = row, col - 1
    down = row, col + 1
    left = row - 1, col
    right = row + 1, col
    directions = [up, down, left, right]
    for direction in directions:
        new_row, new_col = direction
        if is_valid(point, rows, cols):
            if board[new_row][new_col] == value:
                moves.append((new_row, new_col))
    return moves


def do_it(point, board, index=0, path=None):
    rows, cols = len(board), len(board[0])
    found_paths = 0
    if path is None:
        path = []
    path.append(point)
    if index >= 8:
        return found_paths
    str_index = str(index)
    moves = find_moves(point, str_index, board)
    for move in moves:
        if is_valid(move, rows, cols):
            print(index)
            found_paths += do_it(move, board, index + 1, path=path)
    return found_paths
