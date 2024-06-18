#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Gideon O Addo

import sys


def safe_print_integer_err(value):
    """Print an integer with error message

    Args:
        value (int): integer to print

    Return:
        True if value has been correctly printed
        (It means the value is an integer),
        otherwise, False and prints in stderr the error
        precede by Exception
    """
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
        print('Exception: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return False
