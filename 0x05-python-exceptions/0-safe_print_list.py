#!/usr/bin/python3
# 0-safe-_print_list.py
# Gideon O Addo

def safe_print_list(my_list=[], x=0):
    '''Print x elements of a list

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Return:
        The number of elements printed.
    '''
    return_value = 0
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end='')
            return_value += 1
        except IndexError:
            break
    print('')
    return return_value
