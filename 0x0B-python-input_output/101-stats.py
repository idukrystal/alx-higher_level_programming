#!/usr/bin/python3
""" Reads every ten lines of stdin printing errors and storage used

Attributes:
    fs (int): use dto safe total memory used
    sc (dict): records how many times an err code pops up

"""

from sys import stdin
""" imports stdin """

while True:
""" a while loop """
    for i in range(10):
        try:
            line = stdin.readline()
            fs += int(getdata(line, 4))
            sc[int(getdata(line, 3))] += 1
        except (KeyboardInterrupt):
            break
    print(f"File size: {fs}")
    for key in sc:
        if sc[key] != 0:
            print(f"{key}: {sc[key]}")
            sc[key] = 0
