import re

# File handling
def open_file(fname):
    # Returns a file handle
    try:
        fhand = open(fname, "r")
    except IOError as e:
        logger.error("IO Error:", e)
        exit()
    return fhand

def find_matches(line):
    pattern = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)"
    return re.findall(pattern,line)

def clean_matches(seq):
    res = []
    clean_pattern = r"\d{1,3}\,\d{1,3}"
    for item in seq:
        if item == 'do()':
            res.append((True,True))
        elif item == "don't()":
            res.append((False,False))
        else:
            values = re.findall(clean_pattern,item)
            lval, rval = values[0].split(',')
            res.append((int(lval),int(rval)))
    return res


def run_it(fname="data/test/3.txt"):
    res = 0
    fhand = open_file(fname)
    do = True
    for line in fhand:
        items = clean_matches(find_matches(line))
        for item in items:
            left, right = item
            if left == True or left == False:
                do = left
            elif do == True:
                res += left * right

    return res


if __name__ == "__main__":
    print(run_it("data/input/3.txt")) # pragma: no cover
