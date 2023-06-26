#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    n = 0

    while (n <= x):

        try:
            print(my_list[n], end="")
            n++;
        except KeyError:
            pass
    
    if n > 0:
        print("");
        return (n + 1)
    else:
        return (0)
