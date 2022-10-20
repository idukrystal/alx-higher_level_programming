#!/usr/bin/python3

"""module 2-matrix_divided
   fuctions:
       def matrix_divided(matrix, div)
       example
          >>> matrix_divided([[4, 8], [16, 20]], div)
          [[1, 2], [4, 5]]
"""


def matrix_divided(matrix, div):
    """divides a all numbers withen a list of list of numbers(matrix) by (div)
    n.b
       matrix musts be square
    """
    if not (isinstance(matrix, list) and
            all(
                isinstance(li, list) and
                all(
                    isinstance(it, int) or
                    isinstance(it, float) for it in li
                ) for li in matrix
            )
            ):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    if not all(len(li) == len(matrix[0]) for li in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = eval(str(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new[i][j] = (matrix[i][j])/div
    return new
