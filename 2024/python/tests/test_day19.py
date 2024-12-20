"""Tests for AoC 2024 Day 19"""

# pylint: disable=E0606,C0116,W0611
import pytest  # pylint: disable=unused-import
from aoc.day19 import (  # pylint: disable=import-error
    read_file,
    clean_data,
    can_construct,
    count_construct,
    solution,
)

test_filename = "data/test/19.txt"  # pylint: disable=invalid-name

# Load data
towels, patterns = clean_data(test_filename)


def test_read_file():
    assert read_file(test_filename)


def test_clean_data():
    assert isinstance(towels, list)
    assert isinstance(towels[0], str)
    assert isinstance(patterns, list)
    assert isinstance(patterns[0], str)


def test_can_construct():
    assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
    assert not can_construct("abcxdef", ["ab", "abc", "cd", "def", "abcd"])


def test_count_construct():
    assert count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert count_construct("abzcdef", ["ab", "abc", "cd", "def", "abcd"]) == 0


def test_solution():
    task1, task2 = solution(test_filename)
    assert task1 == 6
    assert task2 == 16
