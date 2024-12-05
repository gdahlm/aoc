"""Advent of Code 2024 Day 3 task 2"""
import re
import sys

# File handling
def open_file(fname):
    """Opens the file and returns a file handle, not robust but easy for thsi task"""
    try:
        fhand = open(fname, "r", encoding="utf-8")
    except IOError:  # pragma: no cover
        sys.exit()
    return fhand


def find_matches(line):
    """Matches the task patterns of mul(###,###) or do() or don't()"""
    pattern = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)"
    return re.findall(pattern, line)


def clean_matches(seq):
    """#converts the text form of mul(n,n) to a tuple (n,n) or bools for do() don't()"""
    res = []
    clean_pattern = r"\d{1,3}\,\d{1,3}"
    for item in seq:
        if item == "do()":
            res.append((True, True))
        elif item == "don't()":
            res.append((False, False))
        else:
            values = re.findall(clean_pattern, item)
            lval, rval = values[0].split(",")
            res.append((int(lval), int(rval)))
    return res


def run_it(fname="data/test/3.txt"):
    """Runs the task code"""
    res = 0
    fhand = open_file(fname)
    do_math = True
    for line in fhand:
        items = clean_matches(find_matches(line))
        for item in items:
            left, right = item
            if left in (True,False):
                do_math = left
            elif do_math is True:
                res += left * right

    return res


if __name__ == "__main__":  # pragma: no cover
    print(run_it("data/input/3.txt"))
