import re

def get_lists(filneame):
    left, right = [], []
    with open(filneame, "r") as file:
        for line in file.readlines():
            match = re.match("^(\S+)\s+(\S+)$", line)
            if match:
                left.append(int(match.group(1)))
                right.append(int(match.group(2)))

    return left, right