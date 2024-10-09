#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy after validating input."""

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Use NumPy to perform the multiplication
    result = np.matmul(m_a, m_b)
    return result.tolist()
