#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    func = lambda rw: [col * col for col in rw]
    return [func(row) for row in matrix]
