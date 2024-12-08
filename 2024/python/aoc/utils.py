"""Collection of common utility functions"""

### File reading


def fread_all(file_path):
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def fread_line(file_path):
    """Lazy read of file returning a generator"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        yield from file_in


### Board functions


def frontier(board, directions=None):
    rows, cols = len(board), len(board[0])
    masks = {
        # D:(r,c)
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
        "NW": (-1, -1),
        "NE": (-1, 1),
        "SW": (1, -1),
        "SE": (1, 1),
    }
    if directions is None:
        directions = masks.keys()

    def is_valid(point):
        r, c = point
        if 0 <= r < rows and 0 <= c < cols:
            return True
        return False

    def points(point, directions=directions):
        r, c = point
        res = set()
        for key in directions:
            r_off, c_off = masks[key]
            r_new, c_new = r + r_off, c + c_off
            if is_valid((r_new, c_new)):
                res.add((r + r_off, c + c_off))
        return list(res)

    return points
