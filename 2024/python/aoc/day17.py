
def vm(**kwargs):
    # Registers
    A, B ,C = None, None, None
    # pointer
    pointer = 0
    output = None

    def combo_operands(operand:int) -> int:
        nonlocal A, B, C
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

    def inner():
        nonlocal A, B, C, pointer, output
        print(f'A:{A} B:{B} C:{C}')

    #public methods
    inner.combo_operands = combo_operands

    # Exposed Attributes
    inner.A, inner.B, inner.C, inner.pointer, = A, B, C, pointer
    
    return inner