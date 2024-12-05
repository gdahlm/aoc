"""
AoC 2024 Day 4 task 1
"""

import re

words = ["XMAS"]
test = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
test1 = ["123456789", "123456789", "123456789", "123456789", "123456789"]
test2 = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

masks = {
    # D:(r,c)
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NW": (-1, -1),
    "NE": (-1, 1),
    "SW": (1, -1),
    "SE": (1, 1),
}

all_dirs = masks.keys()
# directions = ['N','S','E','W','NW','NE','SE','SW']


def fread_all(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def valid_move(r, c, ROWS, COLS):
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
        return False

    return True


def find_roots(board, letter):
    """Return (col, row) tuples for all maches"""
    pattern = re.compile(letter)
    res = set()
    for index, row in enumerate(board):
        for match in pattern.finditer(row):
            res.add((index, match.start()))
    return set(res)


def find_frontier(r, c, ROWS, COLS, directions=all_dirs):
    """Find frontiers within the confines of the board.

    Keyword arguments:
    r -- the row address of the origin
    c -- the column address of the origin
    ROWS -- length of rows
    COLS -- length of columns
    directions == dictionary of "name":(r_mask,c_mask)" e.g. "{"N": (-1, 0)}""

    Returns, set of tuple of the form ((r_mask,c_mask), (path))
              where (path) will be a tuple sequence of (c,r)
    """
    res = set()
    for direction in directions:
        row_mask, col_mask = masks[direction]
        tr, tc = r + row_mask, c + col_mask
        if tr < 0 or tc < 0 or tr >= ROWS or tc >= COLS:
            pass
        else:
            path = ((r, c), (tr, tc))
            res.add((masks[direction], path))
    return set(res)


def find_word(board, word, frontiers, acc=''):


def run_it():
    pass
