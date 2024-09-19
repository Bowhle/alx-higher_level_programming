#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")

    for i in range(1, argc + 1):
        print(f"{i}: {argv[i]}")
