#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    i = len(new_list) - 1
    if idx < 0 or idx > i:
        return my_list.copy()
    new_list[idx] = element
    return new_list
