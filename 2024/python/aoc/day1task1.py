def distance(left, right):
    return abs(left - right)


def total_distance(left, right):
    res = 0
    left.sort()
    right.sort()
    for index in range(len(left)):
        res += distance(left[index], right[index])

    return res


def read_file(fname):
    with open(fname) as f:
        lines = f.read().splitlines()
    left = []
    right = []
    for line in lines:
        lval, rval = line.split()
        left.append(int(lval))
        right.append(int(rval))
    return (left, right)


def run_it(fname):
    lvalues, rvalues = read_file(fname)
    return total_distance(lvalues, rvalues)


if __name__ == "__main__":
    print(run_it("data/input/1.txt")) # pragma: no cover
