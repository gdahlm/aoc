"""AoC Day 5 Task 1"""

def fread_all(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def find_middle(line):
    """Find middle element of array index: (len(line[0]) - 1)//2"""
    return (len(line) - 1)//2

def clean_data(input):
    rules = {}
    updates = []
    for line in input:
        if line == '':
            pass
        elif '|' in line:
            (left, right) =line.split('|')
            if left in rules.keys():
                rules[left].append(right)
            else:
                rules[left] = [right]
        else:
            _ = line.split(',')
            updates.append(_)
    return (rules, updates)


def check_line(rules, line):
     key_set = set(rules.keys())
     for index in range(1,len(line)):
         char = line[index]
         if char in key_set:
            lset = set(line[:index])
            rset = set(rules[char])
            if len(rset.intersection(lset)) > 0:
                 return False
     return True

"""
test_raw = fread_all('../data/test/5.txt'


trules, tupdates = clean_data( fread_all('../data/test/5.txt'))

"""

def run_it(filename):

    rules, updates = clean_data( fread_all(filename))

    res = 0
    for line in updates:
        m_val = line[find_middle(line)]
        if check_line(rules, line):
            res += int(m_val)
    return res


