"""AoC Day 5 Task 1"""


def fread_all(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]


def find_middle(line):
    """Find middle element of array index: (len(line[0]) - 1)//2"""
    return (len(line) - 1) // 2


def clean_data(data):
    rules = {}
    updates = []
    for line in data:
        if line == "":
            pass
        elif "|" in line:
            (left, right) = line.split("|")
            if left in rules:
                rules[left].append(right)
            else:
                rules[left] = [right]
        else:
            _ = line.split(",")
            updates.append(_)
    return (rules, updates)


def check_line(rules, line):
    key_set = set(rules.keys())
    for index in range(1, len(line)):
        char = line[index]
        if char in key_set:
            lset = set(line[:index])
            rset = set(rules[char])
            if len(rset.intersection(lset)) > 0:
                return False
    return True


def find_bad(rules, line):
    res = False
    key_set = set(rules.keys())
    for index in range(1, len(line)):
        char = line[index]
        if char in key_set:
            if index == 0:
                pass
            lset = set(line[:index])
            rset = set(rules[char])
            iset = lset.intersection(rset)
            if len(iset) > 0:
                _ = iset.pop()
                res = ((index, char), (line.index(_), _))

    return res


def fix_line(rules, line):
    if not check_line(rules, line):
        ((lindex, lval), (rindex, rval)) = find_bad(rules, line)
        line[lindex], line[rindex] = rval, lval
    if not check_line(rules, line):
        fix_line(rules, line)

    return line


def fix_lines(filename):

    rules, updates = clean_data(fread_all(filename))
    res = 0
    for line in updates:
        m_val = line[find_middle(line)]
        if not check_line(rules, line):
            _ = fix_line(rules, line)
            m_val = line[find_middle(_)]
            res += int(m_val)
    return res


def run_it(filename):

    rules, updates = clean_data(fread_all(filename))

    res = 0
    for line in updates:
        m_val = line[find_middle(line)]
        if check_line(rules, line):
            res += int(m_val)
    return res
