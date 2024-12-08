"""Advent of Code 2024 Day 3 task 1"""

import re
import sys


def open_file(fname):
    """Returns a file handle"""
    try:
        fhand = open(fname, "r", encoding="utf-8")
    except IOError:  # pragma: no cover
        sys.exit()
    return fhand


def find_matches(line):
    """Matches the pattern mul(n,n) with len(n) <= 3"""
    pattern = r"mul\(\d{1,3}\,\d{1,3}\)"
    return re.findall(pattern, line)


def clean_matches(seq):
    """Convert to (n,n)"""
    res = []
    clean_pattern = r"\d{1,3}\,\d{1,3}"
    for item in seq:
        values = re.findall(clean_pattern, item)
        lval, rval = values[0].split(",")
        res.append((int(lval), int(rval)))
    return res


def run_it(fname="data/test/3.txt"):
    """runs the task"""
    res = 0
    fhand = open_file(fname)
    for line in fhand:
        items = clean_matches(find_matches(line))
        for item in items:
            left, right = item
            res += left * right

    return res


if __name__ == "__main__":  # pragma: no cover
    print(run_it("data/input/3.txt"))
