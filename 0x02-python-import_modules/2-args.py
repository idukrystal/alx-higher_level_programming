#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    i = 1
    word = "argument" if (length == 2) else "arguments"
    end = "." if (length == 1) else ":"
    print("{} {}{}".format(length - 1, word, end))
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
