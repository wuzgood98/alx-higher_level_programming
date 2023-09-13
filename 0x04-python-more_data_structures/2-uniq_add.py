#!/usr/bin/python3

def uniq_add(my_list=[]):
    count = 0
    for num in set(my_list):
        count += num
    return count
