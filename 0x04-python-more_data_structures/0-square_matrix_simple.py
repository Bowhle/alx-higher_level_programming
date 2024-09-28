#!/usr/bin/python3
from typing import List

def square_matrix_simple(matrix: List[List[int]]) -> List[List[int]]:
    return [[element ** 2 for element in row] for row in matrix]
