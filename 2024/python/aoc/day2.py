# File handling


def open_file(fname):
    # Returns a file handle
    try:
        fhand = open(fname, "r")
    except IOError as e:  # pragma: no cover
        exit()
    return fhand


def read_file(fname):
    fhand = file_handle = open_file(fname)
    for content in fhand:
        if any(element.isdigit() for element in content):
            seq = [int(x) for x in content.split()]
            yield seq


# Utility functions


def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
    return (datum for datum, selector in zip(data, selectors) if selector)


# Core test logic


def has_duplicates(seq):
    return len(seq) != len(set(seq))


def has_unorder(seq):
    if seq[0] < seq[-1]:
        return seq != sorted(seq)
    elif seq[0] > seq[-1]:
        return seq != sorted(seq, reverse=True)


def has_jump(seq):
    for index in range(1, len(seq)):
        jump = abs(seq[index - 1] - seq[index])
        if jump > 3:
            return True
    return False


def check_line(seq):
    if has_duplicates(seq) or has_unorder(seq) or has_jump(seq):
        return False
    return True


# line fixing for stage 2


def fix_iter(seq):
    # Returns a generator that will drop one element in a list across the entire list
    # list(fix_iter(range(3))) -> [[1, 2], [0, 2], [0, 1]]
    for index in range(len(seq)):
        selectors = [1 for x in seq]
        selectors[index] = 0
        yield list(compress(seq, selectors))


def is_fixable(seq):
    for tseq in fix_iter(seq):
        if check_line(tseq):
            return True
    return False


# Core task


def task(fname, stage=1):
    #
    res = 0
    lines = read_file(fname)
    for line in lines:
        if check_line(line):
            res += 1
        elif stage == 2 and is_fixable(line):
            res += 1

    return res


if __name__ == "__main__":  # pragma: no cover
    print(task("input.txt", stage=2))
