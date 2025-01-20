#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find the peak number with the shortest algorithm """
    if not list_of_integers:
        return None

    def binary_search(start, end):
        mid = (start + end) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
                (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search(start, mid - 1)
        else:
            return binary_search(mid + 1, end)

    return binary_search(0, len(list_of_integers) - 1)
