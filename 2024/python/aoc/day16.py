"""AoC 2024 Day 15 Task 1"""

from dataclasses import dataclass, field

# Constents
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
