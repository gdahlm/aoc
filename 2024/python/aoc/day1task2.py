def similarity(left, right):
    res = 0
    items = set(left).intersection(set(right))
    for item in items:
        res += left.count(item) * item * right.count(item)

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
    return similarity(lvalues, rvalues)


if __name__ == "__main__":
    print(run_it("data/input/1.txt"))  # pragma: no cover
