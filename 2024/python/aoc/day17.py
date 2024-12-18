"""AoC 2024 Day 17 Task 1"""
from dataclasses import dataclass, field

@dataclass(slots=True)
class MachineState:
    """Generic point data object"""
    # registers
    a: int
    b: int
    c: int
    #instruction pointer
    pointer: int
    #output
    output: list[int] = field(default_factory=list)


def combo_operands(operand:int) -> int:
    match operand:
        case 0| 1 | 2 | 3 as n:
            return int(n)
        case 4:
            return state.a
        case 5:
            return state.b
        case 6:
            return state.c
        case 7:
            raise ValueError('Combo Operand (7) is Reserved')
        case _:
            raise ValueError('Combo Operand is out of range')

def do_instruction(opcode:int, operand:int):
    match opcode:
        case 0:
            #adv:
            state.pointer += 2
            state.a = state.a//combo_operands(operand)**2 #pylint: disable=C0103
        case 1:
            #bxl:
            state.pointer += 2
            state.b = state.b ^ operand #pylint: disable=C0103
        case 2:
            #bst
            state.pointer += 2
            state.b = combo_operands(operand) % 8 #pylint: disable=C0103
        case 3:
            #jnz:
            if state.a == 0: #pylint: disable=C0103
                state.pointer += 2
            else:
                state.pointer = operand
        case 4:
            #bxc:
            state.pointer += 2
            state.b = state.b ^ state.c #pylint: disable=C0103
        case 5:
                #out:
            state.pointer += 2
            state.output.append(combo_operands(operand) %8)
        case 6:
            #bdv:
            state.pointer += 2
            state.b = state.a//(combo_operands(operand)**2) #pylint: disable=C0103
        case 6:
            #bdv:
            state.pointer += 2
            state.b = state.a//combo_operands(operand)**2 #pylint: disable=C0103
#    return state

def print_vm():
    print(f'A:{state.a} B:{state.b} C:{state.c} Instruction Pointer: {state.pointer}')


state = MachineState(0,0,0,0,[])
