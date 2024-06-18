#!/usr/bin/python3
# 1-safe_print_integer.py
# Gideon O Addo

def safe_print_integer(value):
    """Print integer with '{}'.format()

    Args:
        value (int): integer to be printed
    Return:
        'True' if value has been correctly printed (It means
        value or type is an integer), otherwise 'False'.
    """
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
        return False
