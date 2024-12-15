"""AoC 2024 Day 11 Part 2"""
def blink_logic(stone):
    if stone == 0:
        return [1]

    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        left = str_stone[: len(str_stone) // 2]
        right = str_stone[len(str_stone) // 2 :]
        return [int(left), int(right)]
    return [stone * 2024]


def solution(stones, blinks):
    memo, count= {}, 0

    def dfs(number, iteraton):
        count = 0
        # Base Case
        if iteraton == 0:
            return 1

        if (number, iteraton) in memo:
            return memo[(number, iteraton)]

        array = blink_logic(number)
        for item in array:
            count += dfs(item, iteraton- 1)
        memo[(number, iteraton)] = count
        return count

    for stone in stones:
        count += dfs(stone, blinks)
    return count


def main():
    return solution([6571, 0, 5851763, 526746, 23, 69822, 9, 989], 25)


if __name__ == '__main__':
    print(main())
