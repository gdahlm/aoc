"""Tests for AoC 2024 Day 12"""

import pytest            # pylint: disable=unused-import
from aoc.day15 import (  # pylint: disable=import-error
    read_file,
    clean_data,
)

def test_fread_all():
    assert len(read_file('data/test/15_small.txt')) == 10

def test_clean_data():
    assert True
