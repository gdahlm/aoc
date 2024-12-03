from aoc.day1task2 import similarity, read_file, run_it


def test_similarity():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    items = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
    res = similarity(left, right)
    assert res == 31


def test_read_file():
    lres, rres = read_file("data/test/1.txt")
    assert lres == [3, 4, 2, 1, 3, 3]
    assert rres == [4, 3, 5, 3, 9, 3]


def test_run_it():
    res = run_it("data/test/1.txt")
    assert res == 31
