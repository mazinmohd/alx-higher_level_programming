#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    length = len(sentence)
    tupl = ()
    if length == 0:
        tupl = 0, "None"
    else:
        tupl = length, first_char
    return tupl
