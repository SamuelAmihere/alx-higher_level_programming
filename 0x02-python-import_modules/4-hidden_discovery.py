#!/usr/bin/python3
import hidden_4

for i in dir(hidden_4).sort():
    if i[0:2] != "__":
        print("{}".format(i))
