"""AoC 2024 Day 17 Task 1"""

from dataclasses import dataclass, field

# pylint: disable=E0606
# state = None #pylint: disable=C0103


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
            state.a = state.a // ((2 ** (combo_operands(operand, state))) % 8)
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
            state.b = (state.a // (2 ** combo_operands(1, state))) % 8
        case 7:
            # bdv:
            state.pointer += 2
            state.c = (state.a // (2 ** combo_operands(1, state))) % 8

def print_vm(state):
    print(f"A:{state.a} B:{state.b} C:{state.c} Instruction Pointer: {state.pointer}")

def run_program(program, reg_a=0, reg_b=0, reg_c=0):
    program_length = len(program)
    program_state = MachineState(reg_a, reg_b, reg_c, 0, []) 

    while program_state.pointer < program_length:
        opcode = program[program_state.pointer]
        operand = program[program_state.pointer +1] 
        do_instruction(opcode,operand, program_state)

    return program_state


if __name__ == "__main__":

    pass
