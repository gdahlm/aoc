"""AoC 2024 Day 9 Task 1


12345 ==
1: one-block file
2: two blocks of free space
3: three-block file
4: four blocks of free space
5: five-block file


"""


test_input = "2333133121414131402"  # pylint: disable=invalid-name

test_input_expanded = (
    "00...111...2...333.44.5555.6666.777.888899"  # pylint: disable=invalid-name
)

test_input_sorting_steps = [  # pylint: disable=invalid-name
    "00...111...2...333.44.5555.6666.777.888899",
    "009..111...2...333.44.5555.6666.777.88889.",
    "0099.111...2...333.44.5555.6666.777.8888..",
    "00998111...2...333.44.5555.6666.777.888...",
    "009981118..2...333.44.5555.6666.777.88....",
    "0099811188.2...333.44.5555.6666.777.8.....",
    "009981118882...333.44.5555.6666.777.......",
    "0099811188827..333.44.5555.6666.77........",
    "00998111888277.333.44.5555.6666.7.........",
    "009981118882777333.44.5555.6666...........",
    "009981118882777333644.5555.666............",
    "00998111888277733364465555.66.............",
    "0099811188827773336446555566..............",
]

small_input = "12345"  # pylint: disable=invalid-name

small_input_expanded = "0..111....22222"  # pylint: disable=invalid-name

small_input_sorting_steps = [
    "0..111....22222",
    "02.111....2222.",
    "022111....222..",
    "0221112...22...",
    "02211122..2....",
    "022111222......",
]

import re
from io import StringIO

def fread_all(file_path: str) -> list[str]:
    """Return all lines from a file at once"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()


def expand_disk(string: str) -> str:
    sentence = StringIO()
    blocks = string[::2]
    freespace = string[1::2]
    length = max(len(blocks), len(freespace))

    for index in range(length):
        f_value = None
        b_count = int(blocks[index])
        b_value = index

        if index < len(freespace):
            f_value = int(freespace[index])
        b_out = str(b_value) * b_count

        if f_value is not None:
            f_out = "." * f_value
        else:
            f_out = ""

        sentence.write(b_out + f_out)

    return sentence.getvalue()

def expand_disk_csv(string: str) -> str:
    sentence = StringIO()
    blocks = string[::2]
    freespace = string[1::2]
    lenght = max(len(blocks), len(freespace))

    for index in range(lenght):
        f_value = None
        b_count = int(blocks[index])
        b_value = index

        if index < len(freespace):
            f_value = int(freespace[index])

        if f_value is not None:
            f_out = ".," * f_value
        else:
            f_out = ""
        
        b_out_list = []
        for count in range(b_count):
            b_out_list.append(str(b_value))
            b_out_list.append(',')

        b_out= ''.join(b_out_list)

        sentence.write(b_out + f_out)

    return sentence.getvalue()

def calculate_checksum(string: str) -> int:
    res = 0
    for index, item in enumerate(string):
        if item != ".":
            res += int(item) * index
    return res

def calculate_checksum_csv(string: str) -> int:
    res = 0
    array = string.split(',')
    array = [x for x in array if x !='.' and x != '']
    for index, item in enumerate(array):
        if item != "." or item != '':
            res += int(item) * index
    return res


def sort_disk(string: str) -> str:  # pylint: disable=unused-argument
    array = [x for x in string]
    num_pattern = re.compile(r"\d")
    free_pattern = re.compile(r"(\.+)")
    free_matches = re.finditer(free_pattern, string)
    num_matches = re.finditer(num_pattern, "".join(array)[::-1])
    length = len(array)

    for free_match in free_matches:
        start, end = free_match.span()
        for index in range(start, end):
            num_match = next(num_matches)
            match_val = num_match.group(0)
            _, match_index = num_match.span()
            match_index *= -1
            offset = length + match_index
            if index >= offset:
                break
            array[index], array[match_index] = match_val, "."
    return "".join(array)

def sort_disk_csv(csv_string: str) -> str:  # pylint: disable=unused-argument
    # TODO
    array = csv_string.split(',')
    free_matches = []
    num_matches = []

    for index, value in enumerate(array):
        if value == '.':
            free_matches.append(index)
        if value.isnumeric():
            num_matches.append(index)

    length = len(array)
    # num_matches.reverse() # Inplace reverse order

    for index in free_matches:
            num_match = num_matches.pop()
            match_val = array[num_match]
            if index >= num_match:
                break
            array[index], array[num_match] = match_val, "."
    return ",".join(array)

def do_it(filename):
    data = fread_all(filename)
    data = data[0].strip()
    data_csv = expand_disk_csv(data)
    data_csv_sorted = sort_disk_csv(data_csv)
    checksum = calculate_checksum_csv(data_csv_sorted)
    return checksum



def main() -> None:
    """Main function"""
    raise NotImplementedError


if __name__ == "__main__":
    main()
