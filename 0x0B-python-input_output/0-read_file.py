#!/usr/bin/python3
""" a function that reads a text file UTF-8 and prints to standard out"""


def read_file(filename=""):
    """  the function defination """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
