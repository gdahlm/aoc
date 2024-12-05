from aoc.day4task1 import fread_all, valid_move,find_roots,find_frontier,  run_it


def test_fread_all():
    res = list(fread_all("data/test/3.txt"))
    assert (
        res[0]
        == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )

def test_valid_move():
    ROWS, COLS = 10, 10
    assert valid_move(0,0,ROWS, COLS) == True
    assert valid_move(9,9,ROWS, COLS) == True
    assert valid_move(0,10,ROWS, COLS) == False
    assert valid_move(10,0,ROWS, COLS) == False
    assert valid_move(-1,9,ROWS, COLS) == False
    assert valid_move(9,-1,ROWS, COLS) == False

def test_find_roots():
    assert (
        find_roots( [
     '..X...',
     '.SAMX.',
     '.A..A.',
     'XMAS.S',
     '.X....'], 'X' )
        == {(0, 2), (1, 4), (3, 0), (4, 1)}
    )

def test_find_frontier():
    masks = {
    # D:(r,c)
    'N':(-1,0),
    'S':(1,0),
    'E':(0,1),
    'W':(0,-1),
    'NW':(-1,-1),
    'NE':(-1,1),
    'SW':(1,-1),
    'SE':(1,1)}

    all_dirs=masks.keys()

    assert (
        find_frontier(0, 0, 10, 10,directions=all_dirs)
        == {((0, 1), ((0, 0), (0, 1))),
            ((1, 0), ((0, 0), (1, 0))),
            ((1, 1), ((0, 0), (1, 1)))})

def test_run_it():
    assert True
