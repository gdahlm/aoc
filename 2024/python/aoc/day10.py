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

small_test = [
    "0123",
    "1234",
    "8765",
    "9876",
]

two_trails_test = [
    "...0...",
    "...1...",
    "...2...",
    "6543456",
    "7.....7",
    "8.....8",
    "9.....9",
]

four_trails_test = [
    "..90..9",
    "...1.98",
    "...2..7",
    "6543456",
    "765.987",
    "876....",
    "987....",
]

nine_trails_test = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]

nine_trails_test_scores = [5, 6, 5, 3, 1, 3, 5, 3, 5]


# File reading
def fread_all(file_path: str) -> list[str]:
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def find_frontier(board: list[str], directions: str | None=None) -> list[tuple]:
    """Return points of the frontier of a point"""
    # Closure: foo = frontier(board)
    # foo((1,1), ['N']) -> [(0, 1)]
    rows, cols = len(board), len(board[0])
    masks = {
        # D:(r,c)
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
    }

    if directions is None:
        directions = masks.keys()

    def is_valid(point: tuple) -> bool:
        """Checks for OOB"""
        r, c = point
        if 0 <= r < rows and 0 <= c < cols:
            return True
        return False

    def points(point:tuple, directions: str=directions):
        """Main function"""
        r, c = point
        res = set()
        for key in directions:
            r_off, c_off = masks[key]
            r_new, c_new = r + r_off, c + c_off
            if is_valid((r_new, c_new)):
                res.add((r + r_off, c + c_off))
        return list(res)

    return points


def find_trailheads(board: list) -> list[tuple]:
    res = []
    for rindex, row in enumerate(board):
        for cindex, col in enumerate(row):
            if col == "0":
                res.append((rindex, cindex))
    return res


def find_next_move(point: tuple, board: list[str], visited: list[tuple]| None=None):
    # Closures
    frontier = find_frontier(board)
    if visited is None:
        visited = set()
    res = []
    moves = set(frontier(point))
    moves.difference(visited)
    # TODO recursion?

    return res


def find_hiking_trails(trailhead: tuple, board: list, visited=None):
    #rows, cols = len(board), len(board[0])
    if visited is None:
        visited = set()
    res = []

    # Inital data discovery
    trailheads = find_trailheads(board)

    for trailhead in trailheads:
        _ = find_next_move(trailhead, board)
    # TODO core logic
    return res


def main() -> None:
    """Main function"""
    #TODO fake mocked up
    res = []
    board = fread_all("data/test/10.txt")
    trailheads = find_trailheads(board)
    for trailhead in trailheads:
        _ =find_hiking_trails(trailhead, board)
        print(_)

    return res

if __name__ == "__main__":
    main()
