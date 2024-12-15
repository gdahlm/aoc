"""AoC 2024 Day 15 Task 1"""

from dataclasses import dataclass

GPS_VALUE = ()
CHARS = {
    'robot':'@',
    'box':'O',
    'wall':'#',
    'empty':'.',
}

@dataclass
class Point:
    """Generic point data object"""

    x: int
    y: int


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


def parse_move(move: chr) -> tuple:
    """Return move tuple"""
    match move:
        case "^" | 'up' | 'u':
            print("Up")
            return (-1, 0)
        case "v" | 'down' | 'd':
            print("Down")
            return (1, 0)
        case ">" | 'right' | 'r':
            print("Right")
            return (0, 1)
        case "<" | 'left' | 'l':
            print("Left")
            return (0, -1)


def look_ahead(location: tuple, move_mask: tuple):
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


if __name__ == "__main__":
    print("TODO")
