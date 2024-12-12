"""AoC 2024 Day 11

1) if stone == 0, then stone == 1
2) if len(stone) % 2 == 0:
    split in left, right in the middle, with leading zeros removed
3) stone replace with new stone, old val * 2024

"""
#from functools import lru_cache

def stones_to_int(stone: str)-> list[int]:
    return [int(x) for x in stone.split()]

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
        multiplier = 1
        if stones[key] > 1:
            multiplier = stones[key]

        res = list(stone_action(key))
        res = res * multiplier

        
        yield from res

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
    total = 0
    res = do_blinks(iterations, stones)
    for index in res:
        total += res[index]
    return total




if __name__ == "__main__":
    pass
