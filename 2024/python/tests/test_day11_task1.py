"""Tests for AoC 2024 Day 11"""
import pytest
from aoc.day11_task1 import (  # pylint: disable=import-error
    main,
    stone_action,
    do_blink,
    do_blinks,
    count_stones,
)


def test_main():
    with pytest.raises(NotImplementedError) as exc_info:
        main()

    assert exc_info.type is NotImplementedError

def test_stone_action():
    input_output = [
        ['0','1'],
        ['10', '1 0'],
        ['12', '1 2'],
        ['99', '9 9'],
        ['1002', '10 2'],
        ['1020', '10 20'],
        ['999', '2021976']
    ]

    for values in input_output:
        assert stone_action(values[0]) == values[1]


def test_do_blink():
    test_seq = [
        "125 17",
        "253000 1 7",
        "253 0 2024 14168",
        "512072 1 20 24 28676032",
        "512 72 2024 2 0 2 4 2867 6032",
        "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32",
        "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2",
    ]
    
    for index in range(len(test_seq)-1):
        assert do_blink(test_seq[index]) == test_seq[index+1]

def test_count_stones():
    assert count_stones(25, "125 17" ) == 55312   

def test_do_blinks():
    test_input = "125 17"
    test_output = "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
    num_blinks = 6
    assert do_blinks(6, test_input) == test_output
