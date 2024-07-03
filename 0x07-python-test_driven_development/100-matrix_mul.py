#!/usr/bin/python3
# 100-matrix_mul.py
# Gideon O Addo
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty([] or [[]]).
        TypeError: If one element of both lists is not integer or a float.
        TypeError: If m_a or m_b is not a rectangle(all rows should be
        of the same size).
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        List of lists of ints/floats: The resulting matrix product.
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(
            (isinstance(elem, (int, float))) for row in m_a for elem in row
            ):
        raise TypeError('m_a should contain only integers or floats')
    if not all(
            (isinstance(elem, (int, float))) for row in m_b for elem in row
            ):
        raise TypeError('m_b should contain only integers or floats')

    row_size_a, row_size_b = len(m_a[0]), len(m_b[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # Validate matrix compatibility
    if row_size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result_matrix = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(row_size_b):
            element_sum = 0
            for k in range(row_size_a):
                element_sum += m_a[i][k] * m_b[k][j]
            result_row.append(element_sum)
        result_matrix.append(result_row)

    return result_matrix
