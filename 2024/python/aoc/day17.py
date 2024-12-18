"""AoC 2024 Day 17 Task 1"""
def vm(**kwargs):
    # Registers
    A, B ,C = None, None, None #pylint: disable=C0103
    # pointer
    pointer = 0
    output = None

    def combo_operands(operand:int) -> int:
        nonlocal A, B, C #pylint: disable=C0103
        match operand:
            case 1 | 2 | 3 as n:
                return n
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                raise ValueError('Combo Operand (7) is Reserved')
            case _:
                raise ValueError('Combo Operand is out of range')

    def do_instruction(opcode:int, operand:int):
        nonlocal A,B,C,pointer,output #pylint: disable=C0103
        match opcode:
            case 0:
                #adv:
                pointer += 2
                A = A//combo_operands(operand)**2 #pylint: disable=C0103
            case 1:
                #bxl:
                pointer += 2
                B = B ^ operand #pylint: disable=C0103
            case 2:
                #bst
                pointer += 2
                B = combo_operands(operand) % 8 #pylint: disable=C0103
            case 3:
                #jnz:
                if A == 0: #pylint: disable=C0103
                    pointer += 2
                else:
                    pointer = operand
            case 4:
                #bxc:
                pointer += 2
                B = B ^ C #pylint: disable=C0103
            case 5:
                #out:
                pointer += 2
                output.append(combo_operands(operand) %8)
            case 6:
                #bdv:
                pointer += 2
                B = A//combo_operands(operand)**2 #pylint: disable=C0103
            case 6:
                #bdv:
                pointer += 2
                B = A//combo_operands(operand)**2 #pylint: disable=C0103

    def inner():
        nonlocal A, B, C, pointer, output #pylint: disable=C0103
        print(f'A:{A} B:{B} C:{C}')

    #public methods
    inner.combo_operands = combo_operands

    # Exposed Attributes
    inner.A, inner.B, inner.C, inner.pointer, = A, B, C, pointer

    return inner
