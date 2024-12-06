"""AoC Day 5 Task 1"""

def fread_all(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def find_middle(line):
    return (len(line) - 1)//2

def clean_data(input):
    rules = {}
    updates = []
    for line in input:
        if line == '':
            pass
        elif '|' in line:
            (left, right) =line.split('|')
            rules[left] = right
        else:
            _ = line.split(',')
            updates.append(_)
    return (rules, updates)

# Find middle element of array index: (len(line[0]) - 1)//2


"""
test_raw = fread_all('../data/test/5.txt'


trules, tupdates = clean_data( fread_all('../data/test/5.txt'))

"""

def run_it(filename):
    pass
