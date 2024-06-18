#!/usr/bin/python3
# 101-safe_function.py
# Gideon O Addo

import sys


def safe_function(fct, *args):
    """Execute a function a safely

    Args:
        fct (func): pointer to a function to execute
        *args: list of arguments
    Return:
        The result of the function, otherwise 'None' if something
        happens during the function and prints in stderr the
        error precede by Exception
    """
    try:
        result = fct(*args)
        return result
    except Exception:
        print('Exception: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return None
