from aoc.day5task1 import (
    fread_all,
    find_middle,
    check_line,
    run_it,
    clean_data,
    fix_line,
    find_bad,
    fix_lines,
)

rules = {
    "47": ["53", "13", "61", "29"],
    "97": ["13", "61", "47", "29", "53", "75"],
    "75": ["29", "53", "47", "61", "13"],
    "61": ["13", "53", "29"],
    "29": ["13"],
    "53": ["29", "13"],
}


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


def test_clean_data():
    test1 = ["1|2", "3|4", "", "1,2,3,4"]
    test2 = ["1|2", "1|3", "3|4", "", "1,2,3,4"]
    res1 = ({"1": ["2"], "3": ["4"]}, [["1", "2", "3", "4"]])
    res2 = ({"1": ["2", "3"], "3": ["4"]}, [["1", "2", "3", "4"]])

    assert clean_data(test1) == res1
    assert clean_data(test2) == res2


def test_check_line():
    good = [
        ["75", "47", "61", "53", "29"],
        ["97", "61", "53", "29", "13"],
        ["75", "29", "13"],
    ]
    bad = [
        ["75", "97", "47", "61", "53"],
        ["61", "13", "29"],
        ["97", "13", "75", "29", "47"],
    ]
    for line in good:
        assert check_line(rules, line) == True
    for line in bad:
        assert check_line(rules, line) == False

def find_bad():
    assert find_bad(rules, ["75", "97", "47", "61", "53"]) == ((1, '97'), (0, '75'))

def test_fix_line():
    assert fix_line(rules, ["75", "97", "47", "61", "53"]) == [
        "97",
        "75",
        "47",
        "61",
        "53",
    ]
    assert fix_line(rules, ["61", "13", "29"]) == ["61", "29", "13"]
    assert fix_line(rules, ["97", "13", "75", "29", "47"]) == [
        "97",
        "75",
        "47",
        "29",
        "13",
    ]
def test_fix_lines():
    assert fix_lines('data/test/5.txt') == 123


def test_run_it():
    assert run_it("data/test/5.txt") == 143
