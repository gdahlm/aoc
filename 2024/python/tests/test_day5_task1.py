from aoc.day5task1 import fread_all, find_middle


def test_fread_all():
    res = list(fread_all("data/test/3.txt"))
    assert (
        res[0]
        == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )


def test_find_middle():
    test = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]
    answers = [61, 53, 29]

    for index, item in enumerate(test):
        _ = find_middle(item)
        assert item[_] == answers[index]


def test_run_it():
    assert True
