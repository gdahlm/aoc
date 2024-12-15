"""Tests for AoC 2024 Day 12"""

import pytest  # pylint: disable=unused-import
from aoc.day15 import (  # pylint: disable=import-error
    read_file,
    clean_data,
    parse_move,
    look_ahead,
    move_boxes,
    score_it,
)


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


def test_parse_move():
    # TODO
    assert parse_move(None) is None


def test_look_ahead():
    # TODO
    assert look_ahead(None, None) is None


def test_move_boxes():
    # TODO
    assert move_boxes() is None


def test_score_it():
    # TODO
    assert score_it() is None
