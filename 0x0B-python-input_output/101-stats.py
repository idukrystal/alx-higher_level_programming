#!/usr/bin/python3
""" Reads every ten lines of stdin printing errors and storage u\
ed

Attributes:
    fs (int): use dto safe total memory used
    sc (dict): records how many times an err code pops up

"""


from sys import stdin
""" Imports stdin module  """

def getdata(st, no):
    """ Parses st for the noth <>

    Args:
        st (str): String to Parsr
        no (int); Point to parse from

    Returns:
        returns int parsed
    """

    le = len(st)
    for i in range(le):
        if st[i] == '<':
            no -= 1
        if no == 0:
            for j in range(i, le):
                if st[j] == '>':
                    return st[i+1:j]


while True:
    """ pumch in the good """
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
