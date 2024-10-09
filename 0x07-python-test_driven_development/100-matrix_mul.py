#!/usr/bin/python3
"""Module for multiplying two matrices"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices m_a and m_b"""

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if the matrices can be multiplied
    if len(m_
