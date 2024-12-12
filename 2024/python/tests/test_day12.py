"""Tests for AoC 2024 Day 12"""

import pytest            # pylint: disable=unused-import
from aoc.day12 import (  # pylint: disable=import-error
    main,
)

### Test data

test_garden = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",]

# Char, (area, perimeter, area*perimeter); Total=1930
test_garden_values = [
    ["R", (12, 18, 216)],
    ["I", (4, 8, 32)],
    ["C", (14, 28, 392)],
    ["F", (10, 18, 180)],
    ["V", (13, 20, 260)],
    ["J", (11, 20, 220)],
    ["C", (1, 4, 4)],
    ["E", (13, 18, 234)],
    ["I", (14, 22, 308)],
    ["M", (5, 12, 60)],
    ["S", (5, 12, 60)],]


def test_main():
    assert main() is None
    # TODO
