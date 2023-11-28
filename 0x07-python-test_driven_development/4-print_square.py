#!/usr/bin/python3
"""function print square of # """


def print_square(size):
    """print square of #

    Args:
        size (int): the size of square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
