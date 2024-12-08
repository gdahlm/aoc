from aoc.day7 import (
    fread_line,
    clean_data,
    cat_op,
    mul_op,
    add_op,
    product,
    ops_iter,
    find_it,
)


def test_fread_line():
    assert True
    # TODO


def test_clean_data():
    assert True
    # TODO


def test_cat_op():
    assert cat_op(11, 17) == 1117
    assert cat_op(12, 34) == 1234


def test_mul_op():
    assert mul_op(2, 10) == 20


def test_add_op():
    assert add_op(2, 10) == 12
    assert True


def test_product():
    assert list(product("ABCD", "xy")) == [
        ("A", "x"),
        ("A", "y"),
        ("B", "x"),
        ("B", "y"),
        ("C", "x"),
        ("C", "y"),
        ("D", "x"),
        ("D", "y"),
    ]
    assert list(product(range(2), repeat=3)) == [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    ]


def test_ops_iter():
    assert ops_iter(3, ops="+*") == [("+", "+"), ("+", "*"), ("*", "+"), ("*", "*")]
    assert ops_iter(4, ops=["a", "b"]) == [
        ("a", "a", "a"),
        ("a", "a", "b"),
        ("a", "b", "a"),
        ("a", "b", "b"),
        ("b", "a", "a"),
        ("b", "a", "b"),
        ("b", "b", "a"),
        ("b", "b", "b"),
    ]


def test_find_it():
    assert find_it('data/test/7.txt', task=1) == 3749
    assert find_it('data/test/7.txt', task=2) == 11387

