#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        num = ord(ch)
        if (num - 32) in range(65, 91):
            ch = chr(num - 32)
        elif (_ord + 32) in range(97, 123):
            ch = chr(num)

        print("{}".format(ch), end="")
    print("")
