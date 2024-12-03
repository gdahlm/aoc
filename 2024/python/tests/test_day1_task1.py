from aoc.day1task1 import distance,total_distance,read_file,run_it

def test_distance():
    distances = [
        (1,3,2),
        (2,3,1),
        (3,3,0),
        (3,4,1),
        (3,5,2),
        (4,9,5)
    ]
    for item in distances:
        left, right, answer = item
        res = distance(left, right)
        assert res == answer


def test_total_distance():
    left = [3,4,2,1,3,3]
    right = [4,3,5,3,9,3]
    res =total_distance(left, right)
    assert res == 11


def test_read_file():
    lres, rres = read_file('data/test/1.txt')
    assert lres == [3,4,2,1,3,3]
    assert rres == [4,3,5,3,9,3]

def test_run_it():
    res = run_it('data/test/1.txt')
    assert res == 11
