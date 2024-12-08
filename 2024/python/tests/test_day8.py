from aoc.day8 import (
    fread_line,
    find_antennas,
    find_antinodes,
    known_antinodes,
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
    assert find_antennas(test) == {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8), (9, 9)]}
    assert find_antennas(test_2) == {'a': [(3, 4), (5, 5)]}

def test_find_known_antinodes():
    assert known_antinodes(test_2) == {'#': [(1, 3), (7, 6)]}

def test_find_antinodes():
    assert True
    # TODO
