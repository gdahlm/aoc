"""AoC 2024 Day 15 Task 1"""

from dataclasses import dataclass, field

# Constents
GPS_VALUE = ()
CHARS = {
    'robot':'@',
    'box':'O',
    'wall':'#',
    'empty':'.',
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
    x: int = field(repr=False)
    y: int = field(repr=False)
    location: tuple[int, int] = field(init=False)
    last_move: str = field(default=None)
    def __post_init__(self):
        self.location = (self.x , self.y)

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
            case x if "#" in line:  # pylint: disable=W0612
                board.append(line)
            case _:
                moves.append(line)
    return board, moves


def parse_move(move: chr) -> tuple[int, int]:
    """Return move mask tuple"""
    match move:
        case "^" | 'up' | 'u':
            return (-1, 0)
        case "v" | 'down' | 'd':
            return (1, 0)
        case ">" | 'right' | 'r':
            return (0, 1)
        case "<" | 'left' | 'l':
            return (0, -1)
    return None


def look_ahead(board:list[str], location: tuple[int, int], move_mask: tuple[int, int]):
    """See if boxes can move"""
    # TODO
    return None


def move_boxes():
    """Move boxes"""
    # TODO
    return None


def score_it():
    """Calculate score based on 'GPS' weights"""
    # TODO
    return None

def find_robot(board: list[str]) -> tuple[int, int] | None:
    char = CHARS['robot']
    for row_index, row in enumerate(board):
        if char in row:
            return ((row_index, row.index(char)))

    return None


if __name__ == "__main__":
    print("TODO")
