"""AoC Day 6 task 1"""

masks = {
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
}
cur = (None, None)
visited = []


def fread_all(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def init_start(board):
    """Returns the current location and the inital visted list"""
    for index, line in enumerate(board):
        if "^" in line:
            cur = (index, line.index("^"))
            return cur, "^", [list(cur)]

    return False


def valid_move(board, r, c):
    ROWS, COLS = len(board), len(board[0])
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
        return "WIN"
    elif board[r][c] != "." and board[r][c] != "^":
        return "turn"

    return "true"


def move(board, cur, cur_dir, visited=[], turns=0):
    ROWS, COLS = len(board), len(board[0])
    next_turn = list(masks.keys())
    r_mask, c_mask = masks[cur_dir]
    r, c = cur
    new_r, new_c = r + r_mask, c + c_mask
    visited.append(cur)
    print("New loc:", (new_r, new_c), "Cur loc:", cur)
    valid = valid_move(board, new_r, new_c)
    print("valid_move out: ", valid)

    if valid == "true":
        turns = 0
        move(board, (new_r, new_c), cur_dir, visited, turns)
    elif valid == "turn" and turns < 4:
        new_dir = next_turn[next_turn.index(cur_dir) - 1]
        move(board, cur, new_dir, visited, turns + 1)
    elif valid == "WIN":
        return (valid, len(visited))
    elif turns >= 4:
        return (valid, len(visited))
    else:
        return (False, len(visited))

    return ("Error", visited)


##### UGLY version due to recursion


def do_move(board, cur, cur_dir):
    ROWS, COLS = len(board), len(board[0])
    next_turn = list(masks.keys())
    found = False
    is_cycle = False
    turns, count = 0, 0
    visited = []
    visited_dir = set()
    corners = set()

    while (not found) and (count < 100000) and not is_cycle:
        count += 1
        r, c = cur
        r_mask, c_mask = masks[cur_dir]
        new_r, new_c = r + r_mask, c + c_mask
        visited.append(cur)
        if (new_r, new_c, cur_dir) in visited_dir:
            is_cycle = True
            break
        visited_dir.add((r, c, cur_dir))
        is_valid = valid_move(board, new_r, new_c)

        if is_valid == "true":
            # visited.append(cur)
            turns = 0
            cur = (new_r, new_c)
            continue
        elif is_valid == "turn" and turns < 4:
            cur_dir = next_turn[next_turn.index(cur_dir) - 1]
            corners.add(cur)
            turns += 1
        elif is_valid == "WIN":
            visited.append(cur)
            found = True
            break
        elif turns >= 4:
            found = True
            break

    return visited


def to_array(board):
    res = []
    for row in board:
        res.append([x for x in row])

    return res


def to_string(board):
    res = []
    for row in board:
        res.append("".join(row))
    return res


def add_obs(board, r, c):
    _ = to_array(board)
    _[r][c] = "#"
    return to_string(_)


def brute_two(filename, path):
    board = fread_all(filename)
    count = 0
    for loc in path:
        o_r, o_c = loc
        cur, cur_dir, _ = init_start(board)
        if do_move(add_obs(board, o_r, o_c), cur, cur_dir):
            count += 1
    return count


"""Notes
In [300]: board = fread_all('data/test/6.txt')
     ...: cur, cur_dir, _  = init_start(board)
     ...: do_move(add_obs(board,6,3), cur, cur_dir)


board = fread_all('data/input/6.txt')
cur, cur_dir, _  = init_start(board)
visited = []
move(board, cur, cur_dir, visited,turns = 0)



masks = {}
'^':(-1,0),
'>':(0,1),
'<':(0,-1),
'v':(1,0)}

"""
