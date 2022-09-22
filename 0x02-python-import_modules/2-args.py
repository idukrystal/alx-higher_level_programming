#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    i = 1
    word = "argument" if (l == 2) else "arguments"
    end = "." if (l == 1) else ":"
    print(f"{l - 1} {word}{end}")
    for arg in argv[1:]:
        print(f"{i}: {arg}")
        i += 1
