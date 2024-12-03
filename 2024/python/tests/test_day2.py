from aoc.day2 import (
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

test_file = "data/test/2.txt"

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


def test_open_file():
    expected = [
        "7 6 4 2 1\n",
        "1 2 7 8 9\n",
        "9 7 6 2 1\n",
        "1 3 2 4 5\n",
        "8 6 4 4 1\n",
        "1 3 6 7 9\n",
    ]
    res = list(open_file(test_file))
    assert res == expected


def test_read_file():
    expected = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert list(read_file(test_file)) == expected


def test_compress():
    expected = ["A", "C", "E", "F"]
    assert list(compress("ABCDEF", [1, 0, 1, 0, 1, 1])) == expected


def test_has_duplicates():
    assert has_duplicates([8, 6, 4, 4, 1]) == True
    assert has_duplicates([8, 6, 4, 5, 1]) == False


def test_has_unorder():
    assert has_unorder([1, 3, 2, 4, 5]) == True
    assert has_unorder([8, 6, 4, 5, 1]) == True
    assert has_unorder([1, 2, 3, 4, 5]) == False
    assert has_unorder([5, 4, 3, 2, 1]) == False


def test_has_jump():
    assert has_jump([1, 2, 7, 8, 9]) == True
    assert has_jump([9, 7, 6, 2, 1]) == True
    assert has_jump([7, 6, 4, 2, 1]) == False


def test_check_line():
    assert True
    assert check_line([7, 6, 4, 2, 1]) == True
    assert check_line([1, 3, 6, 7, 9]) == True
    assert check_line([1, 2, 7, 8, 9]) == False
    assert check_line([9, 7, 6, 2, 1]) == False
    assert check_line([1, 3, 2, 4, 5]) == False
    assert check_line([8, 6, 4, 4, 1]) == False


def test_fix_iter():
    assert list(fix_iter(range(3))) == [[1, 2], [0, 2], [0, 1]]


def test_is_fixable():
    assert is_fixable([7, 6, 4, 2, 1]) == True  # Safe without removing any level.
    assert is_fixable([1, 3, 6, 7, 9]) == True  # Safe without removing any level.
    assert is_fixable([1, 3, 2, 4, 5]) == True  # Safe by removing the second level, 3.
    assert is_fixable([8, 6, 4, 4, 1]) == True  # Safe by removing the third level, 4.
    assert (
        is_fixable([1, 2, 7, 8, 9]) == False
    )  # Unsafe regardless of which level is removed
    assert (
        is_fixable([9, 7, 6, 2, 1]) == False
    )  # Unsafe regardless of which level is removed.


def test_task():
    assert task(test_file, 1) == 2
    assert task(test_file, 2) == 4
