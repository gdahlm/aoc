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


def fread_line(filename):
    """Lazy read of file returning a generator"""
    with open(filename, "r", encoding="utf-8") as file_in:
        yield from file_in


def valid_point(point, board):
    rows, cols = len(board), len(board[0])
    r, c = point
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


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


def known_antinodes(board):
    antinodes = {}
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col in "#":
                if col not in antinodes.keys():
                    antinodes[col] = [(r, c)]
                else:
                    antinodes[col].append((r, c))
    return antinodes


def double_distance(point1, point2):
    """
    Finds a point twice as far away from point1 as point2.
    """
    r1, c1 = point1
    r2, c2 = point2

    # Calculate the new point's coordinates
    new_r = 2 * r2 - r1
    new_c = 2 * c2 - c1

    return new_r, new_c


def to_array(board):
    res = []
    for row in board:
        res.append(list(row))

    return res


def to_string(board):
    res = []
    for row in board:
        res.append("".join(row))
    return res


def draw_it(antennas, points, board):
    board = to_array(board)
    for point in points:
        r, c = point
        board[r][c] = "#"
    for antenna in antennas:
        for point in antennas[antenna]:
            r, c = point
            board[r][c] = antenna
    return to_string(board)


def get_ray(point1, point2, board, points=None):
    if points is None:
        points = set
    points.add(point1)
    points.add(point2)
    rows, cols = len(board), len(board[0])
    new_point = double_distance(point1, point2)
    r, c = new_point
    if r >= 0 and r < rows and c >= 0 and c < cols:
        points.add(new_point)
        get_ray(point2, new_point, board, points)

    return points


def test_it(antennas, board):
    res = set()
    for key in antennas:
        res = set()
        pairs = list(product(antennas[key], repeat=2))
        for pair in pairs:
            left, right = pair
            if left == right:
                continue

            res = res.union(get_ray(left, right, board))

    return res


def run_it(board, total=None):
    if total is None:
        total = set
    antennas = find_antennas(board)
    total = total.union(test_it(antennas, board))
    for antenna in antennas:
        total = total.union(antennas[antenna])
    return len(total)
