from aoc.day3task2 import open_file,find_matches,clean_matches,run_it


def test_open_file():
    res = list(open_file('data/test/3_2.txt'))
    assert res == ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n"]

def test_find_matches():
    line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected = ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']
    assert find_matches(line) == expected

def test_clean_matches():
    sequence = ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']
    expected = [(2, 4), (False, False), (5, 5), (11, 8), (True, True), (8, 5)]
    assert clean_matches(sequence) == expected
    assert True

def test_run_it():
    res = run_it('data/test/3_2.txt')
    assert res == 48
    #assert True
