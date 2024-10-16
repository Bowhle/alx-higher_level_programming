#!/usr/bin/python3
""" a function that appends a string at the end of a txt fiile """


def append_write(filename="", text=""):
    """ returns the number of charcater added """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
