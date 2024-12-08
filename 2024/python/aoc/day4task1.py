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


def find_word(r, c, board, word, mask):
    ROWS, COLS = len(board), len(board[0])
    path = []
    res = ""
    for index, letter in enumerate(word):
        # if index == len(word)-1:
        #   return True
        (r_mask, c_mask) = mask
        r_shift, c_shift = r_mask * index, c_mask * index
        r_new, c_new = r + r_shift, c + c_shift
        path.append((r_new, c_new))
        if valid_move(r_new, c_new, ROWS, COLS):
            if board[r_new][c_new] != word[index]:
                return False
    for index, (row, col) in enumerate(path):
        if valid_move(row, col, ROWS, COLS):
            res = res + board[row][col]
    if res == word:
        return True

    return path


def find_x_mas(board):
    ROWS, COLS = len(board), len(board[0])
    check, res = set(["M", "S"]), 0
    for r, row in enumerate(board):
        if r > 0 and r < ROWS - 1:
            for c, chars in enumerate(row):
                if c > 0 and c < COLS - 1 and board[r][c] == "A":
                    f = set([board[r - 1][c - 1], board[r + 1][c + 1]])
                    b = set([board[r + 1][c - 1], board[r - 1][c + 1]])
                    if check == f and check == b:
                        res += 1
    return res


def run_it():
    pass
