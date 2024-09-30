#!/usr/bin/python4

def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []
    count = 0
    try:
        print("{:d}".format(my_list[x]), end="")
        count += 1
    except (ValueError, TypeError):
        continue
    except IndexError:
        break

    print("")
    return count
