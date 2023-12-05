#!/usr/bin/python3
"""Declaration of function"""
import json


def load_from_json_file(filename):
    """Returns an object represented by a JSON

    Args:
        filename: the name of file
    """
    with open(filename, "w") as my_file:
        json.load(my_file)
