#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    a function that devides a matrix by a number
    matrix: is the matrix to be devided
    div: is the number we are dividing by
    Returns a new matrix
    """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])

    for row in matrix:
        if not (len(row) == length):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix



