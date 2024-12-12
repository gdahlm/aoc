"""AoC 2024 Day 11

1) If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
2) If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
3)If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


1) if stone == 0, then stone == 1
2) if len(stone) % 2 == 0:
    split in left, right in the middle, with leading zeros removed
3) stone replace with new stone, old val * 2024

"""
from functools import lru_cache 

def stones_to_int(stone: str)-> list[int]:
    return [int(x) for x in stone.split()]

#@lru_cache(maxsize = 1024) 
def stone_action(stone:int ):

    if not isinstance(stone, int):
        return

    if stone == 0:
        yield 1
        return

    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        left = stone[0:len(stone)//2]
        right = stone[len(stone)//2:]
        left, right = str(left), str(right)
        right = right.lstrip('0')
        if right == '':
            right = '0'

        yield int(left)
        yield int(right)
        return

    yield stone*2024

def do_blink_gen(stones):
    if isinstance(stones, list):
        _ = {}
        for item in stones:
            if item not in _:
                _[item] = 1
            else:
                _[item] += 1
        stones = _

    for key in stones:
        for _ in range(stones[key]):
            yield from stone_action(key)

def do_blinks(iterations: int, stones):
    res = stones
    for _ in range(iterations):
        res = do_blinks_map(res)

    return res

def do_blinks_map(stones):
    found, res = {}, {}
    if isinstance(stones, list):
        _ = {}
        for item in stones:
            if item not in _:
                _[item] = 1
            else:
                _[item] += 1
        stones = _

    blink_gen = do_blink_gen(stones)
    for item in blink_gen:
        if item in found:
           found[item] +=1 
        else:
            found[item] = 1

    return found


def count_stones(iterations: int, stones) -> int:
    sum = 0
    res = do_blinks(iterations, stones)
    for index in res:
        sum += res[index]
    return sum




if __name__ == "__main__":
    pass
