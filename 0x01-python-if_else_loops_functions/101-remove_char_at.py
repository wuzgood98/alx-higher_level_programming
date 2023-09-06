#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for index in range(len(str)):
        if index != n:
            string += str[index]

    return (string)
