from aoc.day3task1 import (
    open_file,
    read_file,
    compress,
    has_duplicates,
    has_unorder,
    has_jump,
    check_line,
    fix_iter,
    is_fixable,
    task,
)


# Test data
SAFE = [
    [7, 6, 4, 2, 1],
    [1, 3, 6, 7, 9],
]
UNSAFE = [
    [1, 2, 7, 8, 9],  # Unsafe because 2 7 is an increase of 5.
    [9, 7, 6, 2, 1],  # Unsafe because 6 2 is a decrease of 4.
    [1, 3, 2, 4, 5],  # Unsafe because 1 3 is increasing but 3 2 is decreasing.
    [8, 6, 4, 4, 1],  # Unsafe because 4 4 is neither an increase or a decrease.
]
SAFE2 = [
    [7, 6, 4, 2, 1],  # Safe without removing any level.
    [1, 3, 6, 7, 9],  # Safe without removing any level.
    [1, 3, 2, 4, 5],  # Safe by removing the second level, 3.
    [8, 6, 4, 4, 1],  # Safe by removing the third level, 4.
]
UNSAFE2 = [
    [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed
    [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed.
]


def open_file():
    assert True


def read_file():
    assert True


def compress():
    assert True


def has_duplicates():
    assert True


def has_unorder():
    assert True


def has_jump():
    assert True


def check_line():
    assert True


def fix_iter():
    assert True


def is_fixable():
    assert True


def task():
    assert True
