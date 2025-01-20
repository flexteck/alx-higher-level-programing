#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divides all element of a matrix
    raise a TypeError when of of the rows is not of the
    size.
    the parameter div must be an int or float otherwise
    it should raise a TypeError
    raise ZeroDevisionError when div equal 0

    Args:
       matrix: first argument which is a matrix
       div: second argument (int or float)

    Return: new matrix
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if matrix == [] or matrix == [[],[]] or len matrix == 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = [[round(i / div, 2) for i in row] for row in matrix]

    return newMatrix


