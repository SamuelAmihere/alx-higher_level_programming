#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import(
            add, sub, mul, div)

    av = sys.argv[1:]
    
    if len(av) != 3:
        print("{}".format(
            "Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    if av[1] not in ['+', '-', '*', '/']:
        print("{}".format(
            "Unknown operator. Available operators: +, -, * and /"))
        exit(1)

    for fn in [add, sub, mul, div]:
        print("{} {} {} = {}".format(
            av[0], av[1], av[2]
            fn(int(av[0])), int(av[2]))
