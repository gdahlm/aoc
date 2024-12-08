from aoc.day8 import (
    fread_line,
    product,
    find_antennas,
    find_antinodes,
    known_antinodes,
    valid_point,
    double_distance,
)

test = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]

test_2 = [
    "..........",
    "...#......",
    "..........",
    "....a.....",
    "..........",
    ".....a....",
    "..........",
    "......#...",
    "..........",
    "..........",
]

test_3 = [
    "..........",
    "...#......",
    "#.........",
    "....a.....",
    "........a.",
    ".....a....",
    "..#.......",
    "......#...",
    "..........",
    "..........",
]


def test_fread_line():
    assert True
    # TODO


def test_find_antennas():
    assert find_antennas(test) == {
        "0": [(1, 8), (2, 5), (3, 7), (4, 4)],
        "A": [(5, 6), (8, 8), (9, 9)],
    }
    assert find_antennas(test_2) == {"a": [(3, 4), (5, 5)]}


def test_find_known_antinodes():
    assert known_antinodes(test_2) == {"#": [(1, 3), (7, 6)]}


def test_double_distance():
    assert double_distance((5, 5), (3, 4)) == (1, 3)
    assert double_distance((3, 4), (5, 5)) == (7, 6)


def test_valid_move():
    assert True
    # TODO


def test_find_antinodes():
    tdata = [x.strip() for x in fread_line("data/test/8.txt")]
    res = find_antinodes(find_antennas(tdata), tdata)
    assert res == 14
