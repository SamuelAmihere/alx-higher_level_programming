#!/usr/bin/python3
"""A pyhton module that defines a matrix multiplication function""" 


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix
    Returns:
        list: The result of the multiplication
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format("m_a" if isinstance(
            m_a, list) else "m_b"))
    if not all(isinstance(row, list) for row in m_a) or\
        not all(isinstance(row, list) for row in m_b):
        raise TypeError("{} must be a list of lists".format(
            "m_a" if all(isinstance(row, list) for row in m_a) else "m_b"))
    
    if not all(len(row) == len(m_a[0]) for row in m_a) or\
        not all(len(row) == len(m_b[0]) for row in m_b):

        raise TypeError("each row of {} must should be of the same size".format(
            "m_a" if all(len(row) == len(m_a[0]) for row in m_a) else "m_b"))
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("can't multiply matrices of different sizes")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)] for row_a in m_a]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
