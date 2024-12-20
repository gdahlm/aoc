"""AoC 2024 Day 15 Task 1"""

from dataclasses import dataclass, field

# Constents
GPS_VALUE = ()
CHARS = {
    "robot": "@",
    "box": "O",
    "wall": "#",
    "empty": ".",
}

# Dataclases


@dataclass
class Point:
    """Generic point data object"""

    x: int
    y: int


@dataclass(slots=True)
class Robot:
    """Robot object dataclass"""

    row: int = field(repr=False)
    col: int = field(repr=False)
    location: tuple[int, int] = field(init=False)
    last_move: str = field(default=None)

    def __post_init__(self):
        self.location = (self.row, self.col)


# File handling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def clean_data(filename: str) -> list[list[str]]:
    raw_input = read_file(filename)
    board = []
    moves = []
    for line in raw_input:
        match line:
            case "":
                pass
            case str() if "#" in line:
                board.append(line)
            case _:
                moves.append(line)
    return board, moves


def board_to_array(board: list[str]) -> list[list[chr]]:
    res = []
    for line in board:
        res.append([x for x in line])
    return res


def tuple_sum(a: tuple, b: tuple):
    return tuple(sum(x) for x in zip(a, b))


def parse_move(move: chr) -> tuple[int, int]:
    """Return move mask tuple"""
    match move:
        case "^" | "up" | "u":
            return (-1, 0)
        case "v" | "down" | "d":
            return (1, 0)
        case ">" | "right" | "r":
            return (0, 1)
        case "<" | "left" | "l":
            return (0, -1)
    return None


def look_ahead(board, location, move_mask, res=None):
    """See if boxes can move"""
    rows, cols = len(board), len(board[0])
    if res is None:
        res = []
    if not isinstance(move_mask, tuple) or not isinstance(location, tuple):
        return res

    next_loc = tuple_sum(location, move_mask)
    new_row, new_col = next_loc
    if rows >= new_row < 0 or cols >= new_col < 0:
        return res

    new_char = board[new_row][new_col]

    if new_char == CHARS["wall"]:
        return res

    res.extend(new_char)

    _ = look_ahead(board, (new_row, new_col), move_mask)
    res.extend(_.copy())

    return res


def do_move(
    board: list[str] | list[list[str]], location: tuple[int, int], direction: str
):
    """Do individual move"""
    if board is None:
        return None
    cur_row, cur_col = location
    robot = Robot(cur_row, cur_col)
    board = board.copy()  # Shallow copy
    if isinstance(board[0], str):
        board = board_to_array(board)

    move_mask = parse_move(direction)
    move_slice = look_ahead(board, (robot.row, robot.col), move_mask)
    # print(move_slice)

    match move_slice:
        case [] | None:
            return board

    slice_index = move_slice.index(CHARS["empty"])

    if "." in move_slice:
        dot_loc_index = move_slice.index(".")
        # print(f"Index: {slice_index} Slice:{move_slice}")
        # TODO
        slice_tail = move_slice.pop(slice_index)
        new_slice = [CHARS["empty"], CHARS["robot"]]
        new_slice.extend(move_slice)
        # print(f"New slice: {new_slice}")

        _ = write_updates(board, location, move_mask, new_slice)
        return find_robot(board)


def print_board(board: list[str] | list[list[str]]) -> None:
    if isinstance(board[0], list) and isinstance(board[0][0], str):
        for line in board:
            print("".join(line))
    elif isinstance(board[0], str):
        for line in board:
            print(line)


def write_updates(board, location, move_mask, new_slice, index=0, res=None):
    """write the new slice to the board"""
    rows, cols = len(board), len(board[0])
    if len(new_slice) == 0:
        return board
    if index > 0:
        next_loc = tuple_sum(location, move_mask)
    else:
        next_loc = location

    new_row, new_col = next_loc
    new_char = new_slice.pop(0)

    if rows >= new_row < 0 or cols >= new_col < 0:
        return res

    board[new_row][new_col] = new_char

    if new_char == CHARS["wall"]:
        return res

    board = write_updates(board, (new_row, new_col), move_mask, new_slice, index + 1)

    return board


def score_it():
    """Calculate score based on 'GPS' weights"""
    # TODO
    return None


def find_robot(board: list[str] | list[list[str]]) -> tuple[int, int] | None:
    char = CHARS["robot"]
    for row_index, row in enumerate(board):
        if char in row:
            return (row_index, row.index(char))

    return None


if __name__ == "__main__":
    print("TODO")
