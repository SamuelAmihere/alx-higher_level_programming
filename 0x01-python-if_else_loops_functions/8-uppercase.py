#!/usr/bin/python3
def uppercase(str):
    for i, j in zip(range(97, 123), range(65, 91)):
        if i == 122:
            print("{}".format(j))
        if chr(i) in str or chr(j) in str:
            print("{}".format(j), end="")
