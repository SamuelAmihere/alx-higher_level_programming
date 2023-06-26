#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for n, i in enumerate(my_list[0: x]):
            try:
                print("{:d}".format(i), end="")
            except (ValueError, TypeError):
                if n > 0:
                    n -= 1
        print("")
        return (n + 1)
    except (IndexError, UnboundLocalError):
        return (0)
