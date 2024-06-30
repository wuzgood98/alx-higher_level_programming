#!/usr/bin/python3
# 5-text_indentation.py
# Gideon O Addo
"""Defines a function text_indetation"""


def text_indentation(text):
    """Print a text with 2 lines after eachh of these characters:
    ., ?, :

    Args:
        text (str): The text to be processed

    Raises:
        TypeError: If text is not a string

    Returns:
        No return
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    result = ''
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in '.?:':
            result += '\n\n'
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Split the result by new lines and strip each line to remove
    # leading trailing spaces
    lines = [line.strip() for line in result.split('\n')]
    final_result = '\n'.join(lines)

    print(final_result, end='')
