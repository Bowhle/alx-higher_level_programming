#!/usr/bin/python3
"""A function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Initialize a new row with 1s
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
