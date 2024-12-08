"""AoC 2024 Day 8"""


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


# File reading and cleaning
def fread_line(filename):
    """Lazy read of file returning a generator"""
    with open(filename, "r", encoding="utf-8") as file_in:
        yield from file_in


def find_antennas(board):
    antennas = {}
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col not in ".#":
                if col not in antennas.keys():
                    antennas[col] = [(r, c)]
                else:
                    antennas[col].append((r, c))
    return antennas


def double_distance(ref_point, given_point):
    """
    Finds a point twice as far away from ref_point as given_point.
    """

    x1, y1 = ref_point
    x2, y2 = given_point

    # Calculate the new point's coordinates
    new_x = 2 * x2 - x1
    new_y = 2 * y2 - y1

    return new_x, new_y


def valid_point(point, board):
    ROWS, COLS = len(board), len(board[0])
    r, c = point
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
        return False
    return True


def find_antinodes(antennas, board):
    res = set()
    for key in antennas:
        pairs = list(product(antennas[key], repeat=2))
        for pair in pairs:
            left, right = pair
            if left == right:
                continue
            else:
                _ = double_distance(left, right)
                if valid_point(_, board):
                    res.add(_)
                _ = double_distance(right, left)
                if valid_point(_, board):
                    res.add(_)
    return len(res)


# rdata = [x.strip() for x in fread_line('data/input/8.txt')]
# test_it(find_antennas(rdata), rdata)
