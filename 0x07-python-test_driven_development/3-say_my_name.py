#!/usr/bin/python3
# 3-say_my_name.py
# Gideon O Addo.
"""Defines a function say_my_name"""


def say_my_name(first_name, last_name=''):
    """Prints 'My name is <first name> <last name>'

    Args:
        first_name (str): first name of the user.
        last_name (str): last name of the user.

    Raises:
        TypeError: if either of first_name or last_name are not strings.

    Return:
        No return.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
