#!/usr/bin/python3
# 0-add_integer.py
# Gideon O Addo
"""Define a function add_integer"""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Args:
        a (int): The first operand
        b (int): The second operand

    Return:
        The addition of a and b (int).
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
