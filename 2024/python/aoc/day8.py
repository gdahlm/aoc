"""AoC 2024 Day 8"""


# File reading and cleaning
def fread_line(filename):
    """Lazy read of file returning a generator"""
    with open(filename, "r", encoding="utf-8") as file_in:
        yield from file_in


def find_antennas(board):
    antennas = {}
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col not in ".#":
                if col not in antennas.keys():
                    antennas[col] = [(r, c)]
                else:
                    antennas[col].append((r, c))
    return antennas


def known_antinodes(board):
    antinodes = {}
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col in "#":
                if col not in antinodes.keys():
                    antinodes[col] = [(r, c)]
                else:
                    antinodes[col].append((r, c))
    return antinodes


def double_distance(ref_point, given_point):
    """
    Finds a point twice as far away from ref_point as given_point.
    """

    x1, y1 = ref_point
    x2, y2 = given_point

    # Calculate the new point's coordinates
    new_x = 2 * x2 - x1
    new_y = 2 * y2 - y1

    return new_x, new_y


def find_antinodes(board, antennas):
    pass
    # TODO
