#!/usr/bin/python3
# 4-inherits_from.py
# Gideon O Addo
"""Define a an instance comparing function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance
    of a class that inherited(directly or inderectly)
    from, the specified class, otherwise False.

    Args:
        obj (any): object to be compared
        a_class (type): class to be compared to.

    Returns:
        True if it is an instance of the class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
