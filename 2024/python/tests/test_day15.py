"""Tests for AoC 2024 Day 12"""

import pytest  # pylint: disable=unused-import
from aoc.day15 import (  # pylint: disable=import-error
    read_file,
    clean_data,
    find_robot,
    parse_move,
    look_ahead,
    do_move,
    score_it,
    board_to_array,
    print_board,
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


def test_board_to_array():
    test_list = ["abc", "123"]

    assert board_to_array(test_list) == [["a", "b", "c"], ["1", "2", "3"]]


# Dataclasses


def test_robot():
    """Test the robot dataclass"""
    robot = Robot(3, 5)

    # ensure slots are enabled
    #TODO fix this
    #assert robot.__slots__ == ("x", "y", "location", "last_move")
    # Test values
    #assert robot.x == 3 and robot.y == 5
    #assert robot.location == (3, 5)


# Game logic


def test_find_robot():
    """Locate the robot on the board"""
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
    # list[str]
    assert find_robot(test1) == (2, 2)
    assert find_robot(test2) == (3, 4)
    # list[list[chr]]
    assert find_robot(board_to_array(test1)) == (2, 2)
    assert find_robot(board_to_array(test2)) == (3, 4)


def test_parse_move():  # pylint: disable=C0116
    # Single char input
    assert parse_move("u") == (-1, 0)
    assert parse_move("d") == (1, 0)
    assert parse_move("l") == (0, -1)
    assert parse_move("r") == (0, 1)
    # Game file chars
    assert parse_move("^") == (-1, 0)
    assert parse_move("v") == (1, 0)
    assert parse_move("<") == (0, -1)
    assert parse_move(">") == (0, 1)
    # word input
    assert parse_move("up") == (-1, 0)
    assert parse_move("down") == (1, 0)
    assert parse_move("left") == (0, -1)
    assert parse_move("right") == (0, 1)


def test_look_ahead():  # pylint: disable=C0116
    """return the chars along a path of travel"""
    test_board = [
        "########",
        "#.@O.O.#",
        "##..O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
    ]
    # Test Right, Left, Down and Up
    assert look_ahead(test_board, (1, 2), (0, 1)) == ["O", ".", "O", "."]
    assert look_ahead(test_board, (1, 2), (0, -1)) == ["."]
    assert look_ahead(test_board, (1, 2), (1, 0)) == [".", "."]
    assert look_ahead(test_board, (1, 2), (-1, 0)) == []


def test_look_ahead_array():  # pylint: disable=C0116
    """return the chars along a path of travel"""
    test_board = [
        "########",
        "#.@O.O.#",
        "##..O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
    ]
    test_board = board_to_array(test_board)
    # Test Right, Left, Down and Up
    assert look_ahead(test_board, (1, 2), (0, 1)) == ["O", ".", "O", "."]
    assert look_ahead(test_board, (1, 2), (0, -1)) == ["."]
    assert look_ahead(test_board, (1, 2), (1, 0)) == [".", "."]
    assert look_ahead(test_board, (1, 2), (-1, 0)) == []


def test_print_board_strings(capsys: pytest.CaptureFixture[str]):
    print_board(["abc", "123"])
    captured = capsys.readouterr()
    assert captured.out == "abc\n123\n"


def test_print_board_array(capsys: pytest.CaptureFixture[str]):
    print_board([["a", "b", "c"], ["1", "2", "3"]])
    captured = capsys.readouterr()
    assert captured.out == "abc\n123\n"


def test_do_move():  # pylint: disable=C0116
    # TODO
    assert do_move(None, None, None) is None


def test_score_it():  # pylint: disable=C0116
    # TODO
    assert score_it() is None
