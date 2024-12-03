"""AoC 2024 Day 1 Task 1"""
def distance(left, right):
    """simple distance function"""
    return abs(left - right)


def total_distance(left, right):
    """count the total distance across inputs"""
    res = 0
    left.sort()
    right.sort()
    for index, _ in enumerate(left):
        res += distance(_, right[index])

    return res


def read_file(fname):
    """Reads the file and returns two lists"""
    with open(fname, encoding="utf-8") as f:
        lines = f.read().splitlines()
    left = []
    right = []
    for line in lines:
        lval, rval = line.split()
        left.append(int(lval))
        right.append(int(rval))
    return (left, right)


def run_it(fname):
    """task running funciton"""
    lvalues, rvalues = read_file(fname)
    return total_distance(lvalues, rvalues)


if __name__ == "__main__":
    print(run_it("data/input/1.txt"))  # pragma: no cover
