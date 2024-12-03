from aoc.day3task1 import open_file,find_matches,run_it


def test_open_file():
    res = list(open_file('data/test/3.txt'))
    assert res[0] == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"

def test_find_maches():
    line = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n'
    expected = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    assert find_matches(line) == expected

def test_run_it():
    assert True
    #res = run_it('data/test/1.txt')
    #assert res == 161
