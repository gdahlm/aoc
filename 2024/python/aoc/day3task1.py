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
    pattern = r"mul\(\d{1,3}\,\d{1,3}\)"
    return re.findall(pattern,line)


def run_it():
    pass

if __name__ == "__main__":
    print(run_it("data/test/3.txt")) # pragma: no cover
