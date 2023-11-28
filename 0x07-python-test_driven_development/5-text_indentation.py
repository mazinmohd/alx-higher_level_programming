#!/usr/bin/python3
"""
function prints a text with 2 new lines after each ., ? and :
"""


def text_indentation(text):
    """prints a 2 new lines

    Args:
        text (str): the string we have

    Raises:
        TypeError: if text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
