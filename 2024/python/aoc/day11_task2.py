"""AoC 2024 Day 11

1) If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
2) If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
3)If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


1) if stone == 0, then stone == 1
2) if len(stone) % 2 == 0:
    split in left, right in the middle, with leading zeros removed
3) stone replace with new stone, old val * 2024

"""

def stones_to_int(stone: str)-> list[int]:
    return [int(x) for x in stone.split()]


def stone_action(stone:int )-> list[int]:

    if stone == 0:
        return [1]
    
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        left = stone[0:len(stone)//2]
        right = stone[len(stone)//2:]
        left, right = str(left), str(right)
        right = right.lstrip('0')
        if right == '':
            right = '0'
        return [int(left), int(right)]
    
    return [stone*2024]

def do_blink(int_stones:list[int]) -> list[int]:
    res = []
    for stone in int_stones:
        res.extend(stone_action(stone))
    return res

def do_blinks(iterations: int, int_stones: list[int]) -> list[int]:
    res = int_stones
    for _ in range(iterations):
        res = do_blink(res)
    return res

def count_stones(iterations: int, int_stones: list[int]) -> int:
    _ = do_blinks(iterations, int_stones)
    return len(_)

def do_it(iterations: int, stones: str):
    int_stones = stones_to_int(stones)
    return count_stones(iterations, int_stones)

def main() -> None:
    """Main function"""
    raise NotImplementedError


if __name__ == "__main__":
    main()
