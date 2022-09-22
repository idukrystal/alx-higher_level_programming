#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    i = 1
    word = "argument" if (l == 2) else "arguments"
    #end = "." if (l == 1) else ":"
    l -= 1
    print("{} {}{}".format(l, word, end))
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
