#!/usr/bin/python3
# 3-safe_print_division.py
# Gideon O Addo

def safe_print_division(a, b):
    """Print the result of the division of 2 integers

    Args:
        a (int): integer for operation
        b (int): integer for operation

    Return:
        The value of the division, otherwise 'None'
    """
    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print('Inside result: {}'.format(result))
    return result
