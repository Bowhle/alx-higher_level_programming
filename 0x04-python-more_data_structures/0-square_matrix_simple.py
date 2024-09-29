#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix: A 2-dimensional array (list of lists).

    Returns:
        A new matrix where each value is the square of the value of the input matrix.
    """
    return [[value ** 2 for value in row] for row in matrix]

