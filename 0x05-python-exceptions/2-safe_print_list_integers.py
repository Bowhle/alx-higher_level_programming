#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
