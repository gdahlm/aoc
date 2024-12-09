"""Tests for AoC 2024 Day 9"""
import pytest
from aoc.day9 import ( # pylint: disable=import-error
    expand_disk,
    calculate_checksum,
    main,
)


def test_expand_disk():
    expansion_tests = [
        ['12345', '0..111....22222' ],
        ['2333133121414131402', '00...111...2...333.44.5555.6666.777.888899'],
    ]

    for test in expansion_tests:
        assert expand_disk(test[0]) == test[1]

def test_calculate_checksum():
    data = '0099811188827773336446555566..............'
    res = 1928

    assert calculate_checksum(data) == res


def test_main():
    with pytest.raises(NotImplementedError) as exc_info:
        main()

    assert exc_info.type is NotImplementedError
