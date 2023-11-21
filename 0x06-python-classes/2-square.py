#!/usr/bin/python3
"""initalize class"""


class Square:
    """class with private instance"""

    def __init__(slef, size=0):
        """
        Args:
            size: size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
