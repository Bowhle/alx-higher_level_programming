#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
<<<<<<< HEAD
            pass
        except IndexError:
            break
    print()
=======
            continue
    print("")
>>>>>>> 062a8788f3da7b0d968d9a6abb2b5988d9eb1c37
    return count

