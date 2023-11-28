#!/usr/bin/python3
"""Defines an addition function"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Raises:
        TypeError: if either of a or b is a non-int and non-float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
