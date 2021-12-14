#!/usr/bin/python3
"""
Module with function to divide a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Function to divide a matrix by a number
    """

    len_array = []
    j = i = 0
    a = b = m = n = l = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lists in matrix:
        if isinstance(lists, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in lists:
            if isinstance(num, int) is False and isinstance(num, float) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        len_array.append(len(lists))
        i += 1
        l += 1
    for j in range(l - 1):
        if len_array[j] != len_array[j + 1]:
            raise TypeError("Each row of the matrix must have the same size")
        j += 1
    new_matrix = [[0 for a in range(len(matrix[0]))] for b in range(len(matrix))]
    for m in range(2):
        n = 0
        for num in range(len(matrix[m])):
            new_matrix[m][n] = round((matrix[m][n] / div), 2)
            n += 1
        m += 1
    return new_matrix
