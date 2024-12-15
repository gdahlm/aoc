"""Tests for AoC 2024 Day 12"""

import pytest  # pylint: disable=unused-import
from aoc.day15 import (  # pylint: disable=import-error
    read_file,
    clean_data,
    find_robot,
    parse_move,
    look_ahead,
    move_boxes,
    score_it,
    Robot,
)

# Data Handling
def test_fread_all():
    """Test file reading"""
    raw_input = read_file("data/test/15_small.txt")
    assert len(raw_input) == 10
    assert raw_input[1] == "#..O.O.#"


def test_clean_data():
    """Test file parsing"""
    board, moves = clean_data("data/test/15_small.txt")
    assert moves == ["<^^>>>vv<v>>v<<"]
    assert board[1] == "#..O.O.#"
    assert len(board) == 8 and len(board[0]) == 8

def test_find_robot():
    test1 = [
        "########",
        "#..O.O.#",
        "##@.O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
    ]
    test2 = [
        "########",
        "#....OO#",
        "##.....#",
        "#...@O.#",
        "#.#.O..#",
        "#...O..#",
        "#...O..#",
        "########",
    ]
    assert find_robot(test1) == (2, 2)
    assert find_robot(test2) == (3, 4)

# Dataclasses

def test_Robot():
    """Test the robot dataclass"""
    test_robot = Robot(3,5)

    assert test_robot.__slots__ == ('x', 'y', 'location', 'last_move')
    assert test_robot.x == 3 and test_robot.y == 5
    assert test_robot.location == (3,5)

def test_parse_move(): #pylint: disable=C0116
    assert parse_move('u') == (-1, 0)
    assert parse_move('d') == (1, 0)
    assert parse_move('l') == (0, -1)
    assert parse_move('r') == (0, 1)

    assert parse_move('^') == (-1, 0)
    assert parse_move('v') == (1, 0)
    assert parse_move('<') == (0, -1)
    assert parse_move('>') == (0, 1)

    assert parse_move('up') == (-1, 0)
    assert parse_move('down') == (1, 0)
    assert parse_move('left') == (0, -1)
    assert parse_move('right') == (0, 1)



def test_look_ahead(): #pylint: disable=C0116
    # TODO
    assert look_ahead(None, None, None) is None


def test_move_boxes(): #pylint: disable=C0116
    # TODO
    assert move_boxes() is None


def test_score_it():    #pylint: disable=C0116
    # TODO
    assert score_it() is None
