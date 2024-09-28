def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a 2D matrix.

    Args:
        matrix: A 2D matrix (list of lists).

    Returns:
        A new matrix with the same size where each value is squared.
    """
    # Using a list comprehension to create a new matrix with squared values.
    return [[x**2 for x in row] for row in matrix]

