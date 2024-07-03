#!/usr/bin/python3
# 101-lazy_matrix_mul.py
# Gideon O Addo
"""Defines a matrix multiplication function"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
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
        numpy.ndarray: The resulting matrix product.
    """

    # Convert input to numpy arrays
    try:
        m_a_np = np.array(m_a, dtype=float)
        m_b_np = np.array(m_b, dtype=float)
    except ValueError as e:
        raise TypeError('m_a and m_b should contain only integers or float')

    # Validate m_a and m_b are lists of lists
    if (not isinstance(m_a, list) or not
            all(isinstance(row, list) for row in m_a)):
        raise TypeError('m_a must be a list of lists')
    if (not isinstance(m_b, list) or not
            all(isinstance(row, list) for row in m_b)):
        raise TypeError('m_b must be a list of lists')

    # Validate m_a and m_b are not empty
    if m_a_np.size == 0:
        raise ValueError("m_a can't be empty")
    if m_b_np.size == 0:
        raise ValueError("m_b can't be empty")

    # Validate all rows in m_a are of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # Validate if the matrices can be multiplied
    if m_a_np.shape[1] != m_b_np.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result_matrix = np.dot(m_a_np, m_b_np)
    return result_matrix
