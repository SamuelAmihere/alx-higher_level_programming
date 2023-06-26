#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    temp = []

    for n, i in enumerate(my_list_2):
        try:
            try:
                result = my_list_1[n] / i
            except (IndexError, UnboundLocalError):
                print("out of range")
                result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        finally:
            temp.append(result)

    return (temp)
