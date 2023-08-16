#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for r in range(len(new_matrix)):
        new_matrix[r] = list(map(lambda x: x ** 2, new_matrix[r]))
    return new_matrix
