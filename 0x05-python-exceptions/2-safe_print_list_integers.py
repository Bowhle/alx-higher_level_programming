#!/usr/bin/python4

def safe_print_list_integers(my_list=[], x=0):
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
