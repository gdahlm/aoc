"""Tests for AoC 2024 Day 9"""
import pytest
from aoc.day9 import (
    expand_disk,
    main,
)


def test_expand_disk():
    expansion_tests = [
        ['12345', '0..111....22222' ],
        ['2333133121414131402', '00...111...2...333.44.5555.6666.777.888899'],
    ]

    for test in expansion_tests:
        assert expand_disk(test[0]) == test[1]

def test_main():
    with pytest.raises(NotImplementedError) as exc_info:
        main()

    assert exc_info.type is NotImplementedError
