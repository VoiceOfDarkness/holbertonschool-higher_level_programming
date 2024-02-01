#!/usr/bin/python3

def matrix_divided(matrix: list, div: int):
    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeError = 'Each row of the matrix must have the same size'
    if not isinstance(matrix, (list)):
        raise TypeError(listError)
    for item in range(len(matrix)):
        if item != 0:
            result = item - 1
            if len(matrix[item]) is not len(matrix[result]):
                raise TypeError(sizeError)
    if not isinstance(div, int):
        raise TypeError('div must be a number')
    return [[round(i / div, 2) for i in row] for row in matrix]
