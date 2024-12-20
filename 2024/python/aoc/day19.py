"""AoC 2024 Day 18 Task 1"""

# pylint: disable=E0606,E0601,C0103


# File Handeling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def clean_data(filename: str):
    raw_input = read_file(filename)
    towels = raw_input[0].split(", ")

    patterns = []
    for index in range(2, len(raw_input)):
        patterns.append(raw_input[index])

    return towels, patterns


def can_construct(pattern: str, towels: list[str], memo=None) -> bool:
    if memo is None:
        memo = {}
    if pattern in memo:
        return memo[pattern]
    # Base Case
    if pattern == "":
        return True

    for towel in towels:
        if pattern.find(towel) == 0:
            suffix = pattern[len(towel) :]
            if can_construct(suffix, towels, memo=memo):
                memo[pattern] = True
                return True

    memo[pattern] = False
    return False


def count_construct(pattern: str, towels: list[str], memo=None) -> int:
    total = 0
    if memo is None:
        memo = {}
    if pattern in memo:
        return memo[pattern]
    # Base Case
    if pattern == "":
        return 1

    for towel in towels:
        if pattern.find(towel) == 0:
            suffix = pattern[len(towel) :]
            number_matches = count_construct(suffix, towels, memo)
            total += number_matches
            memo[suffix] = number_matches
    memo[pattern] = total
    return total


def solution(filename):
    towels, patterns = clean_data(filename)
    task1, task2 = 0, 0
    # Task 1
    for pattern in patterns:
        task1 += can_construct(pattern, towels)

    # Task 2
    for pattern in patterns:
        task2 += count_construct(pattern, towels)

    return task1, task2


if __name__ == "__main__":

    task_1, task_2 = solution("data/input/19.txt")
    print(f"Task 1: {task_1}")
    print(f"Task 2: {task_2}")
