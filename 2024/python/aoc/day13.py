"""AoC 2024 Day 13
Cramer's Rule
~~~~~~~~~~~~~

ax + by = e
cx + dy = f
    
Given x and y are unknows, and ad - bc != 0:

x = (de-bf)/(ad-bc), y = (af-ce)/(ad-bc)
"""


def fread_line(file_path: str):
    """Lazy read of file returning a generator"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        yield from file_in


def parse_input(finput):
    res = []
    a_in = [x.strip("Button A: ").strip("X+").split(", Y+") for x in finput[::4]]
    b_in = [x.strip("Button B: ").strip("X+").split(", Y+") for x in finput[1::4]]
    p_in = [x.strip("Prize: X=").split(", Y=") for x in finput[2::4]]
    for index in range(len(a_in)):  # pylint: disable=consider-using-enumerate
        res.append(
            (
                (int(a_in[index][0]), int(a_in[index][1])),
                (int(b_in[index][0]), int(b_in[index][1])),
                (int(p_in[index][0]), int(p_in[index][1])),
            )
        )
    return res


def try_game(data, offset):
    (x1, y1), (x2, y2), (xp, yp) = data
    # Added for task 2
    xp += offset
    yp += offset
    # Cramer's Rule: AX=B
    # determinant = (x2 * y1 - x1 * y2)
    B = (y1 * xp - x1 * yp) / (
        x2 * y1 - x1 * y2
    )  # pylint: disable=invalid-name #(it's math!!!!)
    if B.is_integer():
        A = (
            xp - B * x2
        ) / x1  # pylint: disable=invalid-name #(I know, won't do it again)
        if A.is_integer():
            return data, int(A), int(B)


def main(fname: str | None = None) -> None:
    """Main function"""
    a_pmult, b_pmult = 3, 1
    offsets = [0, 10000000000000]
    solution = []

    if fname is None:
        fname = "data/input/13.txt"

    data_input = [x.strip() for x in fread_line(fname)]
    data = parse_input(data_input)

    for offset in offsets:
        res = 0
        for _, a, b in filter(
            bool, map(lambda x: try_game(x, offset), data)
        ):  # pylint: disable=W0640
            res += a * a_pmult + b * b_pmult
        solution.append(res)
    return solution


if __name__ == "__main__":
    print(main("data/test/13.txt"))
