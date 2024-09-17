#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = (tuple_a + (0, 0))[:2]
    # Ensure tuple_b has atleast 2 elements, returning 0 if not.
    b1, b2 = (tuple_b + (0, 0))[:2]
    # Add corresponding elements.
    return a1 + b1, a2 + b2