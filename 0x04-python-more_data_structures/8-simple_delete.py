#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    temp = {}
    for k, v in a_dictionary.items():
        if k != key:
            temp[k] = v
    return temp
