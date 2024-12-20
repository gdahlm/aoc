"""AoC 2024 Day 17 Task 1"""

from dataclasses import dataclass, field

# pylint: disable=E0606,E0601


def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def clean_data(filename):
    raw_data = read_file(filename)
    for line in raw_data:
        if line != "":
            _, value = line.split(": ")
            if _[-1] == "A":
                _a = value
            elif _[-1] == "B":
                _b = value
            elif _[-1] == "C":
                _c = value
            elif _[-1] == "m":
                program = value

    return ([int(x) for x in program.split(",")], _a, _b, _c)


@dataclass(slots=True)
class MachineState:
    """Generic point data object"""

    # registers
    a: int
    b: int
    c: int
    # instruction pointer
    pointer: int
    # output
    output: list[int] = field(default_factory=list)


def combo_operands(operand: int, state: object) -> int:
    match operand:
        case 0 | 1 | 2 | 3 as n:
            return int(n)
        case 4:
            return state.a
        case 5:
            return state.b
        case 6:
            return state.c
        case 7:
            raise ValueError("Combo Operand (7) is Reserved")
        case _:
            raise ValueError("Combo Operand is out of range")


def do_instruction(opcode: int, operand: int, state: object):
    match opcode:
        case 0:
            # adv:
            state.pointer += 2
            state.a = state.a // 2 ** combo_operands(operand, state)
        case 1:
            # bxl:
            state.pointer += 2
            state.b = state.b ^ operand
        case 2:
            # bst
            state.pointer += 2
            state.b = combo_operands(operand, state) % 8
        case 3:
            # jnz:
            if state.a == 0:
                state.pointer += 2
            else:
                state.pointer = operand
        case 4:
            # bxc:
            state.pointer += 2
            state.b = state.b ^ state.c
        case 5:
            # out:
            state.pointer += 2
            state.output.append(combo_operands(operand, state) % 8)
        case 6:
            # bdv:
            state.pointer += 2
            state.b = state.a // 2 ** combo_operands(operand, state)
        case 7:
            # bdv:
            state.pointer += 2
            state.c = state.a // 2 ** combo_operands(operand, state)


def print_vm(state):
    print(f"A:{state.a} B:{state.b} C:{state.c} Instruction Pointer: {state.pointer}")


def run_program(program, reg_a=0, reg_b=0, reg_c=0):
    program_length = len(program)
    program_state = MachineState(reg_a, reg_b, reg_c, 0, [])

    while program_state.pointer < program_length:
        opcode = program[program_state.pointer]
        operand = program[program_state.pointer + 1]
        do_instruction(opcode, operand, program_state)
    return program_state


if __name__ == "__main__":

    # Part 1
    input_program, a, b, c = clean_data("data/input/17.txt")
    print(run_program(input_program, int(a), int(b), int(c)))

    # Part 2
    # I cannot figure out a way to code this without giving away the input.
    # But this is all one needs to udnerstand to solve it.
    """
    oct(A): 0o36414027 mod8:7
    oct(A): 0o3641402 mod8:2
    oct(A): 0o364140 mod8:0
    oct(A): 0o36414 mod8:4
    oct(A): 0o3641 mod8:1
    oct(A): 0o364 mod8:4
    oct(A): 0o36 mod8:6
    oct(A): 0o3 mod8:3
    oct(A): 0o0 mod8:0
    """
