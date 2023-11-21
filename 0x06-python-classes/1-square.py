#!/usr/bin/python3
"""define class"""


class Square:
    """ a square class
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size):
        """initalizes attributes
        Args:
            size (int): size of a side of the square
            Returns: None
        """
        self.__size = size
