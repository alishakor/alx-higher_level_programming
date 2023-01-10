#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    if len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    if len(sys.argv) - 1 > 1:
        print("{} arguments:".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
