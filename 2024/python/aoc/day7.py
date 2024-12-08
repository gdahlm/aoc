"""AoC day 7"""


# File reading and cleaning
def fread_line(filename):
    """Lazy read of file returning a generator"""
    with open(filename, "r", encoding="utf-8") as file_in:
        yield from file_in


def clean_data(filename="data/test/7.txt"):
    """return tuples with int values"""
    for line in fread_line(filename):
        head, tail = line.split(":")
        tail = tail.split()
        yield (int(head), [int(x) for x in tail])


# These are to help with operator permutations
def cat_op(left: int, right: int) -> int:
    """Concat two ints, returning an int"""
    return int(str(left) + str(right))


def add_op(left: int, right: int) -> int:
    """Adds two ints, returning an int"""
    return left + right


def mul_op(left: int, right: int) -> int:
    """Multiplies two ints, returning an int"""
    return left * right


# To avoid imports, copy of tertools.product
def product(*iterables, repeat=1):
    """
    product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
    """

    if repeat < 0:
        raise ValueError("repeat argument cannot be negative")
    pools = [tuple(pool) for pool in iterables] * repeat

    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)


def ops_iter(cols, ops):
    """wrapper for product() due to some current jupyter bugs"""
    return list(product(ops, repeat=cols - 1))


# core code
def find_it(filename="/data/test/7.txt", task=2):
    """core function"""
    res = []
    data = list(clean_data(filename))
    ops_dict = [add_op, mul_op]
    if task == 2:
        ops_dict.append(cat_op)

    for line in data:
        target, arr = line
        _, left, cols = 0, arr[0], len(arr)

        ops = ops_iter(cols, ops_dict)

        for op in ops:
            total = left
            for index, right in enumerate(arr[1:]):
                total = op[index](total, right)
            if total == target:
                _ = total
                break
        res.append(_)
    return sum(res)
