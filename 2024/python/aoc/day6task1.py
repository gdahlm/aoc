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
    elif board[r][c] != ".":
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

    if valid == "true":
        move(board, (new_r, new_c), cur_dir, visited, turns=0)
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


"""Notes

board = fread_all('data/input/6.txt')
cur = (6, 4)
cur, cur_dir, visited = init_start(board)
move(board, cur, cur_dir, [],turns = 0)



masks = {}
'^':(-1,0),
'>':(0,1),
'<':(0,-1),
'v':(1,0)}

"""
