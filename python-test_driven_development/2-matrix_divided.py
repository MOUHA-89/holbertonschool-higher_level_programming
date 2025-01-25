#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
    matrix (list of lists): The input matrix of integers or floats.
    div (int or float): The number to divide by.

    Returns:
    list of lists: A new matrix with all elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
               if rows have different sizes, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix):
        raise TypeError:
            ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and rounding
    return [[round(element / div, 2) for element in row] for row in matrix]
