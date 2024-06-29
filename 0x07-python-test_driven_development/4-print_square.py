#!/usr/bin/python3
# 4-print_square.py
# Gideon O Addo
"""Defines a square-printing function"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Returns:
        No return
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        [print('#', end='') for j in range(size)]
        print('')
