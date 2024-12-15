"""Tests for AoC 2024 Day 12"""

import pytest            # pylint: disable=unused-import
from aoc.day15 import (  # pylint: disable=import-error
    read_file,
    clean_data,
)

def test_fread_all():
    """Test file reading"""
    raw_input = read_file('data/test/15_small.txt')
    assert len(raw_input) == 10
    assert raw_input[1] == '#..O.O.#'

def test_clean_data():
    """Test file parsing"""
    board, moves = clean_data('data/test/15_small.txt')
    assert moves == ['<^^>>>vv<v>>v<<']
    assert board[1] == '#..O.O.#'
    assert len(board) == 8 and len(board[0]) == 8