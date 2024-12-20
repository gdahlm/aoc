"""AoC 2024 Day 16 Task 1

Start Tile (marked S) facing East 
End Tile (marked E)

Points
forward = 1
turn left or right = 1000

look for lowest score.

"""

from dataclasses import dataclass, field

# Constents
test_start = (13, 1)
test_end = (1, 13) 
test_map = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############",
]

# Dataclases


@dataclass
class Point:
    """Generic point data object"""

    x: int
    y: int


# File handling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


if __name__ == "__main__":
    print("TODO")
