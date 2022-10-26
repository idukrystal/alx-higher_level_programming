#!/usr/bin/python3
"""appends a string at a specific point in a file"""


def has(this, that):
    """checks if that has this"""
    le1 = len(that)
    le2 = len(this)
    i = 0
    while i < le1:
        if that[i] == this[0]:
            j = i
            while j < le1 and (j - i) < le2 and that[j] == this[j - i]:
                j += 1
            if (j - i) == le2:
                return True
            i = j - 1
        i += 1


def append_after(filename="", search_string="", new_string=""):
    """appends new to new lines after any line in file containing search"""
    if search_string == "":
        return
    with open(filename, "r") as fil:
        lines = fil.readlines()
        for i in range(len(lines)):
            if has(search_string, lines[i]):
                lines.insert(i + 1, new_string)
    with open(filename, "w") as fil:
        for line in lines:
            fil.write(line)
