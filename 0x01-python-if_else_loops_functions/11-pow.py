#!/usr/bin/python3

def pow(a, b):
    # Handle case when b is 0
    if b == 0:
        return 1

    # Compute power for positive b
    result = 1
    for _ in range(abs(b)):
        result *= a

    # If b is negative, return the reciprocal
    if b < 0:
        return 1 / result
    return result
