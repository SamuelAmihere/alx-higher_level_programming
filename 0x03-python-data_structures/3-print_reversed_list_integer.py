#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    st = len(my_list)
    en = -1

    for i in range(st, en, -1):
        print("{:d}".format(i))
