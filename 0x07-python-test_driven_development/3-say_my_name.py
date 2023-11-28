#!/usr/bin/python3
""" function print the first name and last name"""


def say_my_name(first_name, last_name=""):
    """say the name of person

    Args:
        first_name (str): first name of person
        last_name (str): last name of person Defaults to "".

    Raises:
        TypeError: if first name is not str
        TypeError: if last name is not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
