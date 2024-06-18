#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Gideon O Addo

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers

    Args:
        my_list (list): list of elements to print
        x (int): number of elements to access in my_list

    Return:
        Real number of integers printed
    """
    return_value = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            return_value += 1
        except (TypeError, ValueError):
            continue
    print('')
    return return_value
