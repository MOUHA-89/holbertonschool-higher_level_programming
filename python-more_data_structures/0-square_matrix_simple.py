#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    new_matrix = []

    for row in matrix:
        squared_row = [x ** 2 for x in row]
        new_matrix.append(squared_row)

    return new_matrix
