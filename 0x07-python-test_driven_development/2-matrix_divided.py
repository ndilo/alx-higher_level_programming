#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if the rows of the matrix have different sizes, or
                   if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    """ Check if div is a number (integer or float) """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """ Check if div is equal to 0 """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ Check if matrix is a list of lists of integers or floats """
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """ Check if all rows have the same size """
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    """ Divide all elements of the matrix by div and round to 2 decimal places """
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
