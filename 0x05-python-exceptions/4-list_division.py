#!/usr/bin/python3
# 4-list_division.py
# Gideon O Addo

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists

    Args:
        my_list_1 (list): list of elements 1
        my_list_2 (list): list of elements 2
        list_length (int): length of list

    Return:
        A new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            div = 0
        except ZeroDivisionError:
            print('division by 0')
            div = 0
        except IndexError:
            print('out of range')
            div = 0
        finally:
            new_list.append(div)
    return new_list
