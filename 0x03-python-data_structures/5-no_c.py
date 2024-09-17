#!/usr/bin/python3
def no_c(my_string):
    # Creating a new string with characters that are not 'c' or 'C'
    return ''.join(char for char in my_string if char not in ('c', 'C'))
