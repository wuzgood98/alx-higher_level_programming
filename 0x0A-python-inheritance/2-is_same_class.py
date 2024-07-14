#!/usr/bin/python3
# 2-is_same_class.py
# Gideon O Addo
"""Define a function is_same_class"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly the same as an instance of a given class.

    Args:
        obj (any): Object to compare with the class
        a_class (type): class to compare with the object.

    Returns:
        True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
