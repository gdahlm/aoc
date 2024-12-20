"""AoC 2024 Day 11 task 1"""


def stone_action(stone):

    if stone == "0":
        return "1"

    if len(stone) % 2 == 0:
        left = stone[0 : len(stone) // 2]
        right = stone[len(stone) // 2 :]
        left, right = str(left), str(right)
        right = right.lstrip("0")
        if right == "":
            right = "0"
        return left + " " + right

    _ = int(stone) * 2024
    return str(_)


def do_blink(stones: str) -> str:
    res = []
    stones_list = stones.split()

    for stone in stones_list:
        res.append(stone_action(stone))
    return " ".join(res)


def do_blinks(iterations: int, stones: str) -> str:
    res = stones
    for _ in range(iterations):
        res = do_blink(res)
    return res


def count_stones(iterations: int, stones: str) -> str:
    _ = do_blinks(iterations, stones)
    return len(_.split())


def main() -> None:
    """Main function"""
    raise NotImplementedError


if __name__ == "__main__":
    main()
