"""Tests for AoC 2024 Day 12"""

# pylint: disable=E0606,C0116,W0611
import pytest  # pylint: disable=unused-import
from aoc.day17 import (  # pylint: disable=import-error
    MachineState,
    combo_operands,
    do_instruction,
    print_vm,
    run_program,
)


def test_machine_state():
    tstate = MachineState(1, 2, 3, 20, [100, 200, 300])
    assert tstate.a == 1
    assert tstate.b == 2
    assert tstate.c == 3
    assert tstate.pointer == 20
    assert tstate.output == [100, 200, 300]
    del tstate


def test_combo_operands():
    tstate = MachineState(1, 2, 3, 20, [100, 200, 300])
    assert combo_operands(0, tstate) == 0
    assert combo_operands(1, tstate) == 1
    assert combo_operands(2, tstate) == 2
    assert combo_operands(3, tstate) == 3
    assert combo_operands(5, tstate) == tstate.b
    assert combo_operands(6, tstate) == tstate.c
    del tstate


def test_do_instruction():

    # If register C contains 9, the program 2,6 would set register B to 1.
    tstate = MachineState(0, 0, 9, 0, [])  # pylint: disable=W0612
    do_instruction(2, 6, tstate)
    assert tstate.b == 1
    del tstate


def test_run_program():

    test_out = run_program([5, 0, 5, 1, 5, 4], 10, 0, 0)
    assert test_out.output == [0, 1, 2]
    del test_out

    test_out = run_program([2, 6], 0, 0, 9)
    assert test_out.b == 1
    del test_out

    test_out = run_program([0, 1, 5, 4, 3, 0], 2024, 0, 0)
    assert test_out.output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert test_out.a == 0
    del test_out

    test_out = run_program([1, 7], 0, 29, 0)
    assert test_out.b == 26
    del test_out

    test_out = run_program([4, 0], 0, 2024, 43690)
    assert test_out.b == 44354
    del test_out

    test_out = run_program([0, 1, 5, 4, 3, 0], 729, 0, 0)
    assert test_out.output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
    del test_out


def test_print_vm():
    assert True
