#!/usr/bin/python3
# 101-add_attribute.py
# Gideon O Addo
"""Define a function add_attribute."""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Parameters:
        obj (any): The object to which the attribute should be added.
        attr (str): The name of the attribute to add.
        value (any): The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes,
        with the message "can't add a new attribute".
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
