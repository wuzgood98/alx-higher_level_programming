#!/usr/bin/python3
# 3-is_kind_of_class.py
# Gideon O Addo
"""Define a an instance comparing function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class, otherwise False.

    Args:
        obj (any): object to be compared
        a_class (type): class to be compared to.

    Returns:
        True if it is an instance of the class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
