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

    Returns:
        numpy.ndarray: The resulting matrix product.
    """

    return (np.matmul(m_a, m_b))
